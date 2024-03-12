from typing import (
    List,
    Optional
)
from pydantic import (
    BaseModel,
    Field
)


class LoginForm(BaseModel):

    email: str
    password: str


class UserCreate(BaseModel):

    name: str
    email: str
    role: int = Field(default=1)


class CreateUser(UserCreate):

    password: str = Field(default="0000")


class UpdateProfile(BaseModel):

    name: str = Field(default=None)
    email: str = Field(default=None)
    password: str = Field(default=None)


class UserUpdate(BaseModel):

    name: str = Field(default=None)
    email: str = Field(default=None)


class ProductBase(BaseModel):
    name: str
    category: str
    cost: float = 0
    selling_price: float = 0


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class WarehouseBase(BaseModel):
    name: str
    location: str


class WarehouseCreate(WarehouseBase):
    pass

class WarehouseUpdate(WarehouseBase):
    pass


class StockFlowBase(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int = 1
    source: Optional[str] = None
    destination: Optional[str] = None

    flow_type: str


class StockFlowCreate(StockFlowBase):
    pass


class StockFlowUpdate(StockFlowBase):
    pass
