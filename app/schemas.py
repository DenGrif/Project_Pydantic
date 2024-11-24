from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UserResponse(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str

    class Config:
        from_attributes = True  # Вместо orm_mode

class UpdateUser(BaseModel):
    firstname: str | None = None
    lastname: str | None = None
    age: int | None = None


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
