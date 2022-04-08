import sys
import pygame
from bullet import Bullet
from alien import Alien


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
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
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
    aliens.draw(screen)
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


def create_fleet(ai_settings, screen, ship, aliens):
    """
    Cria uma frota completa de aliens
    :param ai_settings:
    :param screen:
    :param aliens:
    :return:
    """
    # Cria um alien e calcula o numero de aliens em uma linha
    # O espaçamento entre os aliens é a largura de um alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Cria a frota de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """
    Determina quantos aliens cabem em uma linha
    :param ai_settings:
    :param alien_width:
    :return:
    """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """
    Cria um alien e posiciona na linha
    :param ai_settings:
    :param screen:
    :param aliens:
    :param alien_number:
    :return:
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """
    Deytermina quantas linhas de aliens cabem na tela
    :param ai_settings:
    :param ship_height:
    :param alien_height:
    :return:
    """
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, aliens):
    """
    Verifica se a frota está em uma das bordas e Atualiza a posição de todos aliens na frota
    :param aliens:
    :return:
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def check_fleet_edges(ai_settings, aliens):
    """
    Responde apropriadamente se algum alien atingiu a borda
    :param ai_settings:
    :param aliens:
    :return:
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_directions(ai_settings, aliens)
            break


def change_fleet_directions(ai_settings, aliens):
    """
    Faz a frota descer e mudar de direção
    :param ai_settings:
    :param aliens:
    :return:
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
        ai_settings.fleet_direction *= -1
