import json
from typing import Dict, Any

import requests

from chaoslib.types import Configuration, Secrets
from requests import Response


def call_api(base_url: str,
             api_endpoint: str,
             method: str = "GET",
             assaults_configurations: Dict[str, Any] = None,
             headers: Dict[str, Any] = None,
             timeout: float = None,
             configuration: Configuration = None,
             secrets: Secrets = None,
             ) -> Response:
    url = f"{base_url}/{api_endpoint}"
    headers = headers or {}
    headers.setdefault("Accept", "application/json")

    params = {}
    if timeout:
        params["timeout"] = timeout

    data = None
    if assaults_configurations:
        data = json.dumps(assaults_configurations)
        headers.setdefault("Content-Type", "application/json")

    return requests.request(method, url, params=params, data=data, headers=headers)
