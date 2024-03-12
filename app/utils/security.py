from hashlib import sha256

from jwt import (
    encode as jwt_encode,
    decode as jwt_decode
)

from app.utils.settings import (
    JWT_SECRET,
    JWT_ALGOL
)



def hash_string(string: str):

    digest = sha256(string.encode()).hexdigest()

    if isinstance(digest, bytes):
        return digest.decode()

    return digest


def encode_data(data: dict | list):

    return jwt_encode(data, JWT_SECRET, JWT_ALGOL)


def decode_token(token: str | bytes):

    return jwt_decode(token, JWT_SECRET, [JWT_ALGOL])

