import streamlit as st
import pandas as pd
import time
from views import Views

class AgendaUI:
    def Main():
        st.title('Cadastro de Horários')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])

        with tab1:
            AgendaUI.Listar()
        with tab2:
            AgendaUI.Inserir()
        with tab3:
            AgendaUI.Atualizar()
        with tab4:
            AgendaUI.Excluir()

    @classmethod
    def Listar(cls):
        lista = []

        for agenda in Views.agenda_listar():
            lista.append(agenda.to_json())

        df = pd.DataFrame(lista)

        st.dataframe(df)

    @classmethod
    def Inserir(cls):
        data = st.text_input('Informe a data e horário:')
        idCliente = st.text_input('Informe o id do Cliente:')
        idServico = st.text_input('Informe o id do Serviço:')
        confirmado = False

        if st.button('Inserir'):
            Views.agenda_inserir(data, confirmado, idCliente, idServico)
            st.success('Agenda inserida com sucesso')
            time.sleep(1)
            st.experimental_rerun()

    @classmethod
    def Atualizar(cls):
        opcao = st.selectbox(
            'Atualização de agendas',
            (Views.agenda_listar()),
            index=None,
            placeholder='Selecione uma agenda'
        )
        if opcao:
            id = opcao.get_id()

        data = st.text_input('Informe a nova data e horário:')
        idCliente = st.text_input('Informe o novo id do Cliente:')
        idServico = st.text_input('Informe o novo id do Serviço:')
        confirmado = False

        if st.button('Atualizar'):
            Views.agenda_atualizar(id, data, confirmado, idCliente, idServico)
            st.success('Agenda atualizada com sucesso')
            time.sleep(1)
            st.experimental_rerun()

    @classmethod
    def Excluir(cls):
        opcao = st.selectbox(
            'Exclusão de agendas',
            (Views.agenda_listar()),
            index=None,
            placeholder='Selecione uma agenda'
        )
        if opcao:
            id = opcao.get_id()

        if st.button('Excluir'):
            Views.agenda_excluir(id)
            st.success('Agenda excluída com sucesso')
            time.sleep(1)
            st.experimental_rerun()