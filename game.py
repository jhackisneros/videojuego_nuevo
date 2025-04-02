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

    def remove_opponent(self, opponent):
        """
        Remove an opponent and spawn a boss if necessary.
        :param opponent: The opponent to remove.
        """
        if isinstance(opponent, Opponent):
            print("Opponent defeated!")
            self.opponent = Boss()  # Aparece el jefe final
            print("Boss has appeared!")

    def end_game(self):
        """
        End the game and display a victory or game over message.
        """
        self.is_running = False
        if isinstance(self.opponent, Boss) and self.player.lives > 0:
            print("Victory! You defeated the boss!")
        else:
            print("Game over!")