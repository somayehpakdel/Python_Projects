import random
from typing import Tuple


def monty_hall(swiched: bool) -> bool:
    """
    Simulates the Monty Hall problem.

    Args:
        swiched (bool): Whether the player switches their choice or not.

    Returns:
        bool: True if the player wins, False otherwise.
    """

    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    prize_door = doors.index('car')
    player_choice = random.choice(range(3))
    opened_door = random.choice([door for door in range(3) if door != player_choice and door != prize_door ])

    if swiched:
        player_choice = [door for door in range(3) if door != player_choice and door != opened_door][0]

    return player_choice == prize_door


def monty_hall_simulation(num_trials: int) -> Tuple[int, int]:
    """
    Simulates the Monty Hall problem multiple times and returns the win percentage.

    Args:
        num_trials (int): The number of trials to run.

    Returns:
        tuple: The win numbers.
    """

    wins_swiched = sum(monty_hall(True) for _ in range(num_trials))
    wins_not_swiched = sum(monty_hall(False) for _ in range(num_trials))
    return wins_swiched, wins_not_swiched


if __name__ == '__main__':
    num_trials = 100000
    wins_swiched, wins_not_swiched = monty_hall_simulation(num_trials)
    print(f"Number of wins with switching: {wins_swiched}")
    print(f"Number of wins without switching: {wins_not_swiched}")
    print(f"Win percentage with switching: {wins_swiched / num_trials * 100}%")
    print(f"Win percentage without switching: {wins_not_swiched / num_trials * 100}%")
