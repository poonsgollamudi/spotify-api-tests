import pytest

from clients.search_client import SearchClient


@pytest.fixture
def search_client():
    return SearchClient()