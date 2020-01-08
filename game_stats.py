class GameStats():
    """All the statistics for the game"""

    def __init__(self, ai_settings):
        """Initialises statistics for the game"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Initialises statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
