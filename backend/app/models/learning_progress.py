from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy import DateTime

from sqlalchemy.sql import func

from app.db.base import Base


class LearningProgress(Base):
    __tablename__ = "learning_progress"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    current_level = Column(
        String,
        default="A1",
        nullable=False
    )

    xp_points = Column(
        Integer,
        default=0,
        nullable=False
    )

    streak_days = Column(
        Integer,
        default=0,
        nullable=False
    )

    lessons_completed = Column(
        Integer,
        default=0,
        nullable=False
    )

    last_activity_date = Column(
        Date,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )

    def __repr__(self):
        return (
            f"LearningProgress("
            f"user_id={self.user_id}, "
            f"level='{self.current_level}', "
            f"xp={self.xp_points}"
            f")"
        )