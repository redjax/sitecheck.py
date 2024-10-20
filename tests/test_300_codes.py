import logging
import typing as t

log = logging.getLogger(__name__)

import pytest

from sitecheck import ConnectionManager, HTTPResponse

logging.basicConfig(
    level="INFO",
    format="[TESTS] | %(asctime)s | [%(levelname)s] | (%(name)s)-> %(module)s.%(funcName)s:%(lineno)s > %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)


#######
# 300 #
#######
@pytest.mark.xfail
def test_fail_get_300_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/300")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 300 response code, got: {res['status_code']}"
    )


def test_get_300_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/300")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 300, ValueError(
        f"Expected 300 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_300_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/300")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 300 response code, got: {res['status_code']}"
    )


def test_head_300_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/300")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 300, ValueError(
        f"Expected 300 response code, got: {res['status_code']}"
    )


#######
# 301 #
#######
@pytest.mark.xfail
def test_fail_get_301_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/301")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_get_301_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/301")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_301_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/301")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_head_301_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/301")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


#######
# 302 #
#######
@pytest.mark.xfail
def test_fail_get_302_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/302")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_get_302_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/302")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_302_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/302")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_head_302_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/302")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


#######
# 303 #
#######
@pytest.mark.xfail
def test_fail_get_303_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/303")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_get_303_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/303")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_303_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/303")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_head_303_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/303")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


#######
# 304 #
#######
@pytest.mark.xfail
def test_fail_get_304_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/304")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 304 response code, got: {res['status_code']}"
    )


def test_get_304_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/304")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 304, ValueError(
        f"Expected 304 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_304_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/304")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 304 response code, got: {res['status_code']}"
    )


def test_head_304_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/304")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 304, ValueError(
        f"Expected 304 response code, got: {res['status_code']}"
    )


#######
# 307 #
#######
@pytest.mark.xfail
def test_fail_get_307_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/307")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_get_307_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/307")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_307_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/307")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_head_307_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/307")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


#######
# 308 #
#######
@pytest.mark.xfail
def test_fail_get_308_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/308")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_get_308_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/308")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


@pytest.mark.xfail
def test_fail_head_308_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/308")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )


def test_head_308_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/308")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 200 response code, got: {res['status_code']}"
    )
