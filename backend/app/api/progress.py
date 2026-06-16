from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.models.user import User

from app.api.dependencies import (
    get_current_user
)

from app.services.progress_service import (
    get_learning_progress
)

from app.schemas.learning_progress import (
    LearningProgressResponse
)

router = APIRouter(
    prefix="/api/progress",
    tags=["Learning Progress"]
)


@router.get(
    "/me",
    response_model=LearningProgressResponse
)
def get_my_progress(
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    """
    Return current user's learning progress.
    """

    progress = get_learning_progress(
        db=db,
        user_id=current_user.id
    )

    if progress is None:
        raise HTTPException(
            status_code=404,
            detail="Learning progress not found"
        )

    return progress