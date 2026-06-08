"""
Authentication Routes

Contains:
- Register User
- Login User
- Get Current User
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.models.user import User

from app.schemas.user import (
    UserCreate,
    UserResponse,
    Token
)

from app.core.jwt import create_access_token

from app.services.auth_service import (
    create_user,
    authenticate_user
)

from app.api.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


# ==========================================
# REGISTER
# ==========================================

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Create new user account.
    """

    created_user = create_user(
        db,
        user
    )

    if not created_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    return created_user


# ==========================================
# LOGIN
# ==========================================

@router.post(
    "/login",
    response_model=Token
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Login user.

    OAuth2 standard expects:

    username = email
    password = password

    Returns JWT token.
    """

    authenticated_user = authenticate_user(
        db,
        form_data.username,
        form_data.password
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


# ==========================================
# CURRENT USER
# ==========================================

@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(
        get_current_user
    )
):
    """
    Return currently logged-in user.

    Requires valid JWT token.
    """

    return current_user