import asyncio
import websockets

async def handle_connection(websocket, path):
    async for message in websocket:
        print(f"Mensagem recebida do cliente: {message}")
        response = f"{message}"
        await websocket.send(response)

async def start_server():
    server = await websockets.serve(handle_connection, "localhost", 8081)
    print("Servidor WebSocket iniciado na porta 8081 com sucesso!")
    await server.wait_closed()

asyncio.run(start_server())
