import pygame
from settings import Settings
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
    # Inicia o laço principal do jogo
    while True:
        # Observa eventos do teclado e mouse
        gf.check_events(ship)
        ship.update()
        # Redesenha a tela a cada passagem pelo laço e deixa a tela mais recente visivel
        gf.update_screen(ai_settings, screen, ship)
run_game()

