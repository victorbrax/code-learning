from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast.db import get_session
from fast.models import User
from fast.schemas import (MessageSchema, UserList, UserPublicSchema, UserSchema)
from fast.security import get_current_user, hash_password

router = APIRouter(prefix='/users', tags=['users'])
T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema)
def create_user(session: T_Session, user: UserSchema):
    #     **user.model_dump() -- Não esqueça desse método nunca mais..

    # Verificar se não existe antes de criar...
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='O usuário já existe.')
        elif db_user.email == user.email:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='O e-mail já existe.')

    # Criar...
    db_user = User(username=user.username, email=user.email, password=hash_password(user.password))
    session.add(db_user)
    session.commit()
    session.refresh(db_user) # O Refresh é importante porque o UserPublicSchema precisa de um ID.
    return db_user

@router.get('/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users(session: T_Session, limit: int = 10, offset: int = 0):
    user = session.scalars(
        select(User).limit(limit).offset(offset)
    )
    return {'users': user}
    
@router.put('/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublicSchema)
def update_user(session: T_Session, user_id: int, user: UserSchema, current_user: T_CurrentUser):
    # db_user = session.scalar( -- Com a função "get_current_user", voce não precisa mais disso.
    #     select(User).where(User.id == user_id)
    # )
    # if not db_user: 
    #     raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='O usuário não existe.')

    if current_user.id != user_id:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail='Não autorizado, pow.')

    current_user.email = user.email
    current_user.username = user.username
    current_user.password = hash_password(user.password)

    session.commit()
    session.refresh(current_user)
    return current_user


@router.delete('/{user_id}', status_code=HTTPStatus.OK, response_model=MessageSchema)
def delete_user(user_id: int, session: T_Session, current_user: T_CurrentUser):
    # não faz sentido poder deletar apenas o próprio usuário, mas fica para fins de conhecimento o param user_id

    # db_user = session.scalar(  -- Com a função "get_current_user", voce não precisa mais disso.
    #     select(User).where(User.id == user_id)
    # )
    # if not db_user:
    #     raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='O usuário não existe.')
    
    if current_user.id != user_id:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail='Não autorizado, pow.')

    session.delete(current_user)
    session.commit()
    return {'message': 'Usuário deletado.'}