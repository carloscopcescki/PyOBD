from commands import ObdPid
from commands import Frontpage
from commands import *
import streamlit as st
import json

# Chamando webpage
page = Frontpage()
page.set_page()

# Definindo host e porta
host= '192.168.0.10'
port = 35000

# Coletar param
data = open('./pid.json')
pid_desc = json.load(data)

pid = st.sidebar.selectbox('Selecione o PID', [''] + pid_list())
if pid == '':
    st.warning("Escolha um parâmetro de serviço")
else:
    st.sidebar.write(f"Descrição: {pid_desc[pid]}")

pid = ObdPid(pid)  
if st.sidebar.button("Conectar"):
    pid.connection(host, port)
    
st.sidebar.info("Veja mais sobre OBD-2 e PID em: https://www.csselectronics.com/pages/obd2-pid-table-on-board-diagnostics-j1979")