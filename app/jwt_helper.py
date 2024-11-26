import datetime
from flask import jsonify, make_response, request
import jwt
from app import Config


class TokenManager:
    @staticmethod
    def generate_token(user_id):
        payload = {
            "sub": user_id,
            "iat": datetime.datetime.now(datetime.timezone.utc),
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=5),
        }
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")

        response = make_response(
            jsonify({"message": "Token gerado!"}), 200
        )

        response.set_cookie("access_token", token, httponly=True, secure=False, samesite="Lax")

        return response

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    from flask import request, redirect, url_for
