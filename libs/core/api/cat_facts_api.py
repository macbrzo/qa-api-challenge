from typing import Optional

import config

from .api_client import ApiClient


class CatFactsApi(ApiClient):
    def __init__(
        self,
        base_url=config.api_base_url,
        timeout=config.request_timeout,
    ):
        super().__init__(base_url=base_url, timeout=timeout)
        self.session.headers.update(
            {"Accept": "application/json", "User-Agent": "CatFactsAPIClient/1.0.0"}
        )

    @staticmethod
    def build_params(
        max_length: Optional[int] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ):
        params = {}
        if max_length:
            params["max_length"] = max_length
        if limit:
            params["limit"] = limit
        if page:
            params["page"] = page
        return params

    def get_fact(self, max_length: Optional[int] = None):
        params = self.build_params(max_length=max_length)
        return self.get("/fact", params=params)

    def get_facts(
        self,
        max_length: Optional[int] = None,
        limit: Optional[int] = None,
    ):
        params = self.build_params(max_length=max_length, limit=limit)
        return self.get("/facts", params=params)
