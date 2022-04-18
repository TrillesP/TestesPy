import pytest
import csv

import requests
from requests import HTTPError

teste_dados_usuario = [
    (1, 'George', 'Bluth', 'george.bluth@reqres.in'),
    (2, 'Janet', 'Weaver', 'janet.weaver@reqres.in')
]


@pytest.mark.parametrize('id,nome,sobrenome,email', teste_dados_usuario)
def testar_dados_usuarios(id, nome, sobrenome, email):
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']

        print('id: %i \nnome: %s\nsobrenome: %s\nemail: %s' % (id_obtido, nome_obtido, sobrenome_obtido, email_obtido))

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email

    except HTTPError as http_fail:
        print(f'Um erro de http aconteceu: {http_fail}')
    except Exception as fail:
        print(f'Falha inesperada: {fail}')

def leitor_csv():
    teste_dados_csv = []
    nome_arquivo = 'usuarios.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile:
            dados = csv.reader(csvfile, delimiter=',')
            next(dados)
            for linha in dados:
                teste_dados_csv.append(linha)
        return teste_dados_csv
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    except Exception as fail:
        print('Erro não esperado.')

@pytest.mark.parametrize('id,nome,sobrenome,email', leitor_csv())
def testar_dados_usuarios(id, nome, sobrenome, email):
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = str(jsonResponse['data']['id'])
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']

        print('id: %s \nnome: %s\nsobrenome: %s\nemail: %s' % (id_obtido, nome_obtido, sobrenome_obtido, email_obtido))

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email

    except HTTPError as http_fail:
        print(f'Um erro de http aconteceu: {http_fail}')
    except Exception as fail:
        print(f'Falha inesperada: {fail}')