import os
from datetime import datetime, timedelta
import bcrypt
from jose import jwt


class Security():
    def __init__(self):
        self.secret_key = os.getenv("AUTH_SECRET_KEY")
        self.algorithm = os.getenv("AUTH_SECRET_ALGORITHM")

    def verify_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password.encode())

    def get_and_decode_token(self, token):
        try:
            decode_token = jwt.decode(
                token,
                self.secret_key,
                algorithms=self.algorithm
            )

            return decode_token
        except jwt.JWTError:
            return False

    def create_token(self, data, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def create_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()
