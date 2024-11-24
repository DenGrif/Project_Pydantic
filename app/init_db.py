from backend.db import Base, engine
from models.user import User

# Создание таблиц в базе данных
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()


# from sqlalchemy import create_engine
# from sqlalchemy.schema import CreateTable
# from backend.db import Base, engine
# from models.task import Task
# from models.user import User
#
#
# Base.metadata.create_all(bind=engine)
#
# # Генерация SQL-запроса для таблиц
# print(CreateTable(Task.__table__).compile(engine))
# print(CreateTable(User.__table__).compile(engine))
#
# from backend.db import engine, Base
# from models import User, Task
#
# if __name__ == "__main__":
#     Base.metadata.create_all(bind=engine)
#     print("Таблицы успешно созданы.")
