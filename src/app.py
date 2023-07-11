from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config.database_config import database
from controllers.__init__ import private_api_router, public_api_router
from middlewares.auth_middleware import AuthMiddleware

app = FastAPI()
app.include_router(private_api_router, prefix="/api",
                   dependencies=[Depends(AuthMiddleware())])
app.include_router(public_api_router, prefix="/api")


@app.get("/")
def hello():
    return {"message": "Hello world, FastAPI!"}


if __name__ == "__main__":
    app.db = database
    uvicorn.run(app, host="0.0.0.0", port=5000)
