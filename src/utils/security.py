from datetime import datetime, timedelta
import bcrypt
from jose import jwt


class Security():
    def __init__(self):
        pass

    def verify_password(self, password: str, hashed_password: str):
        return bcrypt.checkpw(password.encode(), hashed_password.encode())

    def get_decode_token(self, token, secret_key: str, algorithms: str):
        try:
            decode_token = jwt.decode(
                token,
                secret_key,
                algorithms
            )

            return decode_token
        except jwt.JWTError:
            return False

    def create_token(self, data: dict, secret_key: str, algorithm: str, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, secret_key, algorithm)

    def create_password(self, password: str):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()
