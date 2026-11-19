import requests


# FUNÇÃO PARA CONSULTAR CEP

def consultar_cep():

    cep = input("Digite o CEP: ").strip() # Removendo espaços em branco no início e no final da string

    if len(cep) != 8 or not cep.isdigit():
        print("CEP mal informado. Digite exatamente 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try: # Tenta acessar o url e obter os dados do CEP, caso ocorra algum erro, ele será tratado nos blocos except abaixo
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()

        dados = resposta.json()

        if dados.get("erro"):
            print("CEP não encontrado.")

        else:
            print("\n--- ENDEREÇO ENCONTRADO ---")
            print(f"Rua: {dados.get('logradouro')}")
            print(f"Bairro: {dados.get('bairro')}")
            print(f"Cidade: {dados.get('localidade')}")
            print(f"UF: {dados.get('uf')}")

    except requests.exceptions.Timeout:
        print("O servidor demorou demais para responder.")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão! Verifique sua internet.")

    except requests.exceptions.HTTPError:
        print("O servidor retornou um erro HTTP.")

    except requests.exceptions.RequestException:
      print("Não foi possível realizar a consulta.")

    except ValueError:
      print("O servidor retornou uma resposta inválida.")


# FUNÇÃO PARA CONSULTAR DDD

def consultar_ddd():

    ddd = input("Digite o DDD que deseja consultar: ").strip()

    if len(ddd) != 2 or not ddd.isdigit():
        print("DDD inválido! Digite exatamente dois números.")
        return

    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()

        dados = resposta.json()

        print("\n--- INFORMAÇÕES DO DDD ---")
        print(f"Estado: {dados['state']}")

        print("\nCidades:")

        for cidade in dados["cities"]:
            print(f"- {cidade}")

    except requests.exceptions.Timeout:
        print("O servidor demorou demais para responder.")

    except requests.exceptions.HTTPError:

        if resposta.status_code == 404:
            print("DDD não encontrado!")
        else:
            print("O servidor retornou um erro HTTP.")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão! Verifique sua internet.")

    except ValueError:
        print("O servidor retornou uma resposta inválida.")

    except requests.exceptions.RequestException:
        print("Não foi possível realizar a consulta.")


# FUNÇÃO DO MENU PRINCIPAL

def menu():

    while True:

        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Consultar CEP")
        print("2 - Consultar DDD")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            consultar_cep()

        elif opcao == "2":
            consultar_ddd()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Escolha 1, 2 ou 0.")

# ==================================
# INICIAR O PROGRAMA
# ==================================

menu()