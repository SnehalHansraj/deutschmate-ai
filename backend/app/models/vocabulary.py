from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from sqlalchemy.sql import func

from app.db.base import Base


class Vocabulary(Base):
    __tablename__ = "vocabulary"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    german_word = Column(
        String,
        nullable=False
    )

    english_meaning = Column(
        String,
        nullable=False
    )

    example_sentence = Column(
        String,
        nullable=True
    )

    difficulty = Column(
        String,
        default="A1"
    )

    mastered = Column(
        Boolean,
        default=False
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
            f"Vocabulary("
            f"id={self.id}, "
            f"word='{self.german_word}', "
            f"user_id={self.user_id}"
            f")"
        )