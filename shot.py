# filepath: c:\Users\super\OneDrive\Escritorio\Clases\Apuntes\Metos2\Github\videojuego_nuevo\shot.py

class Shot:
    def __init__(self, x, y, speed, damage):
        """
        Initialize a Shot instance.

        :param x: The x-coordinate of the shot.
        :param y: The y-coordinate of the shot.
        :param speed: The speed of the shot.
        :param damage: The damage the shot can inflict.
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.active = True  # Indicates if the shot is still active

    def move(self):
        """
        Move the shot based on its speed.
        """
        self.y += self.speed
        if self.y < 0:  # Deactivate the shot if it goes off-screen
            self.active = False

    def hit_target(self, target):
        """
        Check if the shot hits a target.

        :param target: The target entity to check collision with.
        :return: True if the shot hits the target, False otherwise.
        """
        if not self.active:
            return False

        shot_bounds = (self.x, self.y, 1, 1)  # Represent the shot as a point
        target_bounds = target.get_bounds()

        # Check for collision
        if (
            shot_bounds[0] < target_bounds[0] + target_bounds[2] and
            shot_bounds[0] + shot_bounds[2] > target_bounds[0] and
            shot_bounds[1] < target_bounds[1] + target_bounds[3] and
            shot_bounds[1] + shot_bounds[3] > target_bounds[1]
        ):
            self.active = False  # Deactivate the shot after hitting
            target.health -= 1  # Reduce the target's health by 1
            return True

        return False