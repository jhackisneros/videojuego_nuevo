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

from opponent import Opponent

class Boss(Opponent):
    def __init__(self):
        """
        Initialize the Boss with enhanced attributes.
        """
        super().__init__()
        self.health = 200  # Boss has more health
        self.speed = 20    # Boss moves faster than regular opponents
        self.damage = 20   # Boss deals more damage

    def move(self):
        """
        Move the boss faster than regular opponents.
        """
        print("Boss is moving twice as fast!")
        # Implement boss-specific movement logic here
        # Example: Move the boss in a zigzag pattern
        self.x += self.speed
        if self.x > 800 or self.x < 0:  # Assuming screen width is 800
            self.speed = -self.speed  # Reverse direction

    def shoot(self):
        """
        Boss shoots more powerful projectiles.
        """
        print("Boss is shooting powerful projectiles!")
        # Implement boss-specific shooting logic here
        # Example: Shoot multiple projectiles at once
        return [
            {"x": self.x, "y": self.y, "speed": -10, "damage": self.damage},
            {"x": self.x - 10, "y": self.y, "speed": -10, "damage": self.damage},
            {"x": self.x + 10, "y": self.y, "speed": -10, "damage": self.damage},
        ]

    def take_damage(self, amount):
        """
        Reduce the boss's health and check if defeated.
        """
        self.health -= amount
        print(f"Boss takes {amount} damage! Remaining health: {self.health}")
        if self.health <= 0:
            self.health = 0
            self.active = False  # Deactivate the boss
            print("Boss defeated!")