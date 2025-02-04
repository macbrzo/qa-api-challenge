from typing import Dict, Optional
from urllib.parse import urljoin

import requests
from requests import Response


class ApiClient:
    def __init__(
        self,
        base_url: str,
        timeout: int = 10,
    ):
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = timeout

    def get(
        self,
        endpoint: str,
        params: Optional[Dict] = None,
        timeout: Optional[int] = None,
    ) -> Response:
        if not params:
            params = {}
        url = urljoin(self.base_url, endpoint)
        return self.session.get(
            url=url,
            params=params,
            timeout=timeout or self.timeout,
        )
