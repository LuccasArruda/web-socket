import asyncio
import websockets

# Lista para armazenar os clientes conectados
connected_clients = set()

async def handle_connection(websocket, path):
    # Adiciona o cliente na lista de conectados
    connected_clients.add(websocket)
    client_ip = websocket.remote_address[0]
    try:
        async for message in websocket:
            print(f"Mensagem recebida do cliente {client_ip}: {message}")
            # Envia a mensagem para todos os clientes conectados
            for client in connected_clients:
                if client != websocket:  # Evita enviar a mensagem de volta para o remetente
                    await client.send(f"{client_ip} {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Um cliente desconectou.")
    finally:
        # Remove o cliente da lista ao desconectar
        connected_clients.remove(websocket)

async def start_server():
    server = await websockets.serve(handle_connection, "localhost", 8081)
    print("Servidor WebSocket iniciado na porta 8081 com sucesso!")
    await server.wait_closed()

asyncio.run(start_server())
