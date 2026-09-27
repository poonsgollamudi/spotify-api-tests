from clients.base_client import BaseClient


class SearchClient(BaseClient):

    def search_tracks(
        self,
        query,
        limit=5,
        token=None,
        use_auth=True
    ):
        params = {
            "q": query,
            "type": "track",
            "limit": limit
        }

        return self.get(
            "/search",
            params=params,
            token=token,
            use_auth=use_auth
        )