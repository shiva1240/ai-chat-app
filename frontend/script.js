const API_URL = "http://127.0.0.1:8000";

let username = "";

const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const loading = document.getElementById("loading");


function login() {

    username = document.getElementById("username").value;

    if (!username) return;

    document.getElementById("login-screen").style.display = "none";
    document.getElementById("chat-screen").style.display = "block";

    loadHistory();
}


async function sendMessage() {

    const message = input.value;

    if (!message) return;

    addMessage(message, "user");

    input.value = "";

    loading.style.display = "block";

    const response = await fetch(`${API_URL}/chat`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            username: username,
            message: message
        })

    });

    const data = await response.json();

    addMessage(data.ai_response, "ai");

    loading.style.display = "none";
}


function addMessage(text, sender) {

    const div = document.createElement("div");

    div.classList.add("message", sender);

    div.innerText = text;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}


async function clearHistory() {

    await fetch(
        `${API_URL}/history/${username}`,
        { method: "DELETE" }
    );

    chatBox.innerHTML = "";
}


async function loadHistory() {

    const response = await fetch(
        `${API_URL}/history/${username}`
    );

    const data = await response.json();

    data.forEach(chat => {

        addMessage(chat.user_message, "user");
        addMessage(chat.ai_response, "ai");

    });

}