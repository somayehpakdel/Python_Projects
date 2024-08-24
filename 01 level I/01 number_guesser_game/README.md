# Number Guessing Game
---
## Description
This is a simple number guessing game implemented in Python. The program generates a random number within a user-defined range, and the player tries to guess the number. After each guess, the program provides hints to guide the player whether the guess was too high or too low. The game continues until the player guesses the correct number.

### How to Play
Guess the hidden number within 10 chances by applying the binary search technique.
- Run the game by executing the `main.py` script.

#### Game Rules:
1. The game provides feedback on whether your guess is too low or too high and you print your score.
2. You have 10 chances to guess the correct number.
3. Every time you guess incorrectly, your score will decrease by 10 units.
4. If you guess the number correctly within 10 chances, you win the game.
5. If you exhaust all 10 chances without guessing the number, the game ends, and the correct number is revealed.

## Code Structure

The code is organized into three main components:

1. **src/main.py**
This is the entry point of the application. It contains the `main` function, which is responsible for running the guessing game. Here's what the `main` function does:

- Prompts the user to enter the start and end of the range for the guessing game.
- Generates a random number within the specified range using the `generate_random` function from the `number_generator` module.
- Initializes the player's score to 100.
- Enters a loop where the player can keep guessing until they either guess the correct number or run out of attempts.
- For each incorrect guess, the player's score is reduced by 10 points.
- If the player guesses the correct number, the game ends, and the final score is displayed.
- If the player runs out of attempts, the game ends, and the correct number is revealed.
- After the game ends, the player is prompted to play again or quit.

2. **src/utils/input_validator.py**
This module contains utility functions for validating user input:

- `get_valid_input`: Prompts the user for input and validates that the input is an integer within a specified range.
- `play_again`: Prompts the user to play again and returns a boolean value based on the user's response.

3. **src/game_logic/number_generator.py**
This module contains a function for generating a random number within a specified range:

- `generate_random`: Generates a random integer between the provided start and end values (inclusive).

The code follows a modular structure, separating concerns into different modules and functions. The `main.py` file acts as the controller, orchestrating the game flow and utilizing the utility functions from the other modules.



