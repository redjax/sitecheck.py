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

from .test_200_codes import test_fail_head_200_response, test_get_200_response
from .test_300_codes import (
    test_fail_head_300_response,
    test_fail_head_301_response,
    test_fail_head_302_response,
)
from .test_400_codes import (
    test_fail_head_400_response,
    test_fail_head_401_response,
    test_fail_head_404_response,
)
from .test_500_codes import test_fail_head_500_response, test_fail_head_501_response
