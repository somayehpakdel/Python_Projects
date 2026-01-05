import random
from typing import List, Optional


class Board:
    def __init__(self) -> None:
        self.run_state: str = 'terminal'     #To differentiate between terminal and streamlit app
        self.message = ''       # For streamlit app
        self.board: List[str] = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',]

    def show_board(self) -> None:
        for i, j in enumerate(self.board):
            if (i + 1) % 3 == 0:
                print(j)
            else:
                print(j, end='|')

    def check_wins(self) -> bool:
        if (self.board[0] == self.board[1] == self.board[2]
            or self.board[3] == self.board[4] == self.board[5] 
            or self.board[6] == self.board[7] == self.board[8]
            or self.board[0] == self.board[3] == self.board[6]
            or self.board[1] == self.board[4] == self.board[7]
            or self.board[2] == self.board[5] == self.board[8]
            or self.board[0] == self.board[4] == self.board[8]
            or self.board[2] == self.board[4] == self.board[6]
        ):
            return True
        else:
            return False

    def check_tie(self) -> bool:
        for i in self.board:
            if i.isdigit():
                return False
        return True

class Player:
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol

    def make_move(self, board_object: Board, cell: int =1) -> List[str]:
        board = board_object.board
        cells = len(board)
        print(f'{self.name}\'s turn')
        if 'computer' in self.name.lower():
            choice: int = random.randint(1, cells)
        else:
            if board_object.run_state == 'terminal':
                choice = int(input(f'Please choose a number between 1-{cells}: '))
            else:
                choice = cell           #For use in streamlit app or pytest

        if board[choice - 1] == str(choice):        #Check if this place has been taken before
            board[choice - 1] = str(self.symbol)
            return board
        else:
            board_object.message = 'That spot is taken, please choose another place'
            print(board_object.message)
            if board_object.run_state == 'Terminal':
                self.make_move(board_object)
            return board


def play(player1: Player, player2: Player, board_object: Board) -> None:
    board_object.show_board()
    while True:
        if board_object.check_tie():
            print('It\'s a tie!')
            break
        player1.make_move(board_object)
        board_object.show_board()
        if board_object.check_wins():
            print(f'{player1.name} wins!')
            break
        player2.make_move(board_object)
        board_object.show_board()
        if board_object.check_wins():
            print(f'{player2.name} wins!')
            break


if __name__ == '__main__':
    board_object = Board()
    player1 = Player('Player 1', 'X')
    player2 = Player('computer', 'O')
    play(player1, player2, board_object)
