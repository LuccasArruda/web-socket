let ipConexao = window.prompt("Digite o IP de conexão: ")

const ws = new WebSocket(`ws://${ipConexao}:8081`);

ws.onopen = () => {
    console.log("Conectado ao servidor WebSocket");
};

ws.onmessage = (event) => {
    const chatLog = document.getElementById("chatLog");
    const message = document.createElement("div");
    
    message.textContent = "Desconhecido: " + event.data;
    message.classList.add("server");
    chatLog.appendChild(message);

    chatLog.scrollTop = chatLog.scrollHeight;
};

function sendMessage() {
    const input = document.getElementById("messageInput");
    const message = input.value;
    if (message.trim() !== "") {
        ws.send(message);

        const chatLog = document.getElementById("chatLog");
        const userMessage = document.createElement("div");
        userMessage.textContent = `${message}`;
        userMessage.classList.add("client"); 
        chatLog.appendChild(userMessage);

        input.value = "";
        chatLog.scrollTop = chatLog.scrollHeight;
    }
}

document.getElementById('messageInput').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
});
