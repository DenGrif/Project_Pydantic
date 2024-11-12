from backend.db import engine, Base
from models import User, Task

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы.")
