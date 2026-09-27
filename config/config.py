import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

    SPOTIFY_AUTH_URL = os.getenv("SPOTIFY_AUTH_URL")
    SPOTIFY_BASE_URL = os.getenv("SPOTIFY_BASE_URL")