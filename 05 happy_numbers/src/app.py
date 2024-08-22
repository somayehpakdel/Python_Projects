import streamlit as st
import matplotlib.pyplot as plt
from src.happy_number import happy_numbers


st.image("images/happy_numbers.png")
number = st.number_input("Insert a Number and Press Enter", min_value=1, step=1)
happy, sequence_numbers = happy_numbers(number)
if happy:
    st.success(f"{number} is a happy number!", icon="✅")
else:
    st.error(f"{number} is not a happy number.", icon="🔥")


st.subheader("Sequence of Numbers:")

html_list = "<div style='display: flex; gap: 10px;'>"
for item in sequence_numbers:
    html_list += f"<div>{item}</div>"
html_list += "</div>"

# Display the HTML in Streamlit
st.markdown(html_list, unsafe_allow_html=True)

plt.figure(figsize=(10, 6))
plt.plot(sequence_numbers, marker='o')
plt.xlabel('Sequence')
plt.ylabel('Numbers')
plt.title('Sequence of Numbers')
st.pyplot(plt)