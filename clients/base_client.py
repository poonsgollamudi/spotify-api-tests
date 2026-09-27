import requests

from auth.token_manager import TokenManager
from config.config import Config
from utils.logger import get_logger


logger = get_logger(__name__)


class BaseClient:

    def __init__(self):
        self.base_url = Config.SPOTIFY_BASE_URL
        self.token_manager = TokenManager()

    def _get_headers(self, token=None, use_auth=True):

        headers = {
            "Accept": "application/json"
        }

        if use_auth:
            if token is None:
                token = self.token_manager.get_token()

            headers["Authorization"] = f"Bearer {token}"

        return headers

    def get(
        self,
        endpoint,
        params=None,
        token=None,
        use_auth=True
    ):

        url = f"{self.base_url}{endpoint}"

        logger.info(
            "GET %s | params=%s",
            url,
            params
        )

        response = requests.get(
            url,
            headers=self._get_headers(
                token=token,
                use_auth=use_auth
            ),
            params=params
        )

        logger.info(
            "Response | status=%s | duration=%.3fs",
            response.status_code,
            response.elapsed.total_seconds()
        )

        if response.status_code >= 400:
            logger.warning(
                "Non-success response | status=%s | body=%s",
                response.status_code,
                response.text[:500]
            )

        return response