from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
import uvicorn
from config.database_config import db
from controllers.__init__ import private_api_router, public_api_router
from middlewares.auth_middleware import AuthMiddleware

app = FastAPI()
app.include_router(private_api_router, prefix="/api", dependencies=[Depends(AuthMiddleware())])
app.include_router(public_api_router, prefix="/api")

# Static folder
app.mount("/api/public/images", StaticFiles(directory='public/images'), name="images")

@app.get("/")
def hello():
    return {"message": "Hello world, FastAPI!"}


if __name__ == "__main__":
    app.db = db
    uvicorn.run(app, host="0.0.0.0", port=5000)
