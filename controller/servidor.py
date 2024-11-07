import asyncio
import websockets

connected_clients = set()

async def handle_connection(websocket, path):
    connected_clients.add(websocket)
    client_ip = websocket.remote_address[0]
    try:
        async for message in websocket:
            print(f"Mensagem recebida do cliente Desconhecido: {message}")
            for client in connected_clients:
                if client != websocket: 
                    await client.send(f"({client_ip}): {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Um cliente desconectou.")
    finally:
        connected_clients.remove(websocket)

async def start_server():
    server = await websockets.serve(handle_connection, "192.168.48.113", 8081)
    print("Servidor WebSocket iniciado na porta 8081 com sucesso!")
    await server.wait_closed()

asyncio.run(start_server())
