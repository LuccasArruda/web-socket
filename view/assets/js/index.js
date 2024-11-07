const ws = new WebSocket("ws://localhost:8081");

ws.onopen = () => {
    console.log("Conectado ao servidor WebSocket");
};

ws.onmessage = (event) => {
    const chatLog = document.getElementById("chatLog");
    const message = document.createElement("div");
    message.textContent = "Servidor: " + event.data;
    message.classList.add("server"); // Adiciona a classe 'server' para estilizar
    chatLog.appendChild(message);

    // Scroll para a última mensagem
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
        userMessage.classList.add("client"); // Adiciona a classe 'client' para estilizar
        chatLog.appendChild(userMessage);

        input.value = ""; // Limpa o campo de entrada
        chatLog.scrollTop = chatLog.scrollHeight; // Scroll automático para o final
    }
}

// Envio com Enter
document.getElementById('messageInput').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
});
