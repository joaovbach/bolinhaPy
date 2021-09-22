import pygame
from bolaInimiga import BolaInimiga as inimigo
from player import Player as jogador
import random


pygame.init()
inimigos = []
telaX = 1000
telaY = 1000
quadradoJogoX = 800
quadradoJogoY = 800
janela = pygame.display.set_mode((telaX,telaY))

contador = 1000

delay = 0

player = jogador([500,500])
pygame.draw.circle(janela, (0, 0, 255), (player.posi[0],player.posi[1]), 50)
pygame.draw.rect(janela, (0,0,255), pygame.Rect((telaX/2)-quadradoJogoX/2, (telaY/2)-quadradoJogoY/2, quadradoJogoX, quadradoJogoY),  2)

def instaciaInimigo():
    inimigos.append(inimigo([quadradoJogoX,quadradoJogoY]))
    pygame.draw.circle(janela, (0, 255, 0), (inimigos[len(inimigos)-1].posi[0], inimigos[len(inimigos)-1].posi[1]), 50)

def colisoes(objeto):
    distanciaX = abs(objeto.posi[0] - player.posi[0])
    distanciaY = abs(objeto.posi[1] - player.posi[1])

    if distanciaX < 70 and distanciaY < 70:
        pygame.draw.circle(janela, (0, 0, 0), (objeto.posi[0], objeto.posi[1]), 50)
        inimigos.remove(objeto)
        player.vida = player.vida - 1
        pygame.draw.circle(janela, (0, 0, 0), (120, 0), 50)

def moveInimigos():
    for i in inimigos:
        pygame.draw.circle(janela, (0, 0, 0),(i.posi[0], i.posi[1]), 50)
        if i.destroy([quadradoJogoX, quadradoJogoY]) == False:
            i.move()
            pygame.draw.circle(janela, (0, 255, 0), (i.posi[0], i.posi[1]), 50)
            colisoes(i)
        else:
            inimigos.remove(i)

def UI():
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('VIDA: ' + str(player.vida), True, (0, 0, 255))
    janela.blit(textsurface, (0, 0))


while True:
    if contador > 400:
        instaciaInimigo()
        #instaciaInimigo([0,0],[800,600])
        contador=0

    else:
        contador+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    comando = pygame.key.get_pressed()
    if comando[pygame.K_RIGHT]:
        pygame.draw.circle(janela, (0, 0, 0), (player.posi[0], player.posi[1]), 50)
        player.posi[0] += 1

    if comando[pygame.K_LEFT]:
        pygame.draw.circle(janela, (0, 0, 0), (player.posi[0], player.posi[1]), 50)
        player.posi[0] -= 1

    if comando[pygame.K_UP]:
        pygame.draw.circle(janela, (0, 0, 0), (player.posi[0], player.posi[1]), 50)
        player.posi[1] -= 1

    if comando[pygame.K_DOWN]:
        pygame.draw.circle(janela, (0, 0, 0), (player.posi[0], player.posi[1]), 50)
        player.posi[1] += 1

    if delay > 100:
        moveInimigos()
        delay=0

    else:
        delay+=1

    moveInimigos()
    UI()

    pygame.draw.circle(janela, (255,0,0),(player.posi[0], player.posi[1]),50)
    pygame.display.update()