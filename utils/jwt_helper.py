import jwt
import datetime
from app import Config


def generate_token(user_id):
    """
    Gera um token JWT para o usuário autenticado.
    """
    payload = {
        'sub': user_id,  # sub é o ID do usuário
        'iat': datetime.datetime.utcnow(),  # data de criação
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # expiração do token (1 hora)
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    return token


def verify_token(token):
    """
    Verifica a validade de um token JWT.
    """
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido
