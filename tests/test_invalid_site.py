from __future__ import annotations

import logging
import typing as t

log = logging.getLogger(__name__)

from sitecheck import ConnectionManager, HTTPResponse

import pytest

logging.basicConfig(
    level="INFO",
    format="[TESTS] | %(asctime)s | [%(levelname)s] | (%(name)s)-> %(module)s.%(funcName)s:%(lineno)s > %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)


@pytest.mark.xfail
def test_fail_invalid_site(sleep_time: int, retry_times: int, invalid_site: str):
    connection_manager = ConnectionManager(url=invalid_site)

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_invalid_site(sleep_time: int, retry_times: int, invalid_site: str):
    connection_manager = ConnectionManager(url=invalid_site)

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res is None, ValueError(
        f"res should be None due to an invalid website address, but was instead ({type(res)})"
    )
