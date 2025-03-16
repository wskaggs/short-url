import uvicorn
from api import create_api
from api.settings import settings

api = create_api()

if __name__ == "__main__":
    uvicorn.run("main:api", workers=4, host=settings.HOST, port=settings.PORT)
