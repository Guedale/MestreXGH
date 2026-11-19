
import requests

# Receber DDD
ddd = input("Digite o DDD que deseja consultar: ").strip()

# Verificar se o DDD possui dois números
if len(ddd) != 2 or not ddd.isdigit():

    print("DDD inválido! Digite exatamente dois números.")

else:

    # Criar endereço da API
    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"

    try:

        # Fazer requisição
        resposta = requests.get(url, timeout=5)

        # Verificar erros HTTP
        resposta.raise_for_status()

        # Converter resposta para dicionário
        dados = resposta.json()

        # Mostrar informações
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
