from character import Character

class Player(Character):
    def __init__(self, x, y, width, height, health):
        """
        Initialize the player with position, size, health, score, and lives.

        :param x: The x-coordinate of the player.
        :param y: The y-coordinate of the player.
        :param width: The width of the player.
        :param height: The height of the player.
        :param health: The health points of the player.
        """
        super().__init__(x, y, width, height, health)
        self.score = 0
        self.lives = 3

    def move(self, direction):
        """
        Moves the player in the specified direction.
        :param direction: str - 'up', 'down', 'left', 'right'
        """
        if direction == 'up':
            self.y -= 10  # Example movement value
        elif direction == 'down':
            self.y += 10
        elif direction == 'left':
            self.x -= 10
        elif direction == 'right':
            self.x += 10
        print(f"Player moves {direction}")

    def shoot(self):
        """
        Simulates the player shooting a projectile.
        """
        projectile = super().shoot()  # Use the shoot method from Character
        print("Player shoots!")
        return projectile

    def earn_star(self):
        """
        Increases the player's score by 1 when they earn a star.
        """
        self.score += 1
        print(f"Player earned a star! New score: {self.score}")