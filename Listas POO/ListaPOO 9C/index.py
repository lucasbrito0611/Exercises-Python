import streamlit as st
from templates.clienteUI import ClienteUI
from templates.servicoUI import ServicoUI
from templates.agendaUI import AgendaUI
from abriragendaUI import AbrirAgendaUI

class IndexUI:
    def sidebar():
        op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços",
                                        "Manter Agenda", "Abrir Agenda do Dia",
                                        "Confirmar Agendamento"])
        if op == "Manter Clientes": st.session_state["page"] = "ManterClienteUI"
        if op == "Manter Serviços": st.session_state["page"] = "ServicoUI"
        if op == "Manter Agenda": st.session_state["page"] = "AgendaUI"
        if op == "Abrir Agenda do Dia": st.session_state["page"] = "AbrirAgendaUI"


    def main():
        IndexUI.sidebar()
        if "page" not in st.session_state: st.session_state["page"] = "manter_clienteUI"
        if st.session_state["page"] == "ClienteUI": ClienteUI.Main()
        if st.session_state["page"] == "ServicoUI": ServicoUI.Main()
        if st.session_state["page"] == "AgendaUI": AgendaUI.Main()
        if st.session_state["page"] == "AbrirAgendaUI": AbrirAgendaUI.Main()

IndexUI.main()