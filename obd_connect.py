from commands import *
import streamlit as st

# Definindo host e porta
host= '192.168.0.10'
port = 35000

# Criando a page
st.set_page_config(
    page_title="OBD Reader",
)
st.sidebar.empty()
st.sidebar.title("OBD Reader")
st.sidebar.write("Aplicativo para monitorar dados do veículo em tempo real")

pid_dict = []
pid = st.sidebar.selectbox('Selecione o PID', [''] + pid_list())
if pid == '':
    st.warning("Escolha um parâmetro de serviço")
else:
    command = Command(pid)  
    st.sidebar.button('Conectar', on_click=command.connection(host, port))