class Settings():
    """
    Uma classe para armazenar todas as configurações do jogo invasão alien
    """
    def __init__(self):
        """
        Inicializa as configurações do jogo
        """
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # Configurações da nave
        self.ship_speed_factor = 1
        # Configuração dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
