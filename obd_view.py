from commands import ObdPid
from commands import Page
import streamlit as st
import json

# Calling webpage
page = Page()
page.set_page()

# Colect params
data = open('./pid.json')
pid_desc = json.load(data)
pid = st.sidebar.selectbox('Selecione o PID', [''] + page.pid_list())

# Create buttons (test and obd connection)
if st.sidebar.button("Conectar"):
    if pid == '':
        st.warning("Escolha um parâmetro de serviço")
    else:
        pid = ObdPid(pid)
        host = '192.168.0.10'
        port = 35000
        pid.connection(host, port)
if st.sidebar.button("Teste"):
    if pid == '':
        st.warning("Escolha um parâmetro de serviço")
    else:
        pid_test = ObdPid(pid)
        pid_test.scanner_test(pid, pid_desc[pid])