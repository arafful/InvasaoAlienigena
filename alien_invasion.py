import sys
import pygame
from settings import Settings
from ship import Ship

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
    ship = Ship(screen)
    # Inicia o laço principal do jogo
    while True:
        # Observa eventos do teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # Deixa a tela mais recente visivel
        pygame.display.flip()

run_game()
