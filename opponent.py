class Opponent:
    def __init__(self, is_star=False):
        """
        Initialize an Opponent instance.
        :param is_star: Boolean indicating if the opponent is a star (default: False).
        """
        self.is_star = is_star

    def collide(self, shot, game):
        """
        Handle collision with a player's shot.
        :param shot: The player's shot.
        :param game: The game instance to update the score.
        """
        if shot.hit_target(self):
            if not self.is_star:
                self.convert_to_star()
                game.update_score(1)  # Incrementar puntuación
                
    def move(self):
        """
        Logic for moving the opponent.
        """
        # Implement movement logic here
        print("Opponent is moving.")

    def shoot(self):
        """
        Logic for the opponent to shoot.
        """
        # Implement shooting logic here
        print("Opponent is shooting.")

    def check_if_star(self):
        """
        Check if the opponent is a star.
        :return: Boolean indicating if the opponent is a star.
        """
        return self.is_star

    def convert_to_star(self):
        """
        Convert the opponent into a star that gives +1 score.
        """
        self.is_star = True
        print("Opponent has converted into a star!")