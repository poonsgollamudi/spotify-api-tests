from utils.schema_validator import validate_schema
import pytest

from data.search_data import SEARCH_QUERIES, SEARCH_LIMIT_CASES, SEARCH_LIMIT_BOUNDARIES

@pytest.mark.smoke
def test_search_tracks_returns_success(search_client):

    response = search_client.search_tracks(
        query="Naruto",
        limit=5
    )

    assert response.status_code == 200

@pytest.mark.smoke
def test_search_tracks_returns_tracks(search_client):

    response = search_client.search_tracks(
        query="Naruto",
        limit=5
    )

    data = response.json()

    assert response.status_code == 200
    assert "tracks" in data
    assert "items" in data["tracks"]
    assert isinstance(data["tracks"]["items"], list)


@pytest.mark.smoke
def test_search_tracks_respects_limit(search_client):

    response = search_client.search_tracks(
        query="Naruto",
        limit=3
    )

    data = response.json()

    assert response.status_code == 200
    assert len(data["tracks"]["items"]) <= 3

@pytest.mark.auth
def test_request_without_token_returns_401(search_client):

    response = search_client.search_tracks(
        query="Naruto",
        use_auth=False
    )

    assert response.status_code == 401

@pytest.mark.auth
def test_request_with_invalid_token_returns_401(search_client):

    response = search_client.search_tracks(
        query="Naruto",
        token="invalid-token"
    )

    assert response.status_code == 401

@pytest.mark.auth
def test_invalid_token_returns_error_response(search_client):

    response = search_client.search_tracks(
        query="Naruto",
        token="invalid-token"
    )

    data = response.json()

    assert response.status_code == 401
    assert "error" in data
    assert data["error"]["status"] == 401
    assert "message" in data["error"]

@pytest.mark.schema
def test_search_tracks_matches_schema(search_client):

    response = search_client.search_tracks(
        query="Naruto",
        limit=5
    )

    assert response.status_code == 200

    validate_schema(
        response.json(),
        "search_response_schema.json"
    )

@pytest.mark.regression
@pytest.mark.parametrize("query", SEARCH_QUERIES)
def test_search_tracks_with_different_queries(search_client, query):

    response = search_client.search_tracks(
        query=query,
        limit=5
    )

    assert response.status_code == 200

    data = response.json()

    assert "tracks" in data
    assert isinstance(data["tracks"]["items"], list)

@pytest.mark.regression
@pytest.mark.parametrize(
    "query, limit",
    SEARCH_LIMIT_CASES,
    ids=[
        "single-result",
        "three-results",
        "five-results",
        "ten-results"
    ]
)
def test_search_tracks_with_different_limits(
    search_client,
    query,
    limit
):
    response = search_client.search_tracks(
        query=query,
        limit=limit
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["tracks"]["items"]) <= limit

@pytest.mark.regression
@pytest.mark.parametrize(
    "query, limit",
    SEARCH_LIMIT_BOUNDARIES
)
def test_search_limit_boundaries(
    search_client,
    query,
    limit
):
    response = search_client.search_tracks(
        query=query,
        limit=limit
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["tracks"]["items"]) <= limit