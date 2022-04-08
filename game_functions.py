import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """
    Responde a eventos de teclado e mouse
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
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
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


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


def update_screen(ai_settings, screen, ship, bullets):
    """
    Atualiza as imagens na tela e alterna para a nova tela
    :param ai_settings:
    :param screen:
    :param ship:
    :return:
    """
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    # Redesenha todos os projéteis atrás da nave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Deixa a tela mais recente visivel
    pygame.display.flip()


def update_bullets(bullets):
    """
    Atualiza a posição dos projéteis e livra-se dos projéteis antigos
    :return:
    """
    # Atualiza posição dos projéteis
    bullets.update()
    # Livra-se dos projéteis que passaram pelo topo da tela
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """
    Dispara um projétil se o limite ainda não foi alcançado
    :return:
    """
    # Verifica se ainda há numero de projéteis permitidos
    if len(bullets) < ai_settings.bullets_allowed:
        # Cria um novo projétil e adiciona ao grupo de projéteis
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
