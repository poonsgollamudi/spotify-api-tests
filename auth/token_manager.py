import time

from auth.auth_client import AuthClient


class TokenManager:

    def __init__(self):
        self.auth_client = AuthClient()
        self._access_token = None
        self._expires_at = 0

    def get_token(self):
        if self._access_token is None or self._is_token_expired():
            self._request_new_token()

        return self._access_token

    def _request_new_token(self):
        token_response = self.auth_client.get_access_token()

        self._access_token = token_response["access_token"]

        expires_in = token_response["expires_in"]

        self._expires_at = time.time() + expires_in

    def _is_token_expired(self):
        return time.time() >= self._expires_at - 30