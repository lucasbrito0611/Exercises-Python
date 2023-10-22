import streamlit as st
import pandas as pd
import time
from views import Views

class ClienteUI:
    def Main():
        st.title('Cadastro de clientes')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1:
            ClienteUI.Listar()
        with tab2:
            ClienteUI.Inserir()
        with tab3:
            ClienteUI.Atualizar()
        with tab4:
            ClienteUI.Excluir()

    @classmethod
    def Listar(cls):
        data = []

        for cliente in Views.cliente_listar():
            id = cliente.get_id()
            nome = cliente.get_nome()
            email = cliente.get_email()
            fone = cliente.get_fone()

            data.append([id, nome, email, fone])

        df = pd.DataFrame(data, columns=['Id', 'Nome', 'Email', 'Telefone'])

        st.dataframe(df)

    @classmethod
    def Inserir(cls):
        nome = st.text_input('Informe o nome: ')
        email = st.text_input('Informe o e-mail: ')
        fone = st.text_input('Informe o telefone: ')
        if st.button('Inserir'):
            Views.cliente_inserir(nome, email, fone)
            st.success('Cliente inserido com sucesso')
            time.sleep(1)
            st.experimental_rerun()

    @classmethod
    def Atualizar(cls):
        opcao = st.selectbox(
            'Atualização de clientes',
            (Views.cliente_listar()),
            index=None,
            placeholder='Selecione um cliente'
        )
        if opcao:
            id = opcao.get_id()

        nome = st.text_input('Nome novo: ')
        email = st.text_input('E-mail novo: ')
        fone = st.text_input('Telefone novo: ')

        if st.button('Atualizar'):
            Views.cliente_atualizar(id, nome, email, fone)
            st.success('Cliente atualizado com sucesso')
            time.sleep(1)
            st.experimental_rerun()

    @classmethod
    def Excluir(cls):
        opcao = st.selectbox(
            'Exclusão de clientes',
            (Views.cliente_listar()),
            index=None,
            placeholder='Selecione um cliente'
        )
        if opcao:
            id = opcao.get_id()

        if st.button('Excluir'):
            Views.cliente_excluir(id)
            st.success('Cliente excluído com sucesso')
            time.sleep(1)
            st.experimental_rerun()