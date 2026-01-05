from src.CONSTANTS import ENGLISH_UNDER_20, ENGLISH_TENS, ENGLISH_ABOVE_100
from src.CONSTANTS import FARSI_UNDER_20, FARSI_TENS,FARSI_HUNDRESD, FARSI_ABOVE_1000


def number_to_word_english(num: int) -> str:
    """
    Convert a given integer to its English word representation.

    Args:
        num : The integer to be converted to words. Must be non-negative.

    Returns:
        The English word representation of the input number.

    Raises:
        ValueError: If the input is negative or exceeds the maximum supported value.

    Examples:
        >>> number_to_word_english(0)
        'Zero'
        >>> number_to_word_english(42)
        'Forty-Two'
        >>> number_to_word_english(1234567)
        'One Million, Two Hundred Thirty-Four Thousand, Five Hundred Sixty-Seven'

    Note:
        - The function uses constants defined in CONSTANTS.py for number-to-word mappings.
        - For numbers 100 and above, it uses a recursive approach to break down the number.
    """
    if len(str(num)) > 12 or num < 0:
        raise ValueError("The number must be positive and smaller than 12 digits.")
    if num < 20:
        return ENGLISH_UNDER_20[num]
    if num < 100:
        ones: int = num % 10
        tens: int = num // 10
        return ENGLISH_TENS[tens] + ("-" + number_to_word_english(ones) if ones else "")
    
    pivot: int = max([key for key in ENGLISH_ABOVE_100 if key <= num])
    p1: int = num // pivot
    p2: int = num % pivot
    return (number_to_word_english(p1) + " " 
            + ENGLISH_ABOVE_100[pivot] 
            + ("," if ENGLISH_ABOVE_100[pivot] != "Hundred" and p2 != 0 else "")
            + (" " + number_to_word_english(p2) if p2 else "")
            )


def number_to_word_farsi(num: int) -> str:
    """
    Convert a given integer to its Farsi (Persian) word representation.

    Args:
        num: The integer to be converted to words. Must be non-negative.

    Returns:
        The Farsi word representation of the input number.

    Raises:
        ValueError: If the input is negative or exceeds the maximum supported value.

    Examples:
        >>> number_to_word_farsi(0)
        'صفر'
        >>> number_to_word_farsi(42)
        'چهل و دو'
        >>> number_to_word_farsi(1234)
        'یک هزار و دویست و سی و چهار'

    Note:
        - The function uses constants defined (FARSI_UNDER_20, FARSI_TENS, etc.) 
        for number-to-word mappings.
        - For numbers 100 and above, it uses a recursive approach to break down the number.
    """
    if len(str(num)) > 12 or num < 0:
        raise ValueError("The number must be positive and smaller than 12 digits.")
    if num < 20:
        return FARSI_UNDER_20[num]
    if num < 100:
        ones: int = num % 10
        tens: int = num // 10
        return FARSI_TENS[tens] + (" و " + number_to_word_farsi(ones) if ones else "")
    if num < 1000:
        tens_1: int = num % 100
        hundreds: int = num // 100
        return FARSI_HUNDRESD[hundreds] + (" و " + number_to_word_farsi(tens_1) if tens_1 else "")

    pivot: int = max([key for key in FARSI_ABOVE_1000 if key <= num])
    p1: int = num // pivot
    p2: int = num % pivot
    return number_to_word_farsi(p1) + " " + FARSI_ABOVE_1000[pivot] + (" و " + number_to_word_farsi(p2) if p2 else "")


if __name__ == "__main__":
    language = input("Enter the language (English or Farsi): ").lower()
    number = int(input("Enter the number: "))
    if language == "english":
        print(number_to_word_english(number))
    elif language == "farsi":
        print(number_to_word_farsi(number)[::-1])
