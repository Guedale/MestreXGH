# ORGINAL ABAIXO

#import csv, random
#
#random.seed(12)
#
#nomes = ["Ana Costa", "Bruno Sales", "Carla Dias", "Diego Matos",
#         "Elaine Reis", "Fábio Luz", "Gisele Prado", "Heitor Nunes"]
#
#ceps = ["11013001",   # Santos — existe
#        "11440003",   # Guarujá — existe
#        "11701000",   # Praia Grande — existe
#        "11310000",   # São Vicente — existe
#        "11075350",   # Santos — existe
#       "01311000",   # São Paulo — existe
#        "99999999",   # formato certo, mas NÃO existe
#        "123"]        # malformado
#
#random.shuffle(nomes)
#
#with open("clientes.csv", "w", newline="", encoding="utf-8") as f:
#    w = csv.writer(f)
#    w.writerow(["nome", "cep"])
#    for nome, cep in zip(nomes, ceps):
#        w.writerow([nome, cep])
#
#print("clientes.csv criado")
#print(open("clientes.csv", encoding="utf-8").read())

import csv, random

random.seed(12)

nomes = ["Ana Costa", "Bruno Sales", "Carla Dias", "Diego Matos",
         "Elaine Reis", "Fábio Luz", "Gisele Prado", "Heitor Nunes"]

ceps = ["11013001",   # Santos — existe
        "11440003",   # Guarujá — existe
        "11701000",   # Praia Grande — existe
        "11310000",   # São Vicente — existe
        "11075350",   # Santos — existe
        "01311000",   # São Paulo — existe
        "99999999",   # formato certo, mas NÃO existe
        "123"]        # malformado


random.shuffle(nomes)
clientes = list(zip(nomes, ceps))
random.shuffle(clientes)


with open("clientes.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["nome", "cep"])

    for nome, cep in clientes:
     w.writerow([nome, cep])


print("clientes.csv criado")
print(open("clientes.csv", encoding="utf-8").read())