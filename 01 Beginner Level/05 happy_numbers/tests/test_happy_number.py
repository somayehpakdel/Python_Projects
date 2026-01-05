from src.happy_number import happy_numbers


def test_happy_numbers():
    assert happy_numbers(19)[0] is True, "19 is a happy number"
    assert happy_numbers(7)[0] is True, "7 is a happy number"
    assert happy_numbers(2)[0] is False, "2 is not a happy number"
    assert happy_numbers(4)[0] is False, "4 is not a happy number"


def test_happy_numbers_sequence():
    assert happy_numbers(19)[1][-1], "19 is a happy number"
    assert happy_numbers(7)[1][-1], "7 is a happy number"
    assert happy_numbers(2)[1][-1] != 1, "2 is not a happy number"
    assert happy_numbers(4)[1][-1] != 1, "4 is not a happy number"