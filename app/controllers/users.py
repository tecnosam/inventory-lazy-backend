from typing import (
    List,
    Type
)

from sqlalchemy.exc import (
    IntegrityError as DBIntegrityError
)

from app.models.orm import (
    Session,
    User,
)

from app.utils.exceptions import (
    AppException,
    EntityNotFoundException,
    EntityExistsException
)

from app.utils.security import (
    encode_data
)

from app.utils.settings import (
    ADMIN_USERNAME,
    ADMIN_PASSWORD
)


def login(
    email: str,
    password: str,
    sudo_mode: bool = False
):

    if sudo_mode:

        if ADMIN_USERNAME != email:

            raise EntityNotFoundException()

        if ADMIN_PASSWORD != password:

            raise AppException(
                msg="Invalid SUDO credentials",
                code=401
            )

        return {
            'token': encode_data({
                'role': 0,
                'id': 0
            }),
            'role': 0
        }

    with Session() as session:

        user = session.query(User).filter_by(
            email=email
        ).first()

        if user is None:

            raise EntityNotFoundException()

        return {
            'token': encode_data({
                'role': user.role,
                'id': user.id
            }),

            'role': user.role
        }


def get_user(user_id: int) -> User:

    with Session() as session:

        user = session.query(User).get(user_id)

        if not user:

            raise EntityNotFoundException()

        return user


def register_user(
    name: str,
    email: str,
    password: str,
    role: int = 1
):

    try:
        with Session() as session:

            user = User(
                name=name,
                email=email,
                password=password,
                role=role
            )

            session.add(user)
            session.commit()

            return True
    except DBIntegrityError as exc:

        raise EntityExistsException(
            msg="User with this E-mail exists"
        ) from exc


def update_user(user_id, updates):

    try:
        with Session() as session:

            update_count = session.query(User).filter_by(
                id=user_id
            ).update(updates)

            session.commit()

            if not update_count:

                raise EntityNotFoundException()

            return True
    except DBIntegrityError as exc:

        raise EntityExistsException(
            msg="User with this E-mail exists"
        ) from exc
