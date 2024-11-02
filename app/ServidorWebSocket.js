const WebSocket = require('ws')
const server = new WebSocket.server({
    port: 8080
})

let sockets = []
server.on('connection', function(socket){
    sockets.push(socket)
    socket.on('message', function(mgs){
        sockets.forEach(s => s.send(msg))
    })

    socket.on('close', function(){
        sockets = sockets.filter(s => s !== socket)
    })
})