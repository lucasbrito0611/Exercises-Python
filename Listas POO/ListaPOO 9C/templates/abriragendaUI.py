import streamlit as st
import time
from views import Views

class AbrirAgendaUI:
    def Main():
        st.title('Abrir Agenda do Dia')

        data = st.text_input('Informe a data no formato dd/mm/aaaa')
        hora_ini = st.text_input('Informe o horário inicial no formato HH:MM')
        hora_fin = st.text_input('Informe o horário final no formato HH:MM')
        contador = st.text_input('Informe o intervalo entre os horários no formato HH:MM')

        if st.button('Inserir horários'):
            Views.abrir_agenda_do_dia(data, hora_ini, hora_fin, contador)
            st.success('Horários inseridos com sucesso')
            time.sleep(1)
            st.experimental_rerun()