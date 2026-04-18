async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();

    if (!message) return;

    addMessage("user", message);
    input.value = "";

    try {
        const res = await fetch("https://chatbot-deploy-goi7.onrender.com/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await res.json();

        addMessage("bot", data.response);

    } catch (error) {
        addMessage("bot", "Error: " + error.message);
    }
}

function addMessage(sender, text) {
    const chatBox = document.getElementById("chatBox");

    const msg = document.createElement("div");
    msg.className = sender;

    msg.innerText = text;

    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}