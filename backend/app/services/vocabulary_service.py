from sqlalchemy.orm import Session
from app.services.xp_service import award_xp

from app.models.vocabulary import Vocabulary
from app.schemas.vocabulary import (
    VocabularyCreate
)


def create_vocabulary(
    db: Session,
    user_id: int,
    vocabulary: VocabularyCreate
):
    """
    Create a new vocabulary word
    for a user.
    """

    new_word = Vocabulary(
        user_id=user_id,
        german_word=vocabulary.german_word,
        english_meaning=vocabulary.english_meaning,
        example_sentence=vocabulary.example_sentence,
        difficulty=vocabulary.difficulty
    )

    db.add(new_word)
    db.commit()
    db.refresh(new_word)

    return new_word


def get_user_vocabulary(
    db: Session,
    user_id: int
):
    """
    Get all vocabulary words
    of a user.
    """

    return (
        db.query(Vocabulary)
        .filter(
            Vocabulary.user_id == user_id
        )
        .all()
    )


def get_vocabulary_by_id(
    db: Session,
    vocabulary_id: int,
    user_id: int
):
    """
    Get one vocabulary word
    belonging to a user.
    """

    return (
        db.query(Vocabulary)
        .filter(
            Vocabulary.id == vocabulary_id,
            Vocabulary.user_id == user_id
        )
        .first()
    )


def mark_word_mastered(db: Session, vocabulary_id: int, user_id: int):
    vocabulary = (
        db.query(Vocabulary)
        .filter(
            Vocabulary.id == vocabulary_id,
            Vocabulary.user_id == user_id
        )
        .first()
    )

    if not vocabulary:
        return None

    # Prevent duplicate XP
    if vocabulary.mastered:
        return vocabulary

    vocabulary.mastered = True

    db.commit()
    db.refresh(vocabulary)

    # Award 10 XP
    award_xp(db, user_id)

    return vocabulary


def delete_vocabulary(
    db: Session,
    vocabulary: Vocabulary
):
    """
    Delete vocabulary word.
    """

    db.delete(vocabulary)
    db.commit()