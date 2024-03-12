from typing import (
    List,
    Type
)

from sqlalchemy.exc import (
    IntegrityError as DBIntegrityError
)

from app.models.orm import (
    Session,

    OurBase,
    User,
    ActivityLog,
    Product,
    Warehouse,
    StockFlow
)

from app.utils.exceptions import (
    EntityNotFoundException,
    EntityExistsException
)


models = [
    User,
    ActivityLog,
    Product,
    Warehouse,
    StockFlow
]


def _get_model(record_type: str) -> Type[OurBase] | None:

    for Model in models:

        if record_type in Model.keywords:

            return Model

    raise EntityNotFoundException(
        msg="The resource requested for doesn't exist"
    )


def get_records(
    record_type: str,
    filters: dict = None,
    offset: int = 0,
    limit: int = 15
) -> List[OurBase]:

    with Session() as session:

        filters = {} if filters is None else filters

        return session.query(
            _get_model(record_type)
        ).filter_by(**filters).offset(offset).limit(limit)


def get_record(
    record_type: str,
    record_id: int
) -> OurBase:

    with Session() as session:

        Model = _get_model(record_type)

        instance = session.query(Model).get(record_id)

        return instance


def add_record(
    record_type: str,
    data: dict
) -> bool:

    try:
        with Session() as session:

            Model = _get_model(record_type)

            instance = Model(**data)

            session.add(instance)
            session.commit()

            return True
    except DBIntegrityError as e:

        raise EntityExistsException() from e


def edit_record(
    record_type: str,
    record_id: int,
    updates: dict
) -> bool:

    try:
        with Session() as session:

            Model = _get_model(record_type)
            
            update_count = session.query(Model).filter_by(
                id=record_id
            ).update(updates)

            session.commit()

            if not update_count:

                raise EntityNotFoundException()

            return True
    except DBIntegrityError as e:

        raise EntityExistsException() from e


def delete_record(
    record_type: str,
    record_id: int
) -> bool:

    with Session() as session:

        Model = _get_model(record_type)

        delete_count = session.query(Model).filter_by(
            id=record_id
        ).delete()

        session.commit()

        if not delete_count:

            raise EntityNotFoundException()

        return delete_count > 0
