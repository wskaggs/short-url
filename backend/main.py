from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "hello, world"}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}
