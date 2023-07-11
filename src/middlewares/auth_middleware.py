from fastapi import HTTPException, Request, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from utils.security import Security

security = HTTPBearer()


class AuthMiddleware(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(AuthMiddleware, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        security_utils = Security()
        credentials: HTTPAuthorizationCredentials = await super(AuthMiddleware, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")
            if not security_utils.verify_token(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")
