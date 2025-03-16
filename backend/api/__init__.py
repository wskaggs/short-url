from fastapi import FastAPI


def create_api() -> FastAPI:
    """
    Factory to create and configure the FastAPI application

    :return: the FastAPI application
    """
    api = FastAPI()

    @api.get("/")
    async def root() -> dict[str, str]:
        return {"message": "hello, world"}

    @api.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "healthy"}

    return api
