import socket
import json

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
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ser:
            ser.connect((self.host, self.port))
            try:
                ser.sendall(bytes.fromhex(self.pid))
                self.response = ser.recv(1024)
                print(f"Resposta: {self.response}")
                print(f"\nDescrição do comando: {read_json.get(self.pid)}")
                socket.close()
            except Exception as e:
                print(f"Erro: {e}")
                socket.close()
        