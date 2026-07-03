from pydantic import BaseModel, ConfigDict, EmailStr


class UserSchemas(BaseModel):
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserDB(UserSchemas):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]