from datetime import datetime

from sqlalchemy import (
    Column,
    Text,
    Boolean,
    String,
    Float,
    DateTime,
    Integer,
    ForeignKey
)

from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker
)

from sqlalchemy.engine import create_engine

from sqlalchemy.exc import IntegrityError

from app.utils.settings import DATABASE_URI


engine = create_engine(DATABASE_URI, echo=False)

Session = sessionmaker(bind=engine)

Base = declarative_base()


class OurBase(Base):

    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

    created_at = Column(DateTime, default=datetime.utcnow)


class User(OurBase):

    __tablename__ = 'users'

    keywords = {'user', 'users'}

    name = Column(String(100), nullable=False)

    email = Column(
        String(200),
        nullable=False,
        unique=True
    )

    password = Column(
        Text,
        nullable=False
    )

    # 0 is Sudo, 1 is admin, 2 in normal
    # 3 is guest (readonly)
    role = Column(
        Integer,
        nullable=False,
        default=2
    )


class ActivityLog(OurBase):

    __tablename__ = 'activity-logs'

    keywords = {'logs', 'activities', 'activity-logs'}

    user_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )

    activity = Column(
        Text,
        nullable=False
    )


class Product(OurBase):

    __tablename__ = 'products'

    keywords = {'products', 'product'}

    name = Column(
        String(200),
        nullable=False,
        unique=True
    )

    category = Column(String(100), nullable=False)

    cost = Column(
        Float,
        nullable=False,
        default=0
    )

    selling_price = Column(
        Float,
        nullable=False,
        default=0
    )

    stockflows = relationship(
        'StockFlow',
        backref='product'
    )


class Warehouse(OurBase):

    __tablename__ = 'warehouses'

    keywords = {'warehouses', 'warehouse'}

    name = Column(
        String(200),
        nullable=False,
        unique=True
    )

    location = Column(
        Text,
        nullable=False
    )

    stockflows = relationship(
        'StockFlow',
        backref='warehouse'
    )


class StockFlow(OurBase):

    __tablename__ = 'stockflows'

    keywords = {
        'stockflows',
        'arrivals',
        'spoilage',
        'sales',
        'movements',
        'stocks'
    }

    product_id = Column(
        Integer,
        ForeignKey('products.id'),
        nullable=False
    )

    warehouse_id = Column(
        Integer,
        ForeignKey('warehouses.id'),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=1
    )

    source = Column(
        Text,
        nullable=True
    )

    destination = Column(
        Text,
        nullable=True
    )

    # Sales, Arrival, Spoilage
    # or Movement
    flow_type = Column(
        Text,
        nullable=False
    )


Base.metadata.create_all(bind=engine)
