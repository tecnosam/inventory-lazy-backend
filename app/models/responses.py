from typing import List, Optional, Any

from pydantic import BaseModel

from app.models.representations import (
    User,
    Product,
    Warehouse,
    StockFlow,
    ActivityLog
)


class BaseResponse(BaseModel):
    status: bool
    message: str
    data: Optional[None | list | dict | Any]

    @classmethod
    def cook(
        cls,
        status: bool = True,
        message: str = "Request complete!",
        data: Optional[None | list | dict] = None
    ):
        return cls(status=status, message=message, data=data).dict()


class AuthResponse(BaseResponse):

    class Auth(BaseModel):

        token: str
        role: int

    data: Auth


class ProductResponse(BaseResponse):
    data: Optional[Product]


class ProductListResponse(BaseResponse):
    data: Optional[List[Product]]


class WarehouseResponse(BaseResponse):
    data: Optional[Warehouse]


class WarehouseListResponse(BaseResponse):
    data: Optional[List[Warehouse]]


class StockFlowResponse(BaseResponse):
    data: Optional[StockFlow]


class StockFlowListResponse(BaseResponse):
    data: Optional[List[StockFlow]]


class ActivityLogResponse(BaseResponse):
    data: Optional[ActivityLog]


class ActivityLogListResponse(BaseResponse):
    data: Optional[List[ActivityLog]]


class UserResponse(BaseResponse):
    data: Optional[User]


class UserListResponse(BaseResponse):
    data: Optional[List[User]]
