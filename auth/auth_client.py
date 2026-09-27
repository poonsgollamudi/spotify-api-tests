import requests

from config.config import Config


class AuthClient:

    def get_access_token(self):
        response = requests.post(
            Config.SPOTIFY_AUTH_URL,
            data={
                "grant_type": "client_credentials"
            },
            auth=(
                Config.SPOTIFY_CLIENT_ID,
                Config.SPOTIFY_CLIENT_SECRET
            )
        )

        response.raise_for_status()

        return response.json()