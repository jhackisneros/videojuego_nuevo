from entity import Entity

# filepath: C:/Users/super/OneDrive/Escritorio/Clases/Apuntes/Metos2/Github/videojuego_nuevo/character.py

class Character(Entity):
    def __init__(self, x, y, width, height, health):
        """
        Class representing a character with health in the game.

        :param x: The x-coordinate of the character.
        :param y: The y-coordinate of the character.
        :param width: The width of the character.
        :param height: The height of the character.
        :param health: The health points of the character.
        """
        super().__init__(x, y, width, height)
        self.health = health

    def take_damage(self, amount):
        """
        Reduce the character's health by a specified amount.

        :param amount: The amount of damage to take.
        """
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.active = False  # Deactivate the character if health is 0

    def heal(self, amount):
        """
        Increase the character's health by a specified amount.

        :param amount: The amount of health to restore.
        """
        self.health += amount

    def is_alive(self):
        """
        Check if the character is still alive.

        :return: True if health is greater than 0, False otherwise.
        """
        return self.health > 0

    def update(self, delta_time):
        """
        Update the character's state. Can be extended by subclasses.

        :param delta_time: Time elapsed since the last update.
        """
        # Example: Add custom logic for character updates here
        pass

    def render(self, screen):
        """
        Render the character on the screen. Can be extended by subclasses.

        :param screen: The game screen or surface to draw on.
        """
        # Example: Add custom rendering logic here
        pass