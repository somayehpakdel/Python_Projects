import random
import getpass
from typing import List, Tuple, Optional

class RockPaperScissors:
    """
    Rock paper scissors game in 2 stats:
    - between 2 users
    - between a user and computer
    
    Attributes:
        choices : A list of valid choices (rock, paper, scissors).
        win_stats : A list of winning combinations (e.g., ('rock', 'scissors')).
        user1_choice : The choice made by the first user.
        user2_choice : The choice made by the second user (user2 or computer).
        numbers_of_users : Number of users playing (1 for 2 users or 2 for a user and computer).
    """
    def __init__(self):
        self.choices: List[str] = ["rock", "paper", "scissors"]
        self.win_stats: List[Tuple[str, str]] = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]
        self.user1_choice: Optional[str]= None # Always is a human
        self.user2_choice: Optional[str] = None  # Human or computer
        self.numbers_of_users: int = 1  # Can be either 1 or 2

    def get_user_choice(self, user: int) -> None:
        """
        Prompts the user to enter their choice and validates the input.

        If the input is invalid, the method calls itself recursively until a valid choice is entered.
        """

        if self.numbers_of_users == 1:
            user_input = input(f"User {user}: Enter your choice (rock, paper, or scissors): ").lower()
        else:
            user_input = getpass.getpass(f"User {user}: Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in self.choices:
            if user == 1:
                self.user1_choice = user_input
            else:
                self.user2_choice = user_input
        else:
            print("Invalid choice. Please try again.")
            self.get_user_choice()

    def get_computer_choice(self) -> None:
        """
        Randomly selects the computer's choice from the list of valid choices.
        """

        self.user2_choice = random.choice(self.choices)

    def get_winner(self) -> None:
        """
        Determines the winner of the game based on the user's and computer's choices.
        """

        if self.user1_choice == self.user2_choice:
            self.print_results()
            print("It's a tie!")
        elif (self.user1_choice, self.user2_choice) in self.win_stats:
            self.print_results()
            print("User1 wins!" if self.numbers_of_users == 2 else "You win!")
        else:
            self.print_results()
            print("User2 wins!" if self.numbers_of_users == 2 else "The computer wins!" )

    def print_results(self) -> None:
        """
        Prints the user's choice and the computer's choice.
        """

        print("User1's" if self.numbers_of_users == 2 else "Your", f'choice = {self.user1_choice}')
        print("User2's" if self.numbers_of_users == 2 else "Computer's", f'choice = {self.user2_choice}')

    def play(self):
        """
        Play one session of the game and determine the winner.
        """

        self.get_user_choice(1)
        if self.numbers_of_users == 1:
            self.get_computer_choice()
        else:
            self.get_user_choice(2)
        self.get_winner()

    def run(self):
        """
        Prompts the user to play again and continues playing.
        """

        self.play()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            self.run()
        elif play_again == 'n':
            print("Thanks for playing!")
        else:
            print("Invalid choice. Please inter y or n: ")
            self.run()

    def numbers_users(self):
        """
        Prompts the user to enter the number of users and validates the input.
        """

        user_input = input("Enter the number of users (1 or 2): ")
        if user_input in ['1', '2']:
            self.numbers_of_users = int(user_input)
        else:
            print("Invalid choice. Please try again.")
            self.numbers_users()


if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    game = RockPaperScissors()
    game.numbers_users()
    game.run()