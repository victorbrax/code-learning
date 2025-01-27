from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast.db import get_session
from fast.models import User
from fast.schemas import TokenSchema
from fast.security import create_acess_token, verify_password

app = FastAPI()

from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['auth'])
T_Session = Annotated[Session, Depends(get_session)]


# oauth2_scheme aponta pra cá
@router.post('/token/', response_model=TokenSchema)
def login_for_access_token(session: T_Session, form_data: OAuth2PasswordRequestForm = Depends()): # podia criar um T_Annotated pra esse, mas nao quis
    user = session.scalar(
        select(User).where(User.email == form_data.username)
    )

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Usuário ou senha incorretos.')

    access_token = create_acess_token(data_claims={'sub': user.email})
    return {'access_token': access_token}

