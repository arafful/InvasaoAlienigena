class Settings():
    """
    Uma classe para armazenar todas as configurações do jogo invasão alien
    """
    def __init__(self):
        """
        Inicializa as configurações do jogo
        """
        self.screen_width = 1200
        self.screen_height = 680
        self.bg_color = (230, 230, 230)
        # Configurações da nave
        self.ship_speed_factor = 1
        # Configuração dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Configuração dos aliens
        self.alien_speed_factor = 0.1
        self.alien_drop_speed = 10
        # direção da frota = 1 representa direita; -1 representa esquerda
        self.fleet_direction = 1
