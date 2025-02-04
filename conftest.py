import pytest

from libs.core.api.cat_facts_api import CatFactsApi


@pytest.fixture
def cats_api_client() -> CatFactsApi:
    api = CatFactsApi()
    yield api
    api.session.close()
