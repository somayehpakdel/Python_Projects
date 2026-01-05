import pytest
from src.monty_hall import monty_hall, monty_hall_simulation


@pytest.mark.parametrize(
    "switch, expected", 
    [(True, [True, False]),
    (False, [True, False]),])
def test_monty_hall(switch, expected):
    assert monty_hall(switch) in expected


# Mock function to control randomness
def mock_random_choice(choices):
    return choices[0]  # Always pick the first choice for predictable outcomes

@pytest.fixture
def mock_random(monkeypatch):
    # Mock random.shuffle and random.choice
    monkeypatch.setattr("random.shuffle", lambda x: None)  # No-op for shuffle
    monkeypatch.setattr("random.choice", mock_random_choice)

def test_monty_hall_switched(mock_random):
    assert monty_hall(swiched=True) is True  # Player should win when switching

def test_monty_hall_not_switched(mock_random):
    assert monty_hall(swiched=False) is False  # Player should lose when not switching

def test_monty_hall_simulation(mock_random):
    num_trials = 10  # Small number for testing purposes

    wins_switched, wins_not_switched = monty_hall_simulation(num_trials)
    
    # Check that the wins are as expected based on the mocked behavior
    assert wins_switched == num_trials
    assert wins_not_switched == 0

if __name__ == "__main__":
    pytest.main()
