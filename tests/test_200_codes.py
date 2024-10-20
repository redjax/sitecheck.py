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


#######
# 200 #
#######
@pytest.mark.xfail
def test_fail_get_200_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/200")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_get_200_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/200")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_200_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/200")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_head_200_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/200")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


#######
# 201 #
#######
@pytest.mark.xfail
def test_fail_get_201_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/201")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 201 response code, got: {res['status_code']}"
    )


def test_get_201_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/201")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 201, ValueError(
        f"Expected 201 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_201_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/201")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 201 response code, got: {res['status_code']}"
    )


def test_get_head_201_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/201")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 201, ValueError(
        f"Expected 201 response code, got: {res['status_code']}"
    )


#######
# 202 #
#######
@pytest.mark.xfail
def test_fail_get_202_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/202")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 202 response code, got: {res['status_code']}"
    )


def test_get_202_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/202")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 202, ValueError(
        f"Expected 202 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_202_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/202")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 202 response code, got: {res['status_code']}"
    )


def test_get_head_202_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/202")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 202, ValueError(
        f"Expected 202 response code, got: {res['status_code']}"
    )
