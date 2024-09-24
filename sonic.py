import pygame
import random


# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Sonic Game")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)

# Configurações do jogador
largura_jogador = 50
altura_jogador = 50
x_jogador = largura_tela // 2
y_jogador = altura_tela - altura_jogador - 10
velocidade_jogador = 5

# Configurações dos obstáculos
largura_obstaculo = 50
altura_obstaculo = 50
velocidade_obstaculo = 5
obstaculos = []

# Configurações do jogo
pontuacao = 0
fonte = pygame.font.SysFont(None, 35)

# Função para desenhar o jogador
def desenha_jogador(x, y):
    pygame.draw.rect(tela, azul, [x, y, largura_jogador, altura_jogador])

# Função para desenhar os obstáculos
def desenha_obstaculo(obstaculos):
    for obstaculo in obstaculos:
        pygame.draw.rect(tela, preto, [obstaculo[0], obstaculo[1], largura_obstaculo, altura_obstaculo])

# Função para mostrar a pontuação
def mostra_pontuacao(pontuacao):
    texto = fonte.render("Pontuação: " + str(pontuacao), True, preto)
    tela.blit(texto, [10, 10])

# Função principal do jogo
def jogo():
    global x_jogador, y_jogador, obstaculos, pontuacao
    fim_de_jogo = False
    clock = pygame.time.Clock()

    while not fim_de_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True

        # Movimento do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and x_jogador > 0:
            x_jogador -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and x_jogador < largura_tela - largura_jogador:
            x_jogador += velocidade_jogador

        # Adiciona novos obstáculos
        if random.randint(1, 20) == 1:
            obstaculos.append([random.randint(0, largura_tela - largura_obstaculo), -altura_obstaculo])

        # Move os obstáculos
        for obstaculo in obstaculos:
            obstaculo[1] += velocidade_obstaculo

        # Remove obstáculos fora da tela
        obstaculos = [obstaculo for obstaculo in obstaculos if obstaculo[1] < altura_tela]

        # Verifica colisão
        for obstaculo in obstaculos:
            if y_jogador < obstaculo[1] + altura_obstaculo and y_jogador + altura_jogador > obstaculo[1]:
                if x_jogador < obstaculo[0] + largura_obstaculo and x_jogador + largura_jogador > obstaculo[0]:
                    fim_de_jogo = True

        # Atualiza a pontuação
        pontuacao += 1

        # Desenha tudo na tela
        tela.fill(branco)
        desenha_jogador(x_jogador, y_jogador)
        desenha_obstaculo(obstaculos)
        mostra_pontuacao(pontuacao)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Inicia o jogo
jogo()
