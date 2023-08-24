from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services.auth_service import AuthService

security = HTTPBearer()


class AuthMiddleware(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        auth_service = AuthService()
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=401, detail="Invalid authentication scheme.")

            user = auth_service.get_access_token(credentials.credentials)

            if not user:
                raise HTTPException(status_code=401, detail="Invalid token or expired token.")

            request.state.user = user

            return user

        raise HTTPException(status_code=401, detail="Invalid authorization code.")
