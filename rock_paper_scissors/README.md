
# Rock Paper Scissors Game

This is a simple implementation of the classic Rock Paper Scissors game in Python. The game can be played between two human players or between a human player and the computer.

## Features

- Play against another human player or against the computer
- Validate user input for valid choices (rock, paper, or scissors)
- Determine the winner based on the game rules
- Option to play multiple rounds

## How to Run

1. Make sure you have Python installed on your system.
2. Clone or download the repository.
3. Navigate to the project directory.
4. Run the following command:
```bash
python src/main.py
```
5. Follow the prompts to choose the number of players (1 for computer, 2 for another human player).
6. Enter your choice when prompted.
7. The game will determine the winner and ask if you want to play again.

## Code Structure

The code is organized into a single Python class called `RockPaperScissors` with the following methods:

- `__init__`: Initializes the game with the valid choices, winning combinations, and player choices.
- `get_user_choice`: Prompts the user to enter their choice and validates the input.
- `get_computer_choice`: Randomly selects the computer's choice.
- `get_winner`: Determines the winner based on the player choices.
- `print_results`: Prints the player choices.
- `play`: Plays a single game session.
- `run`: Prompts the user to play again and continues playing.
- `numbers_users`: Prompts the user to enter the number of players.

The `main.py` file creates an instance of the `RockPaperScissors` class, prompts the user for the number of players, and starts the game loop.

