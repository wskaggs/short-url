from functools import cache
from pydantic.networks import IPv4Address
from pydantic_settings import BaseSettings


class ApiSettings(BaseSettings):
    """
    The configurations (settings) of the short-url backend 
    """
    HOST: IPv4Address  # The host to serve the application to
    PORT: int  # The port to serve the application to
    SQLALCHEMY_DATABASE_URI: str  # The database uri


@cache
def get_settings() -> ApiSettings:
    """
    Get the settings for this api

    :return: the api settings object
    """
    return ApiSettings()
