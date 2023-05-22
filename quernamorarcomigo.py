import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

x = 50
y = 265


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('QUER NAMORAR CMG?')

while True:
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render("QUER NAMORAR COMIGO?", True, (255, 255, 255))
    rect_texto = texto.get_rect()
    rect_texto.center = (largura//2, altura//2-200)
    tela.blit(texto, rect_texto)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if botao.collidepoint(event.pos):
                tela.fill((0,0,0))
                botao_sim = pygame.draw.rect(tela, (255, 255, 255), (450, 265, 130, 60))
                x = randint(130, 320)
                y = randint(50, 420)
            if botao_sim.collidepoint(event.pos):
                fonte_fim = pygame.font.Font(None, 36)
                texto_fim = fonte_fim.render("TE AMO!", True, (255, 255, 255))
                rect_texto_fim = texto_fim.get_rect()
                pygame.mixer.music.load('X2Download (mp3cut.net).mp3')
                pygame.mixer.music.play()
                img = pygame.image.load('coracaoreal.jpg')
                img_retangulo = img.get_rect()
                img_retangulo.center = (largura//2, altura//2)


                fim = True
                while fim:
                    tela.fill((0, 0, 0))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                    rect_texto_fim.center = (largura//2, altura//2-200)
                    tela.blit(img, img_retangulo)
                    tela.blit(texto_fim, rect_texto_fim)
                    pygame.display.update()

    botao_nao = pygame.Rect(x, y, 130, 60)
    fonte_nao = pygame.font.Font(None, 36)
    texto_nao = fonte_nao.render('NÃO', True, (255, 255, 255))
    texto_nao_rect = texto_nao.get_rect()
    texto_nao_rect.center = botao_nao.center

    botao = pygame.draw.rect(tela, (0, 0, 255), (x, y, 130, 60))
    tela.blit(texto_nao, texto_nao_rect)

    botao_sim = pygame.Rect(450, 265, 130, 60)
    fonte_sim = pygame.font.Font(None, 36)
    texto_sim = fonte_sim.render('SIM', True, (255, 255, 255))
    texto_sim_rect = texto_sim.get_rect()
    texto_sim_rect.center = botao_sim.center

    botao_sim = pygame.draw.rect(tela, (255, 0, 0), (450, 265, 130, 60))
    tela.blit(texto_sim, texto_sim_rect)
    pygame.display.update()