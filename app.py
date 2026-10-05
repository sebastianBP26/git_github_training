import streamlit as st

st.title("Conversor de temperatura")
print('Hola mundo')
celsius = st.number_input("Grados Celsius")
fahrenheit = celsius * 9 / 5 + 32
st.write(f'{celsius} °C son {fahrenheit} °F')