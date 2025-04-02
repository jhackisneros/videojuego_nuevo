from player import Player
from opponent import Opponent

class Game:
    def __init__(self):
        """
        Initialize the game with default attributes.
        """
        self.score = 0
        self.player = Player(x=50, y=400, width=50, height=50, health=100)
        self.opponent = Opponent()
        self.is_running = False

    def start(self):
        """
        Start the game by setting is_running to True.
        """
        self.is_running = True
        print("Game started!")

    def update(self):
        """
        Update the game state, including player and opponent actions.
        """
        if not self.is_running:
            return
    def update_score(self, points):
        """
        Update the player's score.
        :param points: Points to add to the score.
        """
        self.score += points
        print(f"Score updated! Current score: {self.score}")
    

        # Example logic for updating game state
        self.player.update(0)  # Update player state
        self.opponent.move()   # Move the opponent
        print("Game updated!")

    def display_status(self):
        """
        Display the player's score and lives on the screen.
        """
        print(f"Score: {self.score} | Lives: {self.player.lives}")

    def end_game(self):
        """
        End the game by setting is_running to False.
        """
        self.is_running = False
        print("Game over!")