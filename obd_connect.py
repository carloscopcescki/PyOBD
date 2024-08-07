from commands import *
import streamlit as st
import json

# Definindo host e porta
host= '192.168.0.10'
port = 35000


data = open('./pid.json')
pid_desc = json.load(data)

# Criando a page
st.set_page_config(
    page_title="OBD Reader",
    page_icon=":car:",
)
st.sidebar.empty()
st.sidebar.title("OBD Reader")
st.sidebar.write("Aplicativo para monitorar dados do veículo em tempo real")

pid = st.sidebar.selectbox('Selecione o PID', [''] + pid_list())
if pid == '':
    st.warning("Escolha um parâmetro de serviço")
else:
    st.sidebar.write(f"Descrição: {pid_desc[pid]}")

command = Command(pid)  

if st.sidebar.button("Conectar"):
    command.connection(host, port)