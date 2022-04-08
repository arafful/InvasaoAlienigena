import pygame
from settings import Settings
from pygame.sprite import Group
from ship import Ship
import game_functions as gf

def run_game():
    """
    Inicializa o pygame, as configurações e o objeto screen
    :return:
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma nave
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()

    # Inicia o laço principal do jogo
    while True:
        # Observa eventos do teclado e mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        # Redesenha a tela a cada passagem pelo laço e deixa a tela mais recente visivel
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()

