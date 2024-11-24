from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from typing import List
from slugify import slugify

from app.backend.db_depends import get_db
from app.models.user import User
from app.schemas import CreateUser, UpdateUser

router = APIRouter()

# Получить всех пользователей
@router.get("/", response_model=List[CreateUser])
def all_users(db: Session = Depends(get_db)):
    users = db.scalars(select(User)).all()
    return users

# Получить пользователя по ID
@router.get("/{user_id}")
def user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user

# Создать нового пользователя
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    slugified_username = slugify(user.username)
    new_user = User(username=slugified_username, **user.dict())
    db.add(new_user)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}

# Обновить данные пользователя
@router.put("/update/{user_id}")
def update_user(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    stmt = update(User).where(User.id == user_id).values(**user.dict())
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}

# Удалить пользователя
@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    stmt = delete(User).where(User.id == user_id)
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User deleted successfully!"}



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