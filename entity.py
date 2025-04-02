class Entity:
    def __init__(self, x, y, width, height):
        """
        Base class for all game entities.

        :param x: The x-coordinate of the entity.
        :param y: The y-coordinate of the entity.
        :param width: The width of the entity.
        :param height: The height of the entity.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = True  # Indicates if the entity is active in the game

    def update(self, delta_time):
        """
        Update the entity's state. To be overridden by subclasses.

        :param delta_time: Time elapsed since the last update.
        """
        pass

    def render(self, screen):
        """
        Render the entity on the screen. To be overridden by subclasses.

        :param screen: The game screen or surface to draw on.
        """
        pass

    def get_bounds(self):
        """
        Get the bounding box of the entity for collision detection.

        :return: A tuple (x, y, width, height).
        """
        return self.x, self.y, self.width, self.height

    def is_colliding(self, other):
        """
        Check if this entity is colliding with another entity.

        :param other: Another entity to check collision with.
        :return: True if colliding, False otherwise.
        """
        x1, y1, w1, h1 = self.get_bounds()
        x2, y2, w2, h2 = other.get_bounds()

        return (
            x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2
        )