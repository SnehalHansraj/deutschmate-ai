from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
    Token
)

from app.core.jwt import create_access_token

from app.services.auth_service import (
    create_user,
    authenticate_user
)

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

@router.post(
    "/login",
    response_model=Token
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    """
    Authenticate user and return JWT token.
    """

    authenticated_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not authenticated_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {
            "sub": str(authenticated_user.id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }