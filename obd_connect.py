from commands import Command
import socket
     
     
pid = input("Digite o número do PID: ")
desc = input("\nDigite a descrição do PID: ")
        
command = Command(pid, desc)

host= '192.168.0.10'
port = 35000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ser:
    ser.connect((host, port))
    try:
        ser.sendall(bytes.fromhex(command.pid))
        response = ser.recv(1024)
        print(f"Resposta: {response}")
        print(f"\nDescrição do comando: {command.desc}")
    except Exception as e:
        print(f"Erro: {e}")
        socket.close()
