import uvicorn
from api import create_api
from api.settings import get_settings

api = create_api()

if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run("main:api", workers=4, host=str(settings.HOST), port=settings.PORT)
