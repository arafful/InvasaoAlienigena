import pygame


class Ship():
    """
    Controla a nave
    """

    def __init__(self, ai_settings, screen):
        """
        Inicializa a nave e define sua posição inicial
        """
        self.screen = screen
        self.ai_settings = ai_settings
        # Carrega a imagem da nave
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicia cada nova nave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Armazena um valor decimal para o centro da nava
        float(self.rect.centerx)
        # Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Atualiza a posição da nave de acordo com a Flag de movimento
        :return:
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """
        Desenha a nave na posição atual
        :return:
        """
        self.screen.blit(self.image, self.rect)

