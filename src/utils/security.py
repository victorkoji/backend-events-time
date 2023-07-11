import bcrypt
from jose import jwt


class Security():
    def __init__(self):
        self.secret_key = "chave_secreta"
        self.algorithm = "HS256"

    def verify_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password.encode())

    def verify_token(self, token):
        try:
            decode_token = jwt.decode(
                token,
                self.secret_key,
                algorithms=self.algorithm
            )

            return decode_token
        except jwt.JWTError:
            return False

    def create_token(self, data):
        return jwt.encode(data, self.secret_key, algorithm=self.algorithm)

    def create_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()
