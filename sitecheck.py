"""Make a request to a given site to test availability.

Description:
    Call the script, passing args to set a site, method, & optional success/failure codes.
    The script will make a `HEAD` request to the site, expecting a `200: OK` response, and retrying
    a specified number of times before determining site is offline.
    
    Check the available options with `sitecheck.py --help`.
    
Usage:
    - `-h`/`--help`: Show help message
    - `--site SITE`: Set the site address to request, i.e. `https://www.google.com`
    - `--method`: (Optional, default=`HEAD`) The HTTP method type, i.e. `GET`, `HEAD`, etc.
    - `--success-codes SUCCESS_CODES`: (Optional, default=<predefined list>) Specify success codes, i.e. `--success-codes 200 201 202`.
    - `--failure-codes FAILURE_CODES`: (Optional, default=<predefined list>) Specify failure codes, i.e. `--failure-codes 400, 404, 500`.
    - `--headers HEADERS`: (Optional, default=None): Pass request headers, i.e. `--headers '{"Content-Type": "application/json", "Authorization": "Bearer: <api-key>"}'
    - `--body BODY`: (Optional, default=`None`): Pass a request body, i.e. `--body '{"someKey": "someValue"}'`. The body must be quoted, and
        will be converted to JSON for the request.
    - `--sleep SLEEP`: (default=5) Time in seconds to pause between retries.
    - `--retries RETRIES`: (default=3) Number of retries on error.
    
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import http.client
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

        self.trace = None

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

        if exc_val:
            msg = f"({exc_type}) {exc_val}"
            log.error(msg)

            self.trace = traceback

            return False

        return True

    def send_request(self, method: str, sleep: int, retries: int) -> dict[str, t.Any]:
        log.info(f"Sending {method} request to URL: {self.parsed_url.geturl()}")

        with (
            self
        ):  # Use the context manager to open and automatically close the connection
            for attempt in range(retries):
                try:
                    # Send the request with the specified method (HEAD, GET, etc.)
                    self.connection.request(
                        method=method,
                        url=self.parsed_url.path or "/",
                        body=self.body,
                        headers=self.headers,
                    )

                    # Get the response
                    response: http.client.HTTPResponse = self.connection.getresponse()
                    log.info(f"Response: [{response.status}]")

                    # Extract the HTTP status code, reason phrase, and headers
                    status_code: int = response.status
                    reason: str = response.reason
                    headers: list[tuple[str, str]] = response.getheaders()

                    # Handle redirects (301, 302, 303, 307, 308)
                    if status_code in {301, 302, 303, 307, 308}:
                        log.info(f"Redirected: {status_code} {reason}")
                        location = response.getheader("Location")
                        if location:
                            log.info(f"Following redirect to: {location}")
                            # Update the URL and retry the request
                            self.parsed_url = urllib.parse.urlparse(location)
                            self.connection.close()  # Close the previous connection
                            self.connection = None  # Reset the connection
                            return self.send_request(method, sleep, retries)

                    return {
                        "status_code": status_code,
                        "reason": reason,
                        "headers": headers,
                    }

                except gaierror as invalid_site:
                    msg = f"({type(invalid_site)}) Invalid site address: '{self.parsed_url.geturl()}'."
                    log.error(msg)
                    raise invalid_site

                except Exception as exc:
                    msg = f"({type(exc)}) Error connecting to URL: {self.parsed_url.geturl()}. Attempt {attempt + 1}/{retries} failed. Details: {exc}"
                    log.error(msg)

                    # If this was not the last attempt, wait for the specified sleep duration
                    if attempt < retries - 1:
                        log.info(f"Retrying in {sleep} seconds...")
                        time.sleep(sleep)

            # If all retries failed, raise an exception
            raise Exception(
                f"Failed to connect to {self.parsed_url.geturl()} after {retries} attempts."
            )


def parse_args() -> argparse.Namespace:
    """Parse CLI args passed to the script."""

    ## Initialize parser
    parser = argparse.ArgumentParser(
        description="Check a website's status with HEAD request."
    )

    ## Site URL to request
    parser.add_argument("--site", required=True, help="URL of the site to check.")
    ## Request method
    parser.add_argument(
        "--method",
        default="HEAD",
        choices=["GET", "POST", "PUT", "HEAD", "DELETE"],
        type=str.upper,
        help="HTTP method to use (i.e. GET, POST, HEAD).",
    )
    ## List of codes that qualify as a succcessful response
    parser.add_argument(
        "--success-codes",
        nargs="+",
        type=int,
        default=DEFAULT_HTTP_SUCCESS_CODES,
        help="List of HTTP success codes.",
    )
    ## List of codes that qualify as a failure response
    parser.add_argument(
        "--failure-codes",
        nargs="+",
        type=int,
        default=DEFAULT_HTTP_FAILURE_CODES,
        help="List of HTTP failure codes.",
    )
    ## Headers dict (formatted as a string, i.e. '{"Key-Name": "Key-Value"}')
    parser.add_argument("--headers", type=str, default=None, help="Headers dict")
    ## Body dict (formatted as a string, i.e. '{"Body-Name": "Body-Value"}')
    parser.add_argument(
        "--body",
        type=str,
        help="Optional request body as a JSON string.",
    )
    ## Number of seconds to sleept between requests
    parser.add_argument(
        "--sleep",
        type=int,
        default=5,
        help="Number of seconds to wait before retrying.",
    )
    ## Number of retries when failure
    parser.add_argument(
        "--retries",
        type=int,
        default=1,
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
