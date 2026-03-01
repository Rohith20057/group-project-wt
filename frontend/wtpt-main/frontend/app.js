const API_BASE_URL = "http://127.0.0.1:8000";

/* REGISTER */
async function register() {
    let email = regEmail.value;
    let password = regPassword.value;
    let message = regMsg;

    let emailPattern = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;
    let strongPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{6,}$/;

    if (!emailPattern.test(email)) {
        message.innerText = "Email must end with @gmail.com";
        return;
    }

    if (!strongPassword.test(password)) {
        message.innerText = "Password must be 6+ chars with uppercase, lowercase & number";
        return;
    }

    try {
        let response = await fetch(`${API_BASE_URL}/register`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        let data = await response.json();

        if (response.ok) {
            message.innerText = "Registration Successful!";
        } else {
            message.innerText = data.detail || "Registration Failed!";
        }
    } catch (error) {
        console.error(error);
        message.innerText = "Server error!";
    }
}

/* LOGIN */
async function login() {
    let email = loginEmail.value;
    let password = loginPassword.value;

    try {
        let response = await fetch(`${API_BASE_URL}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        let data = await response.json();

        if (response.ok) {
            sessionStorage.setItem("user_id", data.user_id);
            window.location.href = "dashboard.html";
        } else {
            loginMsg.innerText = data.detail || "Wrong email or password!";
        }
    } catch (error) {
        console.error(error);
        loginMsg.innerText = "Server error!";
    }
}

/* LOGOUT */
function logout() {
    sessionStorage.removeItem("user_id");
    window.location.href = "login.html";
}

/* NAVIGATION */
function goHistory() { window.location.href = "history.html"; }
function backDashboard() { window.location.href = "dashboard.html"; }

/* SHOW/HIDE PASSWORD */
function togglePassword() {
    regPassword.type = regPassword.type === "password" ? "text" : "password";
}

/* EXPLAIN */
async function explain() {
    let code = codeBox.value.trim();
    let lang = language.value;

    if (!code) {
        explainResult.innerText = "Enter code first.";
        return;
    }

    let user_id = sessionStorage.getItem("user_id");
    if (!user_id) {
        explainResult.innerText = "You must be logged in.";
        return;
    }

    explainResult.innerText = "Analyzing...";

    try {
        let response = await fetch(`${API_BASE_URL}/explain`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id: user_id, code: code, language: lang })
        });

        let data = await response.json();

        if (response.ok) {
            let output = "Explanations:\n" + data.explanation.join("\n") + "\n\n";
            if (data.errors && data.errors.length > 0) {
                output += "Errors:\n" + data.errors.join("\n") + "\n\n";
            }
            if (data.suggestions && data.suggestions.length > 0) {
                output += "Suggestions:\n" + data.suggestions.join("\n") + "\n";
            }
            explainResult.innerText = output;

            errorResult.innerText = data.errors && data.errors.length > 0 ? "Errors found in code. See explanation box." : "No basic errors found.";

        } else {
            explainResult.innerText = data.detail || "Failed to analyze code.";
        }
    } catch (error) {
        console.error(error);
        explainResult.innerText = "Server error while communicating with backend.";
    }
}

/* ERROR CHECK (local static check) */
function checkErrors() {
    let lines = codeBox.value.split("\n");
    let errorMsg = "";

    lines.forEach((line, i) => {
        if (line.includes(";;")) {
            errorMsg += "Error at line " + (i + 1) + ": Double semicolon (;;)\n";
        }
    });

    if (!errorMsg) errorMsg = "No basic errors found.";
    errorResult.innerText = errorMsg;
}

/* LOAD HISTORY */
if (document.getElementById("historyContainer")) {
    loadHistory();
}

async function loadHistory() {
    let user_id = sessionStorage.getItem("user_id");
    if (!user_id) {
        window.location.href = "login.html";
        return;
    }

    try {
        let response = await fetch(`${API_BASE_URL}/history/${user_id}`);
        let history = await response.json();

        let historyContainer = document.getElementById("historyContainer");
        historyContainer.innerHTML = ""; // Clear existing

        if (Array.isArray(history)) {
            history.forEach(item => {
                let div = document.createElement("div");
                div.className = "history-card";

                let explHtml = "";
                if (item.explanation) {
                    explHtml = item.explanation.join("<br>");
                }

                div.innerHTML = `
                    <h3>Code (ID: ${item._id.substring(0, 8)}...)</h3>
                    <p>${new Date(item.created_at).toLocaleString()}</p>
                    <pre>${item.code}</pre>
                    <pre>${explHtml}</pre>
                `;
                historyContainer.appendChild(div);
            });
        }
    } catch (error) {
        console.error(error);
    }
}

function searchHistory() {
    let keyword = searchInput.value.toLowerCase();
    let cards = document.querySelectorAll(".history-card");

    cards.forEach(card => {
        card.style.display =
            card.innerText.toLowerCase().includes(keyword)
                ? "block" : "none";
    });
}

async function clearAllHistory() {
    let user_id = sessionStorage.getItem("user_id");
    if (!user_id) return;

    if (!confirm("Are you sure you want to clear all history?")) return;

    try {
        let response = await fetch(`${API_BASE_URL}/history/${user_id}`, {
            method: "DELETE"
        });

        if (response.ok) {
            document.getElementById("historyContainer").innerHTML = "";
            alert("History cleared!");
        } else {
            alert("Failed to clear history.");
        }
    } catch (error) {
        console.error(error);
        alert("Server error.");
    }
}