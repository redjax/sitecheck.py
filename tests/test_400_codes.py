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
# 400 #
#######
@pytest.mark.xfail
def test_fail_get_400_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/400")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 400 response code, got: {res['status_code']}"
    )


def test_get_400_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/400")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 400, ValueError(
        f"Expected 400 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_400_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/400")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 400 response code, got: {res['status_code']}"
    )


def test_head_400_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/400")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 400, ValueError(
        f"Expected 400 response code, got: {res['status_code']}"
    )


#######
# 401 #
#######
@pytest.mark.xfail
def test_fail_get_401_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/401")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 401 response code, got: {res['status_code']}"
    )


def test_get_401_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/401")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 401, ValueError(
        f"Expected 401 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_401_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/401")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 401 response code, got: {res['status_code']}"
    )


def test_head_401_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/401")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 401, ValueError(
        f"Expected 401 response code, got: {res['status_code']}"
    )


#######
# 402 #
#######
@pytest.mark.xfail
def test_fail_get_402_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/402")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 402 response code, got: {res['status_code']}"
    )


def test_get_402_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/402")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 402, ValueError(
        f"Expected 402 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_402_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/402")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 402 response code, got: {res['status_code']}"
    )


def test_head_402_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/402")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 402, ValueError(
        f"Expected 402 response code, got: {res['status_code']}"
    )


#######
# 404 #
#######
@pytest.mark.xfail
def test_fail_get_404_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/404")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 404 response code, got: {res['status_code']}"
    )


def test_get_404_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/404")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 404, ValueError(
        f"Expected 404 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_404_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/404")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 404 response code, got: {res['status_code']}"
    )


def test_head_404_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/404")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 404, ValueError(
        f"Expected 404 response code, got: {res['status_code']}"
    )


#######
# 405 #
#######
@pytest.mark.xfail
def test_fail_get_405_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/405")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 405 response code, got: {res['status_code']}"
    )


def test_get_405_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/405")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 405, ValueError(
        f"Expected 405 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_405_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/405")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 405 response code, got: {res['status_code']}"
    )


def test_head_405_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/405")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 405, ValueError(
        f"Expected 405 response code, got: {res['status_code']}"
    )


#######
# 406 #
#######
@pytest.mark.xfail
def test_fail_get_406_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/406")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 406 response code, got: {res['status_code']}"
    )


def test_get_406_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/406")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 406, ValueError(
        f"Expected 406 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_406_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/406")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 406 response code, got: {res['status_code']}"
    )


def test_head_406_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/406")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 406, ValueError(
        f"Expected 406 response code, got: {res['status_code']}"
    )


#######
# 407 #
#######
@pytest.mark.xfail
def test_fail_get_407_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/407")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 407 response code, got: {res['status_code']}"
    )


def test_get_407_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/407")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 407, ValueError(
        f"Expected 407 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_407_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/407")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 407 response code, got: {res['status_code']}"
    )


def test_head_407_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/407")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 407, ValueError(
        f"Expected 407 response code, got: {res['status_code']}"
    )


#######
# 408 #
#######
@pytest.mark.xfail
def test_fail_get_408_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/408")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 408 response code, got: {res['status_code']}"
    )


def test_get_408_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/408")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 408, ValueError(
        f"Expected 408 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_408_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/408")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 408 response code, got: {res['status_code']}"
    )


def test_head_408_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/408")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 408, ValueError(
        f"Expected 408 response code, got: {res['status_code']}"
    )


#######
# 409 #
#######
@pytest.mark.xfail
def test_fail_get_409_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/409")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 409 response code, got: {res['status_code']}"
    )


def test_get_409_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/409")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 409, ValueError(
        f"Expected 409 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_409_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/409")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 409 response code, got: {res['status_code']}"
    )


def test_head_409_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/409")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 409, ValueError(
        f"Expected 409 response code, got: {res['status_code']}"
    )


#######
# 410 #
#######
@pytest.mark.xfail
def test_fail_get_410_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/410")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 410 response code, got: {res['status_code']}"
    )


def test_get_410_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/410")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 410, ValueError(
        f"Expected 410 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_410_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/410")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 410 response code, got: {res['status_code']}"
    )


def test_head_410_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/410")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 410, ValueError(
        f"Expected 410 response code, got: {res['status_code']}"
    )


#######
# 415 #
#######
@pytest.mark.xfail
def test_fail_get_415_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/415")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 415 response code, got: {res['status_code']}"
    )


def test_get_415_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/415")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 415, ValueError(
        f"Expected 415 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_415_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/415")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 415 response code, got: {res['status_code']}"
    )


def test_head_415_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/415")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 415, ValueError(
        f"Expected 415 response code, got: {res['status_code']}"
    )
