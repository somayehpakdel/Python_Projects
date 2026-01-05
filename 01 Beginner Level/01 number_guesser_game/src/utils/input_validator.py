def get_valid_input(message: str) -> int:
    """
    Prompts the user for input and validates the input to ensure it is a valid integer.

    Args:
        message (str): The message to display to the user.

    Returns:
        int: The valid integer input by the user.

    :param message: The message to diplay to the user
    :return: The valid integer input by the user
    """
    while True:
        try:
            value = int(input(f"{message}"))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_again() -> bool:
    """ Ask the user if they want to play again.

    :return: True if they want to play again, False otherwise
    """
    user_input = input("Do you want to play again? (y/n):").lower()
    if user_input == 'y':
        return True
    elif user_input == 'n':
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")