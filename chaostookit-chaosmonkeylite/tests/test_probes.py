from unittest import mock
from unittest.mock import MagicMock

import pytest
from requests import Response, codes

from chaosmlite.probes import chaosmonkey_enabled


def test_chaosmonkey_is_enabled():
    mock_response = MagicMock(Response, status_code=codes.ok)
    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch("chaosmlite.api.call_api", return_value=mock_response) as mock_call_api:
        enabled = chaosmonkey_enabled(base_url=actuator_endpoint)

    assert enabled
    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/status",
                                          headers=None,
                                          configuration=None,
                                          secrets=None,
                                          timeout=None)
