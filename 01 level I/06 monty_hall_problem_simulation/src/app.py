import time
import streamlit as st
from src.monty_hall import monty_hall_simulation


st.image("images/monty_hall_problem.png", width=500)
num_simulation = st.number_input("Number of simulations:", min_value=1, value=100, step=10, key="num_simulations")

col1, col2 = st.columns(2)

col1.subheader("Wins Percentage With Switching")
chart1 = col1.line_chart(x=None, y=None, width=0, height=400)

col2.subheader("Wins Percentage Without Switching")
chart2 = col2.line_chart(x=None, y=None, width=0, height=400)

wins_no_switch = 0
wins_switch = 0
for i in range(1, num_simulation):
    win_percentage_swiched, win_percentage_not_swiched  = monty_hall_simulation(1)

    wins_no_switch += win_percentage_not_swiched
    wins_switch += win_percentage_swiched

    chart1.add_rows([wins_no_switch / i])
    chart2.add_rows([wins_switch / i])

    # time.sleep(0.01)