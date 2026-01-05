import pytest
from src.number_to_word import number_to_word_english, number_to_word_farsi


def test_number_to_word_english():
    assert number_to_word_english(123) == "One Hundred Twenty-Three"
    assert number_to_word_english(1000) == "One Thousand"
    assert number_to_word_english(1000000) == "One Million"
    assert number_to_word_english(1000800000) == "One Billion, Eight Hundred Thousand"
    assert (number_to_word_english(1234567890) ==
            "One Billion, Two Hundred Thirty-Four Million, Five Hundred Sixty-Seven Thousand, Eight Hundred Ninety"
            )


def test_number_to_word_farsi():
    assert number_to_word_farsi(123) == "صد و بیست و سه"
    assert number_to_word_farsi(1000) == "یک هزار"
    assert number_to_word_farsi(1000000) == "یک میلیون"
    assert number_to_word_farsi(1000000000) == "یک میلیارد"
    assert (number_to_word_farsi(1234567890) ==
            "یک میلیارد و دویست و سی و چهار میلیون و پانصد و شصت و هفت هزار و هشتصد و نود"
            )


def test_number_to_word_english_valueerror_larger_12_digit():
    with pytest.raises(ValueError):
        number_to_word_english(10 ** 12)


def test_number_to_word_english_valueerror_negetive_number():
    with pytest.raises(ValueError):
        number_to_word_english(-123)