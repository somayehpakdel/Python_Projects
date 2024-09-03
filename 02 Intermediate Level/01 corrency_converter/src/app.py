import time

import streamlit as st
from src.CONSTANTS import CURRENCY_CODES
from src.currency_converter import (convert_currency, get_exchange_rate,
                                    humanize_time)

st.title(':dollar: Currency Converter')
st.markdown("""This app allows you to convert currency from one type to another.""")

col = st.columns(3)
base_currency = col[0].selectbox('From Currency', CURRENCY_CODES, index=CURRENCY_CODES.index('USD'))
target_currency = col[0].selectbox('To Currency', CURRENCY_CODES, index=CURRENCY_CODES.index('IRR'))
amount = col[0].number_input('Amount to Convert', value=0.0, min_value=0.0)

if amount > 0 and base_currency and target_currency:
    exchange_rate, time_last_updated = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        time_last_updated = humanize_time(time_last_updated)
        converted_amount = convert_currency(amount, exchange_rate)
        col[0].success(f'✅ {converted_amount:.2f} {target_currency}')
        col[0].markdown(f'✅ Last updated: {time_last_updated}')
        col1, col2, col3 = st.columns(3)
        col1.metric('Base Currency', f'{amount:.2f} {base_currency}')
        col2.markdown("<h1 style='text-align: center;color:green ; margin: 0;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric('Converted Amount', f'{converted_amount:.2f} {target_currency}')
    else:
        st.error('Failed to retrieve exchange rate. Please try again later.')


st.markdown('---')
st.markdown(r'### \* About this tool')
st.markdown("""
    - This tool allows you to convert currency from one type to another. 
    - It uses the latest exchange rates to perform the conversion.""")
