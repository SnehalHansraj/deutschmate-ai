from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate 
from app.core.security import (
    hash_password,
    verify_password
)
from app.services.progress_service import (
    create_learning_progress
)

def create_user(
    db: Session,
    user: UserCreate
):
    existing_user = (
        db.query(User)
        .filter(
            (User.email == user.email)
            | (User.username == user.username)
        )
        .first()
    )

    if existing_user:
        return None

    try:

        # Create User

        new_user = User(
            email=user.email,
            username=user.username,
            hashed_password=hash_password(
                user.password
            )
        )

        db.add(new_user)

        # User ID generate karne ke liye
        db.flush()

        # Create Learning Progress

        create_learning_progress(
            db=db,
            user_id=new_user.id
        )

        db.commit()

        db.refresh(new_user)

        return new_user

    except Exception:

        db.rollback()

        raise


def authenticate_user(
        db: Session,
        email: str,
        password: str
):
    """
    Authenticate a user by email and password.
    """
    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )
    print("USER FOUND:", user)
    print("INPUT PASSWORD:", password)

    if not user:
        return None
    
    print(
        "PASSWORD MATCH:",
        verify_password(
            password,
            user.hashed_password
        )
    )
    
    if not verify_password(
        password,
        user.hashed_password
    ):
        return None
    
    return user

    