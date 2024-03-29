from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.middleware import AppExceptionHandler

from app.routers import (
    auth,
    records
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.add_middleware(AppExceptionHandler)

app.include_router(auth.router)
app.include_router(records.router)
