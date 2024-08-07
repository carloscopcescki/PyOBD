from commands import Command

pid = input("Digite o número do PID: ")
        
command = Command(pid)

host= '192.168.0.10'
port = 35000

command.connection(host, port)
