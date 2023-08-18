import os
import uvicorn

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from controllers.__init__ import private_api_router, public_api_router
from middlewares.auth_middleware import AuthMiddleware

if os.getenv("FLASK_ENV") == 'development':
    load_dotenv(dotenv_path=f'.env.{os.getenv("FLASK_ENV")}')

app = FastAPI()
app.include_router(private_api_router, prefix=os.getenv('API_PREFIX'), dependencies=[Depends(AuthMiddleware())])
app.include_router(public_api_router, prefix=os.getenv('API_PREFIX'))

# Static folder
app.mount(os.getenv('STATIC_PUBLIC_FOLDER'), StaticFiles(directory='public/images'), name="images")

@app.get("/")
def hello():
    return {"message": "Hello world, FastAPI!"}


if __name__ == "__main__":
    uvicorn.run(app)
