from pydantic import BaseModel


class VocabularyCreate(BaseModel):
    german_word: str
    english_meaning: str
    example_sentence: str | None = None
    difficulty: str = "A1"


class VocabularyResponse(BaseModel):
    id: int
    user_id: int
    german_word: str
    english_meaning: str
    example_sentence: str | None = None
    difficulty: str
    mastered: bool

    model_config = {
        "from_attributes": True
    }


class VocabularyUpdate(BaseModel):
    mastered: bool