
import json
import os
import requests

ARQUIVO = "data.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def adicionar_medicamento(nome, horario):
    if not nome or not horario:
        raise ValueError("Dados inválidos")

    dados = carregar_dados()

    dados.append({
        "nome": nome,
        "horario": horario,
        "tomado": False
    })

    salvar_dados(dados)

def listar_medicamentos():
    return carregar_dados()

def marcar_como_tomado(indice):
    dados = carregar_dados()

    if indice < 0 or indice >= len(dados):
        raise IndexError("Índice inválido")

    dados[indice]["tomado"] = True

    salvar_dados(dados)

def buscar_endereco():
    cep = input("Digite o CEP: ")

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        print("\nEndereço encontrado:")
        print(f"Rua: {dados.get('logradouro')}")
        print(f"Bairro: {dados.get('bairro')}")
        print(f"Cidade: {dados.get('localidade')}")
        print(f"Estado: {dados.get('uf')}")
    else:
        print("Erro ao buscar CEP.")

def menu():
    while True:
        print("\n--- Controle de Medicamentos ---")
        print("1. Adicionar medicamento")
        print("2. Listar medicamentos")
        print("3. Marcar como tomado")
        print("4. Buscar endereço por CEP")
        print("5. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            horario = input("Horário: ")

            adicionar_medicamento(nome, horario)

        elif opcao == "2":
            meds = listar_medicamentos()

            for i, m in enumerate(meds):
                status = "✔" if m["tomado"] else "✘"

                print(f"{i} - {m['nome']} ({m['horario']}) [{status}]")

        elif opcao == "3":
            indice = int(input("Índice: "))

            marcar_como_tomado(indice)

        elif opcao == "4":
            buscar_endereco()

        elif opcao == "5":
            break

if __name__ == "__main__":
    menu()