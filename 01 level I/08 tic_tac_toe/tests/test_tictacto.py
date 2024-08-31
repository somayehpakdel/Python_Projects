import pytest
from src.tic_tac_toe import Board, Player


@pytest.fixture(scope='module')
def board_object():
    board = Board()
    board.run_state = 'test'
    return board

# Test class for Board
class TestBoard:
    @pytest.mark.parametrize(
        "state, expected",
        [
            (['X', 'X', 'X', '4', '5', '6', '7', '8', '9'], True),  # Row win
            (['1', '2', '3', 'X', 'X', 'X', '7', '8', '9'], True),  # Row win
            (['1', '2', '3', '4', '5', '6', 'X', 'X', 'X'], True),  # Row win
            (['X', '2', '3', 'X', '5', '6', 'X', '8', '9'], True),  # Column win
            (['1', 'X', '3', '4', 'X', '6', '7', 'X', '9'], True),  # Column win
            (['X', '2', '3', '4', 'X', '6', '7', '8', 'X'], True),  # Diagonal win
            (['1', '2', 'X', '4', 'X', '6', 'X', '8', '9'], True),  # Diagonal win
        ])
    def test_check_wins(self, board_object, state, expected):
        board_object.board = state
        assert board_object.check_wins() == expected

    def test_check_tie(self, board_object):

        # Test tie condition
        board_object.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        assert board_object.check_tie() is True

        # Test non-tie condition
        board_object.board = ['X', 'O', '3', 'O', '5', '6', '7', '8', '9']
        assert board_object.check_tie() is False

# Test class for Player
class TestPlayer:
    def test_make_move(self, board_object):
        player = Player('Player 1', 'X')
        
        # Make a valid move
        result_board = player.make_move(board_object, cell=1)
        assert result_board[0] == 'X'  # Player should have marked the first cell
        
        # Try to make an invalid move
        player.make_move(board_object, cell=1)  # This should prompt an error message
        assert board_object.message == 'That spot is taken, please choose another place'

if __name__ == "__main__":
    pytest.main()
