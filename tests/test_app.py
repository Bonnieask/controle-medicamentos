import requests

def test_api_viacep():
    cep = "01001000"

    resposta = requests.get(
        f"https://viacep.com.br/ws/{cep}/json/"
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["localidade"] == "São Paulo"