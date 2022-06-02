import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

SERVER_HOST: str = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT: int = int(os.getenv("SERVER_PORT", "4569"))
