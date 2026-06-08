"""
Reusable FastAPI dependencies.

Purpose:
- Get current authenticated user
- Protect private routes
"""

from fastapi import (
    Depends,
    HTTPException,
    status
)

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.models.user import User

from app.core.jwt import verify_access_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """
    Get authenticated user from JWT token.

    Flow:

    Request
        ↓
    Extract Token
        ↓
    Verify Token
        ↓
    Extract User ID
        ↓
    Fetch User From DB
        ↓
    Return User
    """

    payload = verify_access_token(token)

    print("TOKEN RECEIVED:")
    print(token)

    print("PAYLOAD:")
    print(payload)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )

    user = (
        db.query(User)
        .filter(User.id == int(user_id))
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user