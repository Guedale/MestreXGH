#import requests
## 11432390
#cep = input("Digite o CEP: ")
#url = f"https://viacep.com.br/ws/{cep}/json/"

#resposta = requests.get(url)
#dados = resposta.json()

#print(dados["logradouro"])
#print(dados["bairro"])
#print(dados["localidade"])
#print(dados["uf"])



import requests 

cep = input("Digite o CEP: ").strip() # receber o cep do usuário e remover espaços em branco
if len(cep) != 8 or not cep.isdigit(): # verificar se o cep tem 8 dígitos e é composto apenas por números
    print("CEP malinformado. Digite exatamente 8 numeros.")

else:
    url = f"https://viacep.com.br/ws/{cep}/json/" # criar a url para a requisição   

    try:
        resposta = requests.get(url) # fazer a requisição

        resposta.raise_for_status() # verificar erros no HTTP

        dados = resposta.json() # converter JSON para dicionario

        if dados.get("erro"): # verificar se o CEP existe
            print("CEP não encontrado.")

        else:
         print("/n-- ENDEREÇO ENCONTRADO --")
         print(f"rua: {dados.get('logradouro')}")
         print(f"bairro: {dados.get('bairro')}")
         print(f"cidade: {dados.get('localidade')}")
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