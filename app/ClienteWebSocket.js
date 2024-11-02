let clients = [ 
    new WebSocket('ws://localhost:8080'),
    new WebSocket('ws://localhost:8080')
]

clients.map(client => {
    client.on('message', msg => console.log(msg))
})

await new Promisse(resolve => clients[0].once('open', resolve))

clients[0].send('Hello!')