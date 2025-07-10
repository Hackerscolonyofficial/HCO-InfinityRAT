from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ===== Access Key (obfuscated with spaces, not visible in GitHub easily) =====
ACCESS_KEY = "H C O - K E Y - 8 4 2 0 6 1 1 1 5 9".replace(" ", "")
authenticated_clients = set()

# ===== HTML Templates =====
login_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>HCO-InfinityRAT - Access</title>
    <style>
        body { font-family: monospace; background-color: #000; color: #0f0; text-align: center; }
        input { padding: 10px; margin: 10px; font-size: 16px; }
        .msg { color: #0f0; font-size: 18px; }
    </style>
</head>
<body>
    <h2>🔐 Enter Access Key</h2>
    <form method="POST">
        <input type="password" name="key" placeholder="Access Key" required><br>
        <input type="submit" value="Unlock">
    </form>
    <p class="msg">📩 DM <b>@HackersColony</b> on Telegram or WhatsApp <b>+91 8420611159</b> to get your key.<br>
    🔔 Also Subscribe to our YouTube: <b>HackersColonyOfficial</b></p>
</body>
</html>
'''

panel_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>HCO-InfinityRAT Panel</title>
    <style>
        body {
            background-color: black;
            color: #00ff00;
            font-family: monospace;
            text-align: center;
            background-image: url('https://i.imgur.com/6M5132N.gif');
            background-size: cover;
            background-repeat: no-repeat;
        }
        h1 { margin-top: 20px; }
        ul { list-style: none; padding: 0; }
        li { margin: 10px 0; }
        a {
            color: #00ffcc;
            font-size: 18px;
            text-decoration: none;
            border: 1px solid #00ffcc;
            padding: 10px 20px;
            border-radius: 8px;
            background-color: rgba(0,0,0,0.6);
        }
        a:hover { background-color: rgba(0,255,255,0.2); }
        img { width: 120px; border-radius: 10px; margin-top: 10px; }
    </style>
</head>
<body>
    <img src="https://i.imgur.com/Vh3Yh4B.png" alt="HCO Logo">
    <h1>💀 Hackers Colony Infinity RAT 💀</h1>
    <ul>
        <li><a href="/gps">📍 GPS Location</a></li>
        <li><a href="/webcam">📷 Capture Webcam</a></li>
        <li><a href="/files">📁 File Browser</a></li>
        <li><a href="/calls">📞 Call Logs</a></li>
        <li><a href="/logout">🚪 Logout</a></li>
    </ul>
</body>
</html>
'''

# ===== Routes =====
@app.route("/", methods=["GET", "POST"])
def home():
    client_ip = request.remote_addr
    if request.method == "POST":
        key = request.form.get("key")
        if key == ACCESS_KEY:
            authenticated_clients.add(client_ip)
        else:
            return "<h3 style='color:red;'>❌ Invalid Access Key</h3><p>Please DM @HackersColony on Telegram to get a valid key.</p>"

    if client_ip not in authenticated_clients:
        return login_html

    return panel_html

@app.route("/logout")
def logout():
    client_ip = request.remote_addr
    authenticated_clients.discard(client_ip)
    return "<h3>👋 Logged out. <a href='/'>Login again</a></h3>"

@app.route("/gps")
def gps():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return jsonify({
        "lat": "28.7041",
        "lon": "77.1025",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/webcam")
def webcam():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return "<h3>📷 Webcam snapshot would appear here (simulated)</h3>"

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    files = ["Download/", "DCIM/", "Android/", "Notes.txt", "secret_folder/"]
    return "<h4>📁 File Explorer:</h4><pre>" + "\n".join(files) + "</pre>"

@app.route("/calls")
def calls():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    logs = [
        "📞 +919876543210 - Incoming - 2m",
        "📞 +911234567890 - Outgoing - 5m",
        "📞 +918888000111 - Missed Call"
    ]
    return "<h4>📞 Call Logs:</h4><pre>" + "\n".join(logs) + "</pre>"

# ===== Start App =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
