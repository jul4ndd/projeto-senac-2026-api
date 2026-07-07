from jwt import decode

from Viajei_api.security import CHAVE_SECRETA, create_access_token

def test_jwt():

    #GIVEN; DADO
    data = {'test': 'test'}
    token = create_access_token(data)

    #WHEN; QUANDO 
    

