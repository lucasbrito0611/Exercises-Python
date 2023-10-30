import streamlit as st
import time


class AbrirContaUI:
    def Main():
        st.title('Cadastro de Contas')

        nome = st.text_input('Informe o nome: ')
        email = st.text_input('Informe o e-mail: ')
        senha = st.text_input('Informe a senha: ')

        if st.button('Cadastrar'):
            st.success('Conta cadastrada')
            time.sleep(1)
            st.rerun()