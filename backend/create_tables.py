"""
Create all database tables.

Run:
python create_tables.py
"""

from app.db.base import Base
from app.db.database import engine

# Import all models
from app.models.user import User
from app.models.learning_progress import LearningProgress
from app.models.vocabulary import Vocabulary

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")