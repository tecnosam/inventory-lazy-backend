from fastapi import APIRouter, HTTPException
from typing import Union


from app.models.responses import (
    BaseResponse,
    ProductResponse,
    WarehouseResponse,
    ActivityLogResponse,
    UserResponse,

    ProductListResponse,
    WarehouseListResponse,
    ActivityLogListResponse,
    UserListResponse,
    StockFlowListResponse
)

from app.models.forms import (
    UserCreate,
    ProductCreate,
    WarehouseCreate,
    StockFlowCreate,

    ProductUpdate,
    WarehouseUpdate,
    UserUpdate,
    StockFlowUpdate
)

from app.controllers.switch import (
    get_records,
    get_record,
    edit_record,
    add_record,
    delete_record
)

router = APIRouter(prefix='/api', tags=['Records Management'])

# Import your Pydantic models for entities (Product, Warehouse, ActivityLog, User) and responses here

@router.get(
    "/{record_type}",
    response_model=Union[
        ProductListResponse,
        WarehouseListResponse,
        ActivityLogListResponse,
        UserListResponse,
        StockFlowListResponse
    ]
)
async def get_records_route(record_type: str):

    records = get_records(record_type)
    # Add more cases for other record types (ActivityLog, User, etc.)

    return BaseResponse.cook(data=records)


@router.get(
    "/{record_type}/{record_id}",
    response_model=Union[
        ProductResponse,
        WarehouseResponse,
        ActivityLogResponse,
        UserResponse
    ]
)
async def get_record_route(record_type: str, record_id: int):

    record = get_record(record_type, record_id)

    return BaseResponse.cook(data=record)


@router.post("/{record_type}", response_model=BaseResponse)
async def add_record_route(
    record_type: str,
    record_data: Union[
        ProductCreate,
        WarehouseCreate,
        UserCreate,
        StockFlowCreate
    ]
):

    data = record_data.model_dump()

    add_record(record_type, data)
    # Implement logic to add a new record based on record_type and record_data
    # Replace the following line with actual logic

    return BaseResponse.cook()


@router.put("/{record_type}/{record_id}", response_model=BaseResponse)
async def edit_record_route(
    record_type: str,
    record_id: int,
    record_data: Union[
        ProductUpdate,
        WarehouseUpdate,
        UserUpdate,
        StockFlowUpdate
    ]
):
    # Implement logic to edit an existing record based on record_type, record_id, and record_data
    # Replace the following line with actual logic

    data = record_data.model_dump(
        exclude_none=True,
        exclude_unset=True
    )

    edit_record(record_type, record_id, data)
    return BaseResponse.cook()


@router.delete("/{record_type}/{record_id}", response_model=BaseResponse)
async def delete_record_route(record_type: str, record_id: int):
    # Implement logic to delete a record based on record_type and record_id
    # Replace the following line with actual logic

    delete_record(record_type, record_id)
    return BaseResponse.cook()
