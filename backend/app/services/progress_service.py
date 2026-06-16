from sqlalchemy.orm import Session

from app.models.learning_progress import (
    LearningProgress
)


def create_learning_progress(
    db: Session,
    user_id: int
):
    """
    Create default learning progress
    for a newly registered user.

    IMPORTANT:
    No commit here.

    Parent service controls transaction.
    """

    progress = LearningProgress(
        user_id=user_id
    )

    db.add(progress)

    return progress


def get_learning_progress(
    db: Session,
    user_id: int
):
    """
    Get learning progress
    for a user.
    """

    return (
        db.query(LearningProgress)
        .filter(
            LearningProgress.user_id == user_id
        )
        .first()
    )