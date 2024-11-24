from sqlite3 import IntegrityError

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from typing import Annotated
from slugify import slugify

from app.backend.db_depends import get_db
from app.models import User
from app.schemas import CreateUser, UpdateUser, UserResponse

router = APIRouter(tags=["user"]) # убрано: prefix="/user",

# Маршрут для получения всех пользователей
@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

# Маршрут для получения пользователя по ID
@router.get("/{user_id}")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user:
        return user
    raise HTTPException(status_code=404, detail="User was not found")

# Маршрут для создания нового пользователя
@router.post("/create", response_model=UserResponse)
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    try:        
        slug = user.username.lower().replace(" ", "-")

        new_user = User(
            username=user.username,
            firstname=user.firstname,
            lastname=user.lastname,
            age=user.age,
            slug=slug,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # Возвращает обновлённый объект из БД

        return new_user

    except IntegrityError as e:
        # Если нарушено уникальное ограничение (например, slug уже существует)
        print(f"Ошибка целостности: {e}")
        db.rollback()
        raise HTTPException(status_code=400, detail="Пользователь с таким slug уже существует.")

    except Exception as e:
        # Общий обработчик ошибок
        print(f"Неизвестная ошибка: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Произошла ошибка на сервере.")


# Маршрут для обновления данных пользователя
@router.put("/update/{user_id}")
async def update_user(
    user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]
):
    stmt = update(User).where(User.id == user_id).values(**user.dict(exclude_unset=True))
    result = db.execute(stmt)
    db.commit()
    if result.rowcount:
        return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}
    raise HTTPException(status_code=404, detail="User was not found")

# Маршрут для удаления пользователя
@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = delete(User).where(User.id == user_id)
    result = db.execute(stmt)
    db.commit()
    if result.rowcount:
        return {"status_code": status.HTTP_200_OK, "transaction": "User was deleted successfully!"}
    raise HTTPException(status_code=404, detail="User was not found")




# from fastapi import APIRouter
#
# router = APIRouter(prefix="/user", tags=["user"])
#
# @router.get("/")
# async def all_users():
#     pass
#
# @router.get("/user_id")
# async def user_by_id():
#     pass
#
# @router.post("/create")
# async def create_user():
#     pass
#
# @router.put("/update")
# async def update_user():
#     pass
#
# @router.delete("/delete")
# async def delete_user():
#     pass
#
#
#
# # @router.get("/{user_id}")
# # async def user_by_id(user_id: int):
# #     pass
