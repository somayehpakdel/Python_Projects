import random

def generate_random(start: int, end: int) -> int:
    """generate a random number between start and end

    :param start: start of the range
    :param end: end of the range
    :return: a random number between start and end
    """
    return random.randint(start, end)