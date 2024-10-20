import pytest


@pytest.fixture()
def sleep_time() -> int:
    return 5


@pytest.fixture()
def retry_times() -> int:
    return 3
