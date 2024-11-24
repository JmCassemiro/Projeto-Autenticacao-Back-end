import datetime
import jwt
from app import Config

class TokenManager:
    @staticmethod
    def generate_token(user_id):
        """Gera um token JWT para o usuário com um tempo de expiração de 1 hora."""
        payload = {
            "sub": user_id,
            "iat": datetime.datetime.now(datetime.UTC),
            "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1),
        }
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
        return token

    @staticmethod
    def verify_token(token):
        """Verifica a validade do token JWT."""
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
