from __future__ import annotations

import pytest


@pytest.fixture()
def sleep_time() -> int:
    return 5


@pytest.fixture()
def retry_times() -> int:
    return 3


@pytest.fixture()
def invalid_site() -> str:
    return "http://111.222"
