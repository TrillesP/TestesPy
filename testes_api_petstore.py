import pytest
import requests

url = 'https://petstore.swagger.io/v2/user'
def testar_incluir_usuario():
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '12181'

    headers = {'Content-Type': 'application/json'}
    resposta = requests.post(url,
                             data=open('json/usuario1.json', 'rb'),
                             headers=headers)
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_consultar_usuario():
    status_code_esperado = 200
    id_esperado = 12181
    username_esperado = 'correia'
    email_esperado = 'test@iterasys.com.br'
    phone_esperado = '11999992181'
    user_status_esperado = 0

    username = 'correia'
    headers = {'Content-Type': 'application/json'}
    resposta = requests.get("%s/%s" % (url, username), headers=headers)
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == phone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado