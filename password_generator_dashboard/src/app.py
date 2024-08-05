import streamlit as st
from nltk.corpus import words
from src.main_oop import (MemorablePasswordGenerator, PinCodeGenerator,
                        RandomPasswordGenerator)

st.image("images/banner.png")
st.title(":zap: Password Generator")

option = st.radio('**Password Type:**', ('Pin Code', 'Random Password', 'Memorable Password'))

if option == 'Pin Code':
    length = st.slider('Length', min_value=4, max_value=20, value=5)

    generator = PinCodeGenerator(length)

elif option == 'Random Password':
    length = st.slider('Length', min_value=4, max_value=15, value=10)
    include_numbers = st.toggle('Include Numbers', value=False)
    includ_symbols = st.toggle('Include Symbols', value=False)

    generator = RandomPasswordGenerator(length, include_numbers=include_numbers, include_symbols=includ_symbols)

else:
    num_of_words = st.slider('Number of Words', min_value=2, max_value=10, value=5)
    separator = st.text_input('Separator', value='-')

    generator = MemorablePasswordGenerator(num_of_words=num_of_words, separator=separator, vocabulary=words.words())

password = generator.generate_password()
entropy = generator.calculate_entropy()

st.markdown('**Your password is:**')
st.header(f' ```{password}```')
st.markdown(f'**Entropy: {entropy:.2f}**')

if entropy < 28:
    st.write('Weak')
    st.image('images/weak.png', width=350)

elif 28 <= entropy <= 35:
    st.write('Moderate')
    st.image('images/moderate.png', width=350)

elif 35 < entropy <= 59 :
    st.write('Strong')
    st.image('images/strong.png', width=350)

elif 59 < entropy <= 80:
    st.write('Very Strong')
    st.image('images/very_strong.png', width=350)

else:
    st.write('Extremely Strong')
    st.image('images/extremely_strong.png', width=350)
