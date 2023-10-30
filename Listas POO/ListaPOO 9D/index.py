import streamlit as st
from templates.clienteUI import ClienteUI
from templates.servicoUI import ServicoUI
from templates.agendaUI import AgendaUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.abrircontaUI import AbrirContaUI

class IndexUI:
  def sidebar():
    op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda", "Abrir Agenda do Dia", "Confirmar Agendamento", "Abrir Conta"])
    if op == "Manter Clientes": st.session_state["page"] = "clienteUI"
    if op == "Manter Serviços": st.session_state["page"] = "servicoUI"
    if op == "Manter Agenda": st.session_state["page"] = "agendaUI"
    if op == "Abrir Agenda do Dia": st.session_state["page"] = "abriragendaUI"
    if op == "Abrir Conta": st.session_state["page"] = "abrircontaUI"

  def main():
    IndexUI.sidebar()
    if "page" not in st.session_state: st.session_state["page"] = "clienteUI"
    if st.session_state["page"] == "clienteUI": ClienteUI.Main()
    if st.session_state["page"] == "servicoUI": ServicoUI.Main()
    if st.session_state["page"] == "agendaUI": AgendaUI.Main()
    if st.session_state["page"] == "abriragendaUI": AbrirAgendaUI.Main()
    if st.session_state["page"] == "abrircontaUI": AbrirContaUI.Main()

IndexUI.main()