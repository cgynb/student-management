import jwt
import time


def create_token(user_id, role):
    headers = {
        "alg": "HS256",
        "typ": "JWT",
    }
    exp = int(time.time() + 60000)
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": exp,
        "iss": 'hhh'
    }
    key = "key"

    token = jwt.encode(payload=payload, key=key, algorithm='HS256', headers=headers)
    return token


def validate_token(token):
    payload = {}
    key = "key"
    msg = None
    try:
        payload = jwt.decode(jwt=token, key=key, algorithms=['HS256'], issuer='hhh')
    except jwt.DecodeError:
        msg = 'token认证失败'
    except jwt.InvalidTokenError:
        msg = '非法的token'
    except Exception:
        msg = "something wrong"
    return payload.get("user_id"), payload.get("role"), msg


if __name__ == "__main__":
    t = create_token(1, "student")
    print(validate_token(t))
