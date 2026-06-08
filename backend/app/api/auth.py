from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.services.auth_service import(
    create_user
)

router =APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    response_model=UserResponse
)

def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    created_user = create_user(
        db,
        user
    )

    if not created_user:
        raise HTTPException(
            status_code = 400,
            detail = "User already exists"
        )
    
    return created_user