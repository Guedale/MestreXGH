import qrcode

link = input("Digite o link para gerar o QR code: ") # Solicita ao usuário que insira um link
nome = input("Digite o nome do arquivo: ") # Solicita ao usuário que insira o nome do arquivo

imagem = qrcode.make(link) # Gera o QR code para o link fornecido pelo usuário
imagem.save(nome + ".png") # Salva a imagem do QR code com o nome fornecido pelo usuário

print("QR code criado com sucesso!") # Informa ao usuário que o QR code foi criado com sucesso

imagem.show() # Exibe a imagem do QR code gerado

