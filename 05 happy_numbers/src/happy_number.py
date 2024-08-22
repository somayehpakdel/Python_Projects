from typing import Tuple, List


def happy_numbers(number: int) -> Tuple[bool, List[int]]:
    """
    Determines if a given number is a happy number.

    A happy number is defined by the following process:
    Starting with any positive integer, replace the number by the sum
    of the squares of its digits, and repeat the process until the number
    either equals 1 (where it will stay), or it loops endlessly in a cycle
    that does not include 1. Numbers for which this process ends in 1 are
    considered happy numbers.

    :param number: The number to check for happiness.
    :return: True if the number is a happy number, False otherwise.

    :Example:

    >>> is_happy(19)
    True

    >>> is_happy(2)
    False
    """
    seen_numbers = set()
    sequence_numbers = [number]
    while number != 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = sum((int(num) ** 2 for num in str(number)))
        sequence_numbers.append(number)
    return number == 1, sequence_numbers
