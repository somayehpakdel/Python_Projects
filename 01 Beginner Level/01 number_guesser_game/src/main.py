from src.utils.input_validator import get_valid_input, play_again
from src.game_logic.number_generator import generate_random


def main():
    """
    Main function to run the guessing game.
    """
    print(f'What range would you like to play?')
    start = get_valid_input('Enter start of rage:')
    end = get_valid_input('Enter end of rage:')
    print(f'range: ({start} , {end})')
    number = generate_random(start, end)
    score = 100
    while True:
        if score <= 0:
            print(f'The number was {number}')
            print('Game over! You ran out of attempts.')
            break
        user_input = get_valid_input('Enter your guess:')
        if user_input == number:
            print('Congratulations! You guessed correctly!')
            print(f'Your score is {score}')
            break
        elif user_input < number:
            score -= 10
            print('Your guess is too low. Try again.')
            print(print(f'Your score is {score}'))
        else:
            score -= 10
            print(f'Your score is {score}')
            print('Your guess is too high. Try again.')
    if play_again():
        main()
    else:
        print('Thanks for playing!')


if __name__=='__main__':
    print('Welcome to the Guessing Game!')
    main()