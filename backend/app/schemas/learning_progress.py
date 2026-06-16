from pydantic import BaseModel


class LearningProgressResponse(BaseModel):
    id: int

    user_id: int

    current_level: str

    xp_points: int

    streak_days: int

    lessons_completed: int

    model_config = {
        "from_attributes": True
    }