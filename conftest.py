import pytest

from libs.system.cat_facts.cat_facts_api import CatFactsApi


@pytest.fixture
def cats_api_client() -> CatFactsApi:
    api = CatFactsApi()
    yield api
    api.session.close()
