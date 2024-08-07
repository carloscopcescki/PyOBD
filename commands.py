import socket
import json
import streamlit as st

def pid_list():
    pid_dict = []
    with open('./pid.json') as data:
        pids = json.load(data)
        for pid in pids:
            pid_dict.append(pid)
    return pid_dict

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
                
        