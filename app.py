import streamlit as st

st.title("Conversor de temperatura")

modo = st.ratio("Convertir de: " ['Celsisus a Fahrenheit', 'Farenheit a Celsius'])
valor = st.number_input("Valor")

if modo == "Celsisus a Fahrenheit":
    resultado = valor * 9 / 5 + 32
    st.write(f'{valor} °C son {round(resultado, 2)} °F')
else:
    resultado = (valor - 32) * 5 / 9
    st.write(f'')