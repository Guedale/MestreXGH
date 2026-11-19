
import pygame

# Inicializa o Pygame
pygame.init()

# Cria a janela do jogo
janela = pygame.display.set_mode((1280, 720))

# Define o título
pygame.display.set_caption("Alguma bomba ai HAHAHEAHEASHEASHJEAHEAHEASHEAHSE")

# Define algumas cores (RGB)
branco = (255, 255, 255)
azul = (0, 100, 255)
vermelho = (255, 127, 127)

# Cria o personagem
personagem = pygame.Rect(375, 275, 50, 50)

# Velocidade do personagem
velocidade = 10

# Controla o jogo
rodando = True

# Relógio para controlar FPS
relogio = pygame.time.Clock()

# Loop principal
while rodando:

    # Verifica eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Verifica teclas pressionadas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        personagem.x += velocidade

    if teclas[pygame.K_LEFT]:
        personagem.x -= velocidade

    if teclas[pygame.K_UP]:
        personagem.y -= velocidade

    if teclas[pygame.K_DOWN]:
        personagem.y += velocidade

    # Pinta o fundo
    janela.fill(azul)

    limites = janela.get_rect()  # Obtém os limites da janela
    personagem.clamp_ip(limites)  # Mantém o personagem dentro dos limites da janela

    # Desenha o personagem
    pygame.draw.rect(janela, vermelho, personagem)

    # Atualiza a tela
    pygame.display.update()

    # Limita a 60 FPS
    relogio.tick(60)

# Encerra o Pygame
pygame
#Adições:
