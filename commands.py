import socket
import json
import streamlit as st
from time import time
import time
import random

class ObdPid:
    def __init__(self, pid) -> None:
        '''Inicialize OBD connection'''
        self.pid = pid
    
    def connection(self, host, port):
        '''Create connection with OBD scanner'''
        data = open('./pid.json')
        read_json = json.load(data)
        self.host = host
        self.port = port
        ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            ser.settimeout(10)
            ser.connect((self.host, self.port))
            ser.sendall(bytes.fromhex(self.pid))
            self.response = ser.recv(1024)
            st.write(f"Resposta: {self.response}")
            st.write(f"\nDescrição do comando: {read_json.get(self.pid)}")
        except TimeoutError:
            st.warning("Erro ao realizar a conexão com OBD.")
        except Exception as e:
            st.warning(f"Erro: {e}")
        finally:
            ser.close()

    def hex_list(self):
        '''Generate Hex List'''
        values = []
        count = 1
        while count <= 100:
            values.append(hex(count))
            count += 1
        return values

    def scanner_test(self, pid_number, description):
        '''OBD scanner test'''
        self.pid_number = pid_number
        self.description = description
        now = time.time()
        time_loop = 30
        stop = st.sidebar.button("Parar")
        st.write(f"PID selecionado: {self.pid_number}")
        st.write(f"Descrição: {self.description}")
        
        while(time.time() - now < time_loop):
            pid_response = random.choice(ObdPid.hex_list(self))
            st.write(f'Resposta: {int(pid_response, 16)} Km/h')
            time.sleep(1)
            if stop:
                break
        
class Page():
    def __init__(self) -> None:
        '''Create web interface'''
        pass
    
    def set_page(self):
        '''Customize webpage'''
        st.set_page_config(
        page_title="OBD Reader",
        page_icon=":car:",
        )
        st.sidebar.empty()
        st.sidebar.title("OBD Reader")
        st.sidebar.write("Aplicativo para monitorar dados do veículo em tempo real")
        st.sidebar.divider()
        
        st.subheader("Dados do veículo em tempo real")
        
    def pid_list(self):
        '''Extract PID list for json file'''
        pid_dict = []
        with open('./pid.json') as data:
            pids = json.load(data)
            for pid in pids:
                pid_dict.append(pid)
        return pid_dict
    
    
        

        