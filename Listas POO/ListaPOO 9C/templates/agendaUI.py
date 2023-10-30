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
        tabela = []

        for agenda in Views.agenda_listar():

            id = agenda.get_id()
            data = agenda.get_data()
            conf = agenda.get_confirmado()
            idCliente = int(agenda.get_idCliente())
            idServico = int(agenda.get_idServico())

            if idCliente != 0 and idServico != 0:
                clientes = Views.cliente_listar()
                for cliente in clientes:
                    if idCliente == cliente.get_id():
                        idCliente = cliente.get_nome()

                servicos = Views.servico_listar()
                for servico in servicos:
                    if idServico == servico.get_id():
                        idServico = servico.get_descricao()

            tabela.append([id, data, conf, idCliente, idServico])

        df = pd.DataFrame(tabela, columns=['Id', 'Data', 'Confirmado', 'idCliente', 'idServico'])

        st.dataframe(df, use_container_width=True)

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
            st.rerun()

    @classmethod
    def Atualizar(cls):
        data = ''
        idCliente = ''
        idServico = ''

        opcao = st.selectbox(
            'Atualização de agendas',
            (Views.agenda_listar()),
            index=None,
            placeholder='Selecione uma agenda'
        )
        if opcao:
            id = opcao.get_id()
            data = opcao.get_data()
            idCliente = opcao.get_idCliente()
            idServico = opcao.get_idServico()

        data = st.text_input('Informe a nova data e horário:', data)
        idCliente = st.text_input('Informe o novo id do Cliente:', idCliente)
        idServico = st.text_input('Informe o novo id do Serviço:', idServico)
        confirmado = False

        if st.button('Atualizar'):
            Views.agenda_atualizar(id, data, confirmado, idCliente, idServico)
            st.success('Agenda atualizada com sucesso')
            time.sleep(1)
            st.rerun()

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
            st.rerun()