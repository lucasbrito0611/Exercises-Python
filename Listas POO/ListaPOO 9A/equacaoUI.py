import streamlit as st
from equacao import Equacao
from retangulo import Retangulo
import pandas as pd

class EquacaoUI:
    def main():
        st.title('Equação do II Grau: y = ax**2 + bx + c')

        a = st.text_input('A:')
        b = st.text_input('B:')
        c = st.text_input('C:')

        if st.button('Calcular'):
            e = Equacao(float(a), float(b), float(c))
            
            st.write(f'Delta = {e.Delta()}')
            st.write(f'Tem raíz real? {e.TemRaizesReais()}')
            st.write(f'Raízes = {e.Raiz1()} e {e.Raiz2()}')

            px = []
            py = []

            for x in range(-100, 101):
                px.append(x)
                py.append((e.GetA()*(x**2)) + (e.GetB() * x) + e.GetC()) 

            chart_data = pd.DataFrame(
                {
                    "col1": px,
                    "col2": py
                }
            )

            st.line_chart(chart_data, x="col1", y="col2")