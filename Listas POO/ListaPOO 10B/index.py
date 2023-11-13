from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manteragendaUI import ManterAgendaUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.loginUI import LoginUI
from templates.agendahojeUI import AgendaHojeUI
from templates.servicoreajusteUI import ServicoReajusteUI
from templates.abrircontaUI import AbrirContaUI
from views import View

import streamlit as st

class IndexUI:
    def sidebar():
      if "cliente_id" not in st.session_state:
        op = st.sidebar.selectbox("Menu", ["Login", "Abrir conta no Sistema"])
        if op == "Login": LoginUI.main()
        if op == "Abrir conta no Sistema": AbrirContaUI.main()
      else:
          st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
          if st.session_state["cliente_nome"] != "admin":
            op1 = st.sidebar.selectbox("Menu", ["Agenda do Dia"])
            if op1 == "Agenda do Dia": AgendaHojeUI.main()
          else:
            op2 = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda", "Abrir Agenda do Dia", "Agenda de Hoje", "Reajuste de Preço"])
            if op2 == "Manter Clientes": ManterClienteUI.main()
            if op2 == "Manter Serviços": ManterServicoUI.main()
            if op2 == "Manter Agenda": ManterAgendaUI.main()
            if op2 == "Abrir Agenda do Dia": AbrirAgendaUI.main()
            if op2 == "Agenda de Hoje": AgendaHojeUI.main()
            if op2 == "Reajuste de Preço": ServicoReajusteUI.main()

    def main():
      View.cliente_admin()
      IndexUI.sidebar()

IndexUI.main()



