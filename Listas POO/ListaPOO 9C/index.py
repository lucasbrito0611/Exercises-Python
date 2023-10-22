import streamlit as st
from clienteUI import ClienteUI
from servicoUI import ServicoUI
from agendaUI import AgendaUI
from abriragendaUI import AbrirAgendaUI

class IndexUI:
    def main():
        # ClienteUI.Main()
        # ServicoUI.Main()
        # AgendaUI.Main()   
        AbrirAgendaUI.Main()  

IndexUI.main()        