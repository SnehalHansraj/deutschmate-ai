from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.user import User
from app.api.dependencies import get_current_user

from app.schemas.vocabulary import (
    VocabularyCreate,
    VocabularyResponse
)

from app.services.vocabulary_service import (
    create_vocabulary,
    get_user_vocabulary,
    get_vocabulary_by_id,
    mark_word_mastered,
    delete_vocabulary
)

router = APIRouter(
    prefix="/api/vocabulary",
    tags=["Vocabulary"]
)


# ==========================================
# ADD VOCABULARY
# ==========================================

@router.post(
    "",
    response_model=VocabularyResponse
)
def add_vocabulary(
    vocabulary: VocabularyCreate,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    """
    Add new vocabulary word
    for current user.
    """

    return create_vocabulary(
        db=db,
        user_id=current_user.id,
        vocabulary=vocabulary
    )


# ==========================================
# GET ALL VOCABULARY
# ==========================================

@router.get(
    "",
    response_model=list[VocabularyResponse]
)
def get_all_vocabulary(
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    """
    Get all vocabulary words
    of current user.
    """

    return get_user_vocabulary(
        db=db,
        user_id=current_user.id
    )


# ==========================================
# GET ONE VOCABULARY WORD
# ==========================================

@router.get(
    "/{vocabulary_id}",
    response_model=VocabularyResponse
)
def get_vocabulary(
    vocabulary_id: int,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    """
    Get one vocabulary word.
    """

    vocabulary = get_vocabulary_by_id(
        db=db,
        vocabulary_id=vocabulary_id,
        user_id=current_user.id
    )

    if vocabulary is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vocabulary not found"
        )

    return vocabulary


# ==========================================
# MARK AS MASTERED
# ==========================================

@router.patch(
    "/{vocabulary_id}/master",
    response_model=VocabularyResponse
)
def master_vocabulary(
    vocabulary_id: int,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    """
    Mark vocabulary word
    as mastered.
    """

    vocabulary = get_vocabulary_by_id(
        db=db,
        vocabulary_id=vocabulary_id,
        user_id=current_user.id
    )

    if vocabulary is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vocabulary not found"
        )

    return mark_word_mastered(
        db=db,
        vocabulary_id=vocabulary_id,
        user_id=current_user.id
    )


# ==========================================
# DELETE VOCABULARY
# ==========================================

@router.delete(
    "/{vocabulary_id}"
)
def remove_vocabulary(
    vocabulary_id: int,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    """
    Delete vocabulary word.
    """

    vocabulary = get_vocabulary_by_id(
        db=db,
        vocabulary_id=vocabulary_id,
        user_id=current_user.id
    )

    if vocabulary is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vocabulary not found"
        )

    delete_vocabulary(
        db=db,
        vocabulary=vocabulary
    )

    return {
        "message": "Vocabulary deleted successfully"
    }