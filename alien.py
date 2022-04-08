import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    Uma classe que representa um únic alienigena da frota
    """
    def __init__(self, ai_settings, screen):
        """
        Inicializa o alienigena e define sua posição inicial
        :param ai_settings:
        :param screen:
        """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Carrega a imagem do Alien e define seu atributo rect
        self.image = pygame.image.load('images\img_alien.bmp')
        self.rect = self.image.get_rect()
        # Inicia cada novo alien próximo a parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Armazena a posição exata do alien
        self.x = float(self.rect.x)

    def blitme(self):
        """
        Desenha o alien em sua posição atual
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Move o alien
        :return:
        """
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """
        Devolve True se o alien estiver na borda da tela
        :return:
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

