from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jwt import encode 

SECRET_KEY = 'your-very-secre-and-exclusive-key'
ALGORITIMO = 'hs256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
contexto_senha = PassawordHash.recommend

def creat_token(dados: dict):
    para_codificar = dados.copy()
    # BR = UTC-03
    expira = datetime.now(
        tz=ZoneInfo('UTC')
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    para_codificar.update({'exp': expira})
    jwt_codificado = encode(para_codificar,
    CHAVE_SECRETA,
    algorithm=ALGORITIMO
    )

    return jwt_codificado

