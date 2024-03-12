from typing import (
    List,
    Optional
)
from datetime import datetime

from pydantic import BaseModel


class OurBase(BaseModel):

    id: int
    created_at: datetime


class Product(OurBase):

    name: str
    category: str
    cost: float
    selling_price: float


class Warehouse(OurBase):

    name: str
    location: str


class StockFlow(OurBase):

    product: Product
    warehouse: Warehouse

    product_id: int
    warehouse_id: int
    quantity: int

    source: Optional[str]
    destination: Optional[str]
    flow_type: str


class User(OurBase):

    name: str
    email: str
    role: int


class ActivityLog(OurBase):

    user: User
    activity: str
