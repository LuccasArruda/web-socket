import socket
import sys
import re
import websockets

SERVER_PORT = 8000  # Porta constante do servidor
BUFFER = 1024

def connecting():
    value = input("Digite o endereço IP para iniciar a comunicação: ")
    confirmation = input(f"\nO destino é: {value}. Está correto?\n0-Não\n1-Sim\n")
    confirmation = (False if int(confirmation) == 0 else True)
    if not confirmation:
        print("Saindo...")
        sys.exit()
    return start_connection(value)

def checking_ip_address(ip_address):
    # Validação do endereço IP com regex
    if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip_address):
        return True
    print("Programa finalizado... Verifique se o endereço IP está correto.")
    sys.exit()

def close_connection(tcp_connection):
    print("Finalizando a conexão TCP...")
    tcp_connection.close()

def start_connection(ip_address):
    print("Tentando conectar ao servidor...")
    checking_ip_address(ip_address)
    tcp_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        destiny = (ip_address, SERVER_PORT)
        tcp_connection.connect(destiny)
        print("Conectado ao servidor com sucesso!")
    except ConnectionError as error:
        print("Conexão recusada. Tente novamente!\n"
              f"Tipo de erro: {type(error)}")
        sys.exit()
    return tcp_connection

def conversation(tcp_connection):
    print("Iniciando o chat!\nObs: Para sair da conversa, digite: exit")

    while True:
        try:
            message = input("Você: ")

            if message:
                tcp_connection.send(bytes(message, "utf8"))
                if message.lower() == 'exit':
                    print("Saindo da conversa...")
                    break
            
            recv_message = tcp_connection.recv(BUFFER).decode("utf-8")
            if recv_message:
                print(f"Servidor: {recv_message}")
                if recv_message.lower() == 'exit':
                    print("O servidor encerrou a conexão.")
                    break
        except ConnectionError:
            print("Conexão encerrada inesperadamente.")
            break

    close_connection(tcp_connection)

if __name__ == '__main__':
    print("Bem-vindo ao chat com comunicação via socket!\n")
    connection = connecting()
    conversation(connection)
    try:
        connection.close()
    except ConnectionError:
        print("A conexão TCP foi encerrada.")
