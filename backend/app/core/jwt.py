"""
JWT Token Utilities

Purpose:
- Create JWT access tokens
- Verify JWT access tokens

Used during:
- Login
- Protected routes
- User authentication
"""

from datetime import datetime, timedelta, timezone

from jose import jwt

from app.core.config import settings


def create_access_token(data: dict) -> str:
    """
    Create JWT access token.

    Example:
    {
        "sub": "1"
    }

    sub = user id
    """

    # Copy incoming data
    to_encode = data.copy()

    # Token expiry time
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Add expiry inside payload
    to_encode.update(
        {
            "exp": expire
        }
    )

    # Generate JWT token
    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return encoded_jwt