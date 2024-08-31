# Tic Tac Toe Game

A simple Tic Tac Toe game built with Python using Streamlit for the user interface and pytest for testing. This project allows two players to play Tic Tac Toe in their web browser.

## Features

- Two-player game mode
- Interactive web interface using Streamlit
- Unit tests for game logic using pytest

<p align="center">
    <img src='./images/tictactoe_app.png' alt='happy_numbers', width=400>
</p>


## Game Rules

1. The game is played on a 3x3 grid.
2. Players take turns placing their marks (X or O) in empty squares.
3. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
4. If all squares are filled and no player has three in a row, the game is a tie.

## Installation

1. **Clone the repository:**

```bash
git clone (https://github.com/somayehpakdel/Python_Projects.git
cd '01 level I/08 tic_tac_toe'
```

2. **Install the required packages:**

```bash
   pip install -r requirements.txt
```

## Running the Game

To start the Tic Tac Toe game, run the following command:

```bash
streamlit run src/app.py
```
This will start a local web server and open the application in your default web browser.

## Running Tests

To run the unit tests, execute:

``` bash
pytest tests/test_tic_tac_toe.py
```
