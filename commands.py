import socket
import json
import streamlit as st

def pid_list():
    '''Obter PID's e descrições'''
    pid_dict = []
    with open('./pid.json') as data:
        pids = json.load(data)
        for pid in pids:
            pid_dict.append(pid)
    return pid_dict

class Frontpage:
    def __init__(self) -> None:
        pass
    
    def set_page(self):
        '''Criando o front'''
        st.set_page_config(
        page_title="OBD Reader",
        page_icon=":car:",
        )
        # Barra lateral
        st.sidebar.empty()
        st.sidebar.title("Sobre")
        st.sidebar.write("Aplicativo para monitorar dados do veículo em tempo real")
        # Página principal
        st.title("OBD Reader")
        st.subheader("Dados do veículo em tempo real")

class Command:
    def __init__(self, pid) -> None:
        '''Inicializa a classe PID Command - pid = 0100 (comando PID)'''
        self.pid = pid
    
    def connection(self, host, port):
        '''Estabelece a conexão com o OBD Scanner'''
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
                
        
