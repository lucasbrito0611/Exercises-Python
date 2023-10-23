import streamlit as st
import pandas as pd
import time
from views import Views

class ServicoUI:
    def Main():
        st.title('Serviço')

        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1:
            ServicoUI.Listar()
        with tab2:
            ServicoUI.Inserir()
        with tab3:
            ServicoUI.Atualizar()
        with tab4:
            ServicoUI.Excluir()

    @classmethod
    def Listar(cls):
        data = []

        for servico in Views.servico_listar():
            id = servico.get_id()
            nome = servico.get_descricao()
            email = servico.get_valor()
            fone = servico.get_duracao()

            data.append([id, nome, email, fone])

        df = pd.DataFrame(data, columns=['Id', 'Descrição', 'Valor', 'Duração (min)'])

        st.dataframe(df)

    @classmethod
    def Inserir(cls):
        descricao = st.text_input('Descrição:')
        valor = st.text_input('Valor:')
        duracao = st.text_input('Duração (min):')

        if st.button('Inserir'):
            Views.servico_inserir(descricao, float(valor), duracao)
            st.success('Serviço inserido com sucesso')
            time.sleep(1)
            st.experimental_rerun()

    @classmethod
    def Atualizar(cls):
        opcao = st.selectbox(
            'Atualização de serviços',
            (Views.servico_listar()),
            index=None,
            placeholder='Selecione um serviço'
        )
        if opcao:
            id = opcao.get_id()

        descricao = st.text_input('Descrição nova:')
        valor = st.text_input('Valor novo:')
        duracao = st.text_input('Duração nova (min):')

        if st.button('Atualizar'):
            Views.servico_atualizar(id, descricao, float(valor), duracao)
            st.success('Serviço atualizado com sucesso')
            time.sleep(1)
            st.experimental_rerun()

    @classmethod
    def Excluir(cls):
        opcao = st.selectbox(
            'Exclusão de serviços',
            (Views.servico_listar()),
            index=None,
            placeholder='Selecione um serviço'
        )

        if opcao:
            id = opcao.get_id()

        if st.button('Excluir'):
            Views.servico_excluir(id)
            st.success('Serviço excluído com sucesso')
            time.sleep(1)
            st.experimental_rerun()