from pydantic import BaseModel, EmailStr


class MessageSchema(BaseModel):
    message: str

class UserSchema(BaseModel):
    username:str
    email: EmailStr
    password: str

class UserPublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    # Não retorne a senha para o cliente (dããã)

class UserList(BaseModel):
    users: list[UserPublicSchema]

class TokenSchema(BaseModel):
    access_token: str
    token_type: str = 'Bearer'