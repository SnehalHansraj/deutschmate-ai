from sqlalchemy.orm import Session
from app.models.learning_progress import LearningProgress

XP_PER_WORD = 10


def award_xp(db: Session, user_id: int, xp: int = XP_PER_WORD):
    progress = (
        db.query(LearningProgress)
        .filter(LearningProgress.user_id == user_id)
        .first()
    )

    if not progress:
        return None

    progress.xp_points += xp

    db.commit()
    db.refresh(progress)

    return progress