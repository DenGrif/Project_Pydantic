from sqlalchemy.orm import Session
from .db import SessionLocal

# Генератор для работы с сессией БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
