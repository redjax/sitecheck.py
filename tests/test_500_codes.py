from __future__ import annotations

import logging
import typing as t
import time

log = logging.getLogger(__name__)

from sitecheck import ConnectionManager, HTTPResponse

import pytest

logging.basicConfig(
    level="INFO",
    format="[TESTS] | %(asctime)s | [%(levelname)s] | (%(name)s)-> %(module)s.%(funcName)s:%(lineno)s > %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)


#######
# 500 #
#######
@pytest.mark.xfail
def test_fail_get_500_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/500")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 500 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_get_500_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/500")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 500 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


@pytest.mark.xfail
def test_fail_head_500_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/500")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 500 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_head_500_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/500")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 500, ValueError(
        f"Expected 500 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


#######
# 501 #
#######
@pytest.mark.xfail
def test_fail_get_501_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/501")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 501 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_get_501_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/501")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 501, ValueError(
        f"Expected 501 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


@pytest.mark.xfail
def test_fail_head_501_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/501")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 501 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_head_501_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/501")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 501, ValueError(
        f"Expected 501 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


#######
# 502 #
#######
@pytest.mark.xfail
def test_fail_get_502_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/502")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 502 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_get_502_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/502")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 502, ValueError(
        f"Expected 502 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


@pytest.mark.xfail
def test_fail_head_502_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/502")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 502 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_head_502_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/502")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 502, ValueError(
        f"Expected 502 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


#######
# 503 #
#######
@pytest.mark.xfail
def test_fail_get_503_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/503")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 503 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_get_503_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/503")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 503, ValueError(
        f"Expected 503 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


@pytest.mark.xfail
def test_fail_head_503_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/503")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 503 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_head_503_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/503")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 503, ValueError(
        f"Expected 503 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


#######
# 504 #
#######
@pytest.mark.xfail
def test_fail_get_504_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/504")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 504 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_get_504_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/504")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 504, ValueError(
        f"Expected 504 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


@pytest.mark.xfail
def test_fail_head_504_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/504")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 504 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_head_504_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/504")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 504, ValueError(
        f"Expected 504 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


#######
# 511 #
#######
@pytest.mark.xfail
def test_fail_get_511_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/511")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 511 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_get_511_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/511")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="GET", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 511, ValueError(
        f"Expected 511 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


@pytest.mark.xfail
def test_fail_head_511_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/511")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 200, ValueError(
        f"Expected 511 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)


def test_head_511_response(sleep_time: int, retry_times: int):
    connection_manager = ConnectionManager(url="https://http.codes/511")

    res: dict[str, t.Any] = connection_manager.send_request(
        method="HEAD", sleep=sleep_time, retries=retry_times
    )

    assert res["status_code"] == 511, ValueError(
        f"Expected 511 response code, got: {res['status_code']}"
    )

    # print(
    #     f"Sleep for {sleep_time} second(s) after request to avoid spamming http.codes/ site."
    # )
    # time.sleep(sleep_time)
