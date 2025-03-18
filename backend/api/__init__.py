from fastapi import FastAPI
from api.dependencies import Settings


def create_api() -> FastAPI:
    """
    Factory to create and configure the FastAPI application

    :return: the FastAPI application
    """
    api = FastAPI()

    @api.get("/")
    async def root(settings: Settings) -> dict[str, str]:
        return {"database_uri": settings.SQLALCHEMY_DATABASE_URI}

    @api.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "healthy"}

    return api
