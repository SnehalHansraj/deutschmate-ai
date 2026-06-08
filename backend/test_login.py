from app.db.database import SessionLocal

from app.services.auth_service import (
    authenticate_user
)

db = SessionLocal()

user = authenticate_user(
    db,
    "maithili@example.com",
    "Deutsch123"
)

print(user)