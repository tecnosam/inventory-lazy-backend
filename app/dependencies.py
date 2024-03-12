
from app.utils.security import decode_token

from fastapi import (
    Depends,
    Header,
    HTTPException
)


def raise_auth_exception():

    raise HTTPException(
        status_code=403,
        detail="Invalid Token!"
    )


def get_user_data(token: str = Header()):

    try:
        return decode_token(token)
    except Exception:
        raise_auth_exception()


def get_user_id(user_data: dict = Depends(get_user_data)):

    return user_data['id']


def get_admin_id(user_data: dict = Depends(get_user_data)):

    if user_data.get('role') != 1:
        raise_auth_exception()

    return 0


def get_sudo_id(user_data: dict = Depends(get_user_data)):

    if user_data.get('role') != 0:
        raise_auth_exception()

    return user_data.get('id')

