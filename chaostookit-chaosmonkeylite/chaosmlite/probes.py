# -*- coding: utf-8 -*-
from typing import Any, Dict

from chaoslib.exceptions import ActivityFailed
from chaoslib.types import Configuration, Secrets
from requests.status_codes import codes

from chaosmlite import api

__all__ = ["chaosmonkey_enabled"]


def chaosmonkey_enabled(
        base_url: str,
        headers: Dict[str, Any] = None,
        timeout: float = None,
        configuration: Configuration = None,
        secrets: Secrets = None,
) -> bool:
    """
    enquire if chaosmonkey is enabled on the specified service.
    """
    response = api.call_api(base_url=base_url, headers=headers, timeout=timeout, configuration=configuration,
                            secrets=secrets, api_endpoint="chaosmonkey/status")

    if response.status_code == codes.ok:
        return True
    elif response.status_code == codes.service_unavailable:
        return False
    else:
        raise ActivityFailed("chaosmonkey status enquiry failed: {m}".format(m=response.text))
