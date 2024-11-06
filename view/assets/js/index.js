    const ws = new WebSocket("ws://localhost:8081");
    let nomeDoCabra       
    ws.onopen = () => {
        console.log("Conectado ao servidor WebSocket");
        nomeDoCabra = window.prompt("Digite seu nome:")
        console.log(nomeDoCabra)
    };

    ws.onmessage = (event) => {
        const chatLog = document.getElementById("chatLog");
        const message = document.createElement("div");
        message.textContent = "Servidor " + event.data;
        chatLog.appendChild(message);
    };

    ws.onclose = () => {
        console.log("Conexão fechada com o servidor WebSocket");
    };

    function sendMessage() {
        const input = document.getElementById("messageInput");
        const message = input.value;
        ws.send(message);

        const chatLog = document.getElementById("chatLog");
        const userMessage = document.createElement("div");
        userMessage.textContent = `${nomeDoCabra}: ${message}`
        chatLog.appendChild(userMessage);

        input.value = "";
    }

    document.getElementById('messageInput').addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault(); 
            sendMessage();
        }
    });
