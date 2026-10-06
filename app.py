import streamlit as st

st.title("Conversor de temperatura")

modo = st.ratio("Convertir de: " ['Celsisus a Fahrenheit', 'Farenheit a Celsius'])
valor = st.number_input("Valor")

if modo == "Celsisus a Fahrenheit":
    resultado = valor * 9 / 5 + 32
    st.success(f"**{round(resultado, 2)} °F**")
    st.caption(f"{valor} °C convertidos a Fahrenheit")
else:
    resultado = valor * 9 / 5 + 32
    st.success(f"**{round(resultado, 2)} °F**")
    st.caption(f"{valor} °F convertidos a Celsius")