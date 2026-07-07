from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from http import HTTPStatus
from jwt import encode, decode
from pwdlib import Passwordhash
from fastapi import depends, HTTPException
from fastapi .security import oAuth2PasswordBearer
from sqlalchemy import select 
from sqlachemy.orm import Session 

from Viajei_api.database import get_session
from Viajei_api.models import User 

CHAVE_SECRETA = "your-very-secret-and-exclusive-key"
ALGORITMO = "HS256"
TOKEN_ACESSO_MINUTOS_EXPIRAR = 30

contexto_senha = PasswordHash.recommended()
oauth2_scheme = oAuth2PasswordBearer(tokenUrl="/auth") 


def create_token(dados: dict):
    para_codificar = dados.copy()
    # BR = UTC-03
    expira = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
        minutes=TOKEN_ACESSO_MINUTOS_EXPIRAR
    )

    para_codificar.update({"exp": expira})
    jwt_codificado = encode(para_codificar, CHAVE_SECRETA, algorithm=ALGORITMO)

    return jwt_codificado


def get_password_hash(password: str):
    return contexto_senha.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return contexto_senha.verify(plain_password, hashed_password)

def get_current_user(
        token: str = Depends(oauth2_scheme), 
        session: Session = Depends(get_session)
):
        try:
            payload = decode(token, CHAVE_SECRETA, algorithms=[ALGORITMO])
            email: str = payload.get("sub")
            if email is None:
                raise HTTPException(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    detail="Could not validate credentials",
                    headers={"www-Authenticate": "Bearer"},
                )
        except AttributeError:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="Could not validate credentials", 
                headers={"www-Authenticate": "Bearer"},
        )
    
        user = session.scalar(select(User).where(User.email == email))

        if user is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="User credentials are invalid",
            )
        
        return user 
        

