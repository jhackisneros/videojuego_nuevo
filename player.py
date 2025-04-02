from character import Character

class Player(Character):
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height, health)
        self.score = 0
        self.lives = 3  # Vidas iniciales

    def take_damage(self, amount, game):
        """
        Reduce the player's health and handle lives.
        :param amount: Damage amount.
        :param game: The game instance to check for game over.
        """
        super().take_damage(amount)
        if not self.is_alive():
            self.lives -= 1
            print(f"Player lost a life! Remaining lives: {self.lives}")
            if self.lives <= 0:
                game.end_game()
            else:
                self.respawn()

    def respawn(self):
        """
        Respawn the player after losing a life.
        """
        self.health = 100
        self.x, self.y = 50, 400  # Reset position
        print("Player respawned!")

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