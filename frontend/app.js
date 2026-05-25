const API_URL =
"https://web-production-eb849.up.railway.app/api/chat";

const chatContainer =
    document.getElementById(
        "chat-container"
    );

const input =
    document.getElementById(
        "user-input"
    );

const sendBtn =
    document.getElementById(
        "send-btn"
    );


let sessionId =
    localStorage.getItem(
        "sessionId"
    );

if (!sessionId) {

    sessionId =
        "session_" +
        Math.random()
        .toString(36)
        .substring(2, 12);

    localStorage.setItem(
        "sessionId",
        sessionId
    );
}


function addMessage(
    text,
    sender
) {

    const message =
        document.createElement("div");

    message.classList.add(
        sender === "user"
            ? "user-message"
            : "bot-message"
    );

 const time =
    new Date()
    .toLocaleTimeString(
        [],
        {
            hour: "2-digit",
            minute: "2-digit"
        }
    );

if (sender === "bot") {

    message.innerHTML =
    `
    ${marked.parse(text)}
    <div class="timestamp">
        ${time}
    </div>
    `;
}

else {

    message.innerHTML =
    `
    <span>${text}</span>
    <div class="timestamp">
        ${time}
    </div>
    `;
}

    chatContainer.appendChild(
        message
    );

        chatContainer.scrollTo({
    top:
        chatContainer.scrollHeight,

    behavior:
        "smooth"
    });
}


async function sendMessage() {

    const message =
        input.value.trim();

    if (!message) return;

    addMessage(
        message,
        "user"
    );

    input.value = "";

    input.focus();

    sendBtn.disabled = true;
    sendBtn.innerText = "Sending...";

    const loading =
        document.createElement("div");

    loading.classList.add(
        "bot-message",
        "loading-message"
    );

    loading.innerHTML =
    `
    <span class="thinking">
        Thinking
        <span class="dot">.</span>
        <span class="dot">.</span>
        <span class="dot">.</span>
    </span>
    `;

    chatContainer.appendChild(
        loading
    );

    chatContainer.scrollTo({
        top:
            chatContainer.scrollHeight,

        behavior:
            "smooth"
    });

    try {

        const response =
            await fetch(
                API_URL,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                    JSON.stringify({
                        sessionId,
                        message
                    })
                }
            );

        const data =
            await response.json();

        loading.remove();

        addMessage(
            data.reply,
            "bot"
        );

    } catch (error) {

        loading.remove();

        addMessage(
            "⚠️ Unable to connect to the server. Please try again.",
            "bot"
        );
    }

    sendBtn.disabled = false;
    sendBtn.innerText = "Send";

    input.focus();
}


sendBtn.addEventListener(
    "click",
    sendMessage
);

input.addEventListener(
    "keypress",
    function (event) {

        if (
            event.key === "Enter"
        ) {
            sendMessage();
        }
    }
);