import socket
import sys

SERVER_IP = ''  # Endereço IP do servidor, em branco para aceitar conexões de qualquer IP
SERVER_PORT = 8000  # Porta de conexão
BUFFER = 1024  # Buffer de recepção para mensagens

def bind_to_the_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reutilizar a porta rapidamente
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)
    print("Servidor aguardando conexão...")
    return server_socket

def client_confirmation(server_socket):
    connection, client_address = server_socket.accept()
    print(f"\nO cliente com o IP {client_address[0]} conectou-se.\n")
    return connection, client_address

def close_connection(connection):
    print("Finalizando a conexão TCP...")
    connection.close()

def listening(connection, client_address):
    print("Iniciando o chat. Aguardando mensagem...\nObs: Para sair da conversa, digite: exit")

    while True:
        try:
            recv_message = connection.recv(BUFFER).decode("utf-8")

            if recv_message:
                print(f"Cliente ({client_address[0]}): {recv_message}")
                if recv_message.lower() == 'exit':
                    print("O cliente encerrou a conexão.")
                    break

            sending_message = input("Você: ")
            if sending_message:
                connection.send(bytes(sending_message, "utf8"))
                if sending_message.lower() == 'exit':
                    print("Encerrando a conexão...")
                    break
        except ConnectionError:
            print("Cliente desconectado inesperadamente.")
            break

    close_connection(connection)

if __name__ == '__main__':
    server_socket = bind_to_the_server()
    connection, client_address = client_confirmation(server_socket)
    listening(connection, client_address)
    server_socket.close()
    sys.exit()
