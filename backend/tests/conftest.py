from collections.abc import Generator
from functools import cache
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture
from api import create_api
from api.settings import ApiSettings, get_settings


@cache
def get_test_settings() -> ApiSettings:
    """
    Override settings for a testing environment

    :return: the modified settings
    """
    settings = get_settings()

    settings.SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

    return settings


@fixture(scope="module")
def test_client() -> Generator[TestClient, None, None]:
    """
    Get a client to test the api without a running server

    :return: a test client
    """
    api = create_api()

    api.dependency_overrides[get_settings] = get_test_settings

    with TestClient(api) as client:
        yield client
