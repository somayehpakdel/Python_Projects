# app/api/errors.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.exceptions import (
    ResourceNotFoundError, 
    AlreadyExistsError, 
    InvalidCredentialsError
)

def setup_exception_handlers(app: FastAPI):
    
    # 1. Not Found -> 404
    @app.exception_handler(ResourceNotFoundError)
    async def not_found_handler(request: Request, exc: ResourceNotFoundError):
        return JSONResponse(
            status_code=404,
            content={
                "success": False, 
                "error": {
                    "code": "NOT_FOUND", 
                    "message": exc.message
                }
            }
        )

    # 2. Already Exists -> 409 Conflict (This is better than 400 for duplicates)
    @app.exception_handler(AlreadyExistsError)
    async def already_exists_handler(request: Request, exc: AlreadyExistsError):
        return JSONResponse(
            status_code=409, 
            content={
                "success": False, 
                "error": {
                    "code": "ALREADY_EXISTS", 
                    "message": exc.message
                }
            }
        )

    # 3. Invalid Creds -> 401 Unauthorized
    @app.exception_handler(InvalidCredentialsError)
    async def invalid_creds_handler(request: Request, exc: InvalidCredentialsError):
        return JSONResponse(
            status_code=401,
            content={
                "success": False, 
                "error": {
                    "code": "INVALID_CREDENTIALS", 
                    "message": exc.message
                }
            }
        )