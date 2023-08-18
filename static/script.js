document.addEventListener("DOMContentLoaded", function() {
    const conversationDiv = document.getElementById("conversation");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    sendButton.addEventListener("click", function() {
        const userMessage = userInput.value;
        if (userMessage.trim() !== "") {
            addMessage("You", userMessage);
            fetchResponse(userMessage);
            userInput.value = "";
        }
    });

    function addMessage(sender, message) {
        const messageDiv = document.createElement("div");
        messageDiv.className = "message";
        messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
        conversationDiv.appendChild(messageDiv);
        conversationDiv.scrollTop = conversationDiv.scrollHeight;
    }

    function fetchResponse(userMessage) {
        fetch("/generate", {
            method: "POST",
            body: JSON.stringify({ "seed_word": userMessage }),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            const generatedText = data.generated_text;
            addMessage("LLM", generatedText);
        })
        .catch(error => console.error("Error:", error));
    }
});
