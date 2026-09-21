import pygame
import sys

pygame.init()
LARGURA_TELA, ALTURA_TELA = 800, 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Demo Do Soul Heart")
clock = pygame.time.Clock()

fonte_titulo = pygame.font.SysFont(None, 72)
fonte_botao = pygame.font.SysFont(None, 40)

BRANCO = (255, 255, 255)
CINZA_ESCURO = (60, 60, 70)
CINZA_CLARO = (90, 90, 105)
VERMELHO_ESCURO = (120, 40, 40)
VERMELHO_CLARO = (160, 60, 60)

estado_jogo = "menu"

botao_iniciar = pygame.Rect(300, 260, 200, 60)
botao_sair = pygame.Rect(300, 340, 200, 60)


LARGURA_MUNDO, ALTURA_MUNDO = 2400, 1800

jogador_x, jogador_y = LARGURA_MUNDO // 2, ALTURA_MUNDO // 2
tamanho = 50
velocidade_normal = 5
velocidade_correndo = 10

def desenhar_botao(rect, texto, cor_normal, cor_hover, mouse_pos):
    cor = cor_hover if rect.collidepoint(mouse_pos) else cor_normal
    pygame.draw.rect(tela, cor, rect, border_radius=8)
    texto_render = fonte_botao.render(texto, True, BRANCO)
    tela.blit(texto_render, texto_render.get_rect(center=rect.center))

rodando = True
while rodando:
    mouse_pos = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if estado_jogo == "menu":
                if botao_iniciar.collidepoint(mouse_pos):
                    estado_jogo = "jogando"
                elif botao_sair.collidepoint(mouse_pos):
                    rodando = False

    if estado_jogo == "menu":
        tela.fill((20, 20, 30))
        titulo = fonte_titulo.render("DEMO DO MEU JOGO", True, BRANCO)
        tela.blit(titulo, titulo.get_rect(center=(400, 160)))
        desenhar_botao(botao_iniciar, "INICIAR", CINZA_ESCURO, CINZA_CLARO, mouse_pos)
        desenhar_botao(botao_sair, "SAIR", VERMELHO_ESCURO, VERMELHO_CLARO, mouse_pos)

    elif estado_jogo == "jogando":
        teclas = pygame.key.get_pressed()

        correndo = teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]
        velocidade = velocidade_correndo if correndo else velocidade_normal

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            jogador_x -= velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            jogador_x += velocidade
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            jogador_y -= velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            jogador_y += velocidade

        jogador_x = max(0, min(jogador_x, LARGURA_MUNDO - tamanho))
        jogador_y = max(0, min(jogador_y, ALTURA_MUNDO - tamanho))


        camera_x = jogador_x - LARGURA_TELA // 2
        camera_y = jogador_y - ALTURA_TELA // 2

       
        camera_x = max(0, min(camera_x, LARGURA_MUNDO - LARGURA_TELA))
        camera_y = max(0, min(camera_y, ALTURA_MUNDO - ALTURA_TELA))

        tela.fill((30, 30, 40))


        for gx in range(0, LARGURA_MUNDO, 200):
            pygame.draw.line(tela, (50, 50, 60), (gx - camera_x, 0), (gx - camera_x, ALTURA_TELA))
        for gy in range(0, ALTURA_MUNDO, 200):
            pygame.draw.line(tela, (50, 50, 60), (0, gy - camera_y), (LARGURA_TELA, gy - camera_y))

       
        pygame.draw.rect(
            tela, (255, 100, 100),
            (jogador_x - camera_x, jogador_y - camera_y, tamanho, tamanho)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()