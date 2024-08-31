from typing import Optional
import streamlit as st
from src.tic_tac_toe import Board, Player

#Utility functions

# Initialize session state dictionary to manage game state
def init_sesson_state() -> None:
    session_state_dict: dict[str, Optional[Board]] = {
        'Board': Board(),
        'turn': None,
        'board': None,
        'player_1': None,
        'player_2': None,
        'game_session': None,
        'winner': None,
        'tie': None,
        'message': None,
        }
    for sess_stat, init_sees_stat in session_state_dict.items():
        if sess_stat not in st.session_state:
            st.session_state[sess_stat] = init_sees_stat

def init_board() -> None:
    st.session_state.Board = Board()

def switch_turn() -> None:
    if st.session_state['turn'] == st.session_state['player_1']:
        st.session_state['turn'] = st.session_state['player_2']
    else:
        st.session_state['turn'] = st.session_state['player_1']

def check_wins_tie() -> None:
    if board_object.check_wins() and st.session_state['winner'] is None:
        st.session_state['winner'] = st.session_state['turn'].name
    elif board_object.check_tie():
        st.session_state['tie'] = True

def play(cell) -> None:
    st.session_state['turn'].make_move(board_object, cell)
    check_wins_tie()
    switch_turn()

init_sesson_state()
board_object: Board = st.session_state['Board']
board_object.run_state = 'streamlit'
st.session_state['board'] = board_object.board
st.session_state['message'] = board_object.message

#Streamlit showcase

st.image('images/tictactoe.png')



col = st.columns([0.2, 0.2, 0.4, 0.2, 0.2])
player1_name = col[2].text_input("Player 1's name: ", key='player1')
if player1_name and st.session_state['player_1'] is None:
    st.session_state['player_1'] = Player(player1_name, 'X')
    st.session_state['turn'] = st.session_state['player_1']

player2_name = col[2].text_input("Player 2's name: ", key='player2')
if player2_name and st.session_state['player_2'] is None:
    st.session_state['player_2'] = Player(player2_name, 'O')

col = st.columns([0.2, 0.2, 0.4, 0.2, 0.2])
if col[2].button('Start'):
    st.session_state['game_session'] = True
if st.session_state['game_session']:
    col[2].write(f"{st.session_state['turn'].name}'s turn: {st.session_state['turn'].symbol}")

# Loop through each cell in the board and create buttons for user interaction
col = st.columns([0.7, 0.2, 0.2, 0.2, 0.7])
for i, j in enumerate(st.session_state['board'], start=1):
    if i % 3 == 1:
        col[1].button(j, key=f'col1{i}', on_click=play, args=(i,))
    elif i % 3 == 2:
        col[2].button(j, key=f'col1{i}', on_click=play, args=(i,))
    else:
        col[3].button(j, key=f'col1{i}', on_click=play, args=(i, ))

col = st.columns([0.2, 0.2, 0.4, 0.2, 0.2])
if st.session_state['winner'] is not None:
    col[2].success(f"{st.session_state['winner']} wins!")
    st.balloons()

col = st.columns([0.2, 0.2, 0.4, 0.2, 0.2])
if st.session_state['tie'] is not None:
    col[2].error("It's a tie! Try again")

col = st.columns([0.2, 0.2, 0.4, 0.2, 0.2])
if st.session_state['Board'].message is not None:
    col[2].error(st.session_state['Board'].message)
    st.session_state['Board'].message = None
    switch_turn()

col = st.columns([0.7, 0.2, 0.4, 0.2, 0.7])
if col[2].button('Play Again'):
    init_board()
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
