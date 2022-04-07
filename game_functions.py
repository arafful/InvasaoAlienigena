import sys
import pygame


def check_events(ship):
    """
    Responde a eventos de teclado e mouse
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    """
    Responde a pressionamento de teclas
    :param event:
    :param ship:
    :return:
    """
    if event.key == pygame.K_RIGHT:
        # Move a espaçonave para a direita
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """
    Responde a soltura de teclas
    :param event:
    :param ship:
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """
    Atualiza as imagens na tela e alterna para a nova tela
    :param ai_settings:
    :param screen:
    :param ship:
    :return:
    """
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Deixa a tela mais recente visivel
    pygame.display.flip()
