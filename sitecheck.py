from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import http.client
from http.client import CannotSendHeader, CannotSendRequest, NotConnected
import json
import logging
from socket import gaierror
import time
import typing as t
import urllib.parse

log: logging.Logger = logging.getLogger(__name__)

DEFAULT_HTTP_SUCCESS_CODES: list[int] = [200, 201, 202]
DEFAULT_HTTP_FAILURE_CODES: list[int] = [400, 401, 402, 403, 404, 500, 501, 502]


@dataclass
class HTTPResponse:
    """Custom class to store the response from a request."""

    status_code: int
    reason: str | None = field(default=None)
    headers: list[tuple[str, str]] | None = field(default=None)


class ConnectionManager:
    """Custom context manager for HTTP/HTTPS connections."""

    def __init__(
        self,
        url: str,
        headers: dict | None = None,
        body: t.Union[dict, str] | None = None,
    ) -> None:
        self.logger: logging.Logger = log.getChild("ConnectionManager")
        self.connection = None
        self.parsed_url: urllib.parse.ParseResult | t.Any = self._ensure_schema(url)
        self.headers: dict = headers or {}
        self.body: bytes = self._prepare_body(body)

    def _ensure_schema(self, url) -> urllib.parse.ParseResult | t.Any:
        parsed = urllib.parse.urlparse(url)
        if not parsed.scheme:
            self.logger.warning(
                f"No schema provided for URL: {url}. Assuming 'http://'"
            )
            url: str = f"http://{url}"
            parsed: urllib.parse.ParseResult = urllib.parse.urlparse(url)
        return parsed

    def _prepare_body(self, body: t.Union[dict, str] | None) -> bytes | None:
        if isinstance(body, dict):
            body = json.dumps(body).encode(encoding="utf-8")
        elif isinstance(body, str):
            body = body.encode(encoding="utf-8")
        return body

    def __enter__(self) -> http.client.HTTPSConnection | http.client.HTTPConnection:
        if self.parsed_url.scheme == "https":
            self.connection = http.client.HTTPSConnection(self.parsed_url.netloc)
        else:
            self.connection = http.client.HTTPConnection(self.parsed_url.netloc)
        return self.connection

    def __exit__(self, exc_type, exc_val, traceback) -> bool:
        if self.connection:
            self.connection.close()
        return True  # Allow exception propagation

    def send_request(self, method: str, sleep: int, retries: int) -> dict[str, t.Any]:
        log.info(f"Sending {method} request to URL: {self.parsed_url.geturl()}")

        with (
            self
        ):  # Use the context manager to open and automatically close the connection
            for attempt in range(retries):
                try:
                    self.connection.request(
                        method=method,
                        url=self.parsed_url.path or "/",
                        body=self.body,
                        headers=self.headers,
                    )
                    response: http.client.HTTPResponse = self.connection.getresponse()
                    status_code: int = response.status
                    reason: str = response.reason
                    headers: list[tuple[str, str]] = response.getheaders()
                    return {
                        "status_code": status_code,
                        "reason": reason,
                        "headers": headers,
                    }

                except gaierror as invalid_site:
                    msg = f"({type(invalid_site)}) Invalid site address: '{self.parsed_url.geturl()}'."
                    log.error(msg)
                    return None  # Return None to indicate failure

                except Exception as exc:
                    msg = f"({type(exc)}) Error connecting to URL: {self.parsed_url.geturl()}. Attempt {attempt + 1}/{retries} failed. Details: {exc}"
                    log.error(msg)

                    if attempt < retries - 1:
                        log.info(f"Retrying in {sleep} seconds...")
                        time.sleep(sleep)

            raise Exception(
                f"Failed to connect to {self.parsed_url.geturl()} after {retries} attempts."
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a website's status with HEAD request."
    )

    # Arguments for site URL, method (for future extensions), success codes, and failure codes
    parser.add_argument("--site", required=True, help="URL of the site to check.")
    parser.add_argument(
        "--method",
        default="HEAD",
        choices=["GET", "POST", "PUT", "HEAD", "DELETE"],
        type=str.upper,
        help="HTTP method to use (i.e. GET, POST, HEAD).",
    )
    parser.add_argument(
        "--success-codes",
        nargs="+",
        type=int,
        default=DEFAULT_HTTP_SUCCESS_CODES,
        help="List of HTTP success codes.",
    )
    parser.add_argument(
        "--failure-codes",
        nargs="+",
        type=int,
        default=DEFAULT_HTTP_FAILURE_CODES,
        help="List of HTTP failure codes.",
    )
    parser.add_argument(
        "--body",
        type=str,
        help="Optional request body as a JSON string.",
    )
    parser.add_argument(
        "--sleep",
        type=int,
        default=5,
        help="Number of seconds to wait before retrying.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Number of retry attempts for failed requests.",
    )

    return parser.parse_args()


def main() -> None:
    args: argparse.Namespace = parse_args()

    ## Create an instance of ConnectionManager with headers and body
    headers: dict[str, str] = {"Content-Type": "application/json"}
    ## Load body from JSON string, if provided
    body: t.Any | None = json.loads(args.body) if args.body else None

    connection_manager = ConnectionManager(url=args.site, headers=headers, body=body)

    ## Make the request with the specified sleep and retries
    res: dict[str, t.Any] = connection_manager.send_request(
        method=args.method, sleep=args.sleep, retries=args.retries
    )

    if res is None:
        log.error(f"Failed to connect to site: {args.site}.")
        exit(1)

    result: HTTPResponse = HTTPResponse(
        status_code=res["status_code"], reason=res["reason"], headers=res["headers"]
    )

    # Check if the status code is in success or failure codes
    if result.status_code in args.success_codes:
        log.info(f"Success: {result.status_code} {result.reason}")
    elif result.status_code in args.failure_codes:
        log.error(f"Failure: {result.status_code} {result.reason}")
    else:
        log.warning(f"Unexpected status: {result.status_code} {result.reason}")


if __name__ == "__main__":
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s | [%(levelname)s] | line:%(lineno)s > %(message)s",
        datefmt=("%Y-%m-%dT%H:%M:%S"),
    )

    main()
