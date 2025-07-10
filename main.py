from flask import Flask, request, render_template_string, jsonify
from datetime import datetime
from dotenv import load_dotenv
import os

# ===== Load Access Key from .env =====
load_dotenv()
ACCESS_KEY = os.getenv("HCO_ACCESS_KEY", "")
authenticated_clients = set()

app = Flask(__name__)

# ===== TEMPLATES =====
login_html = '''
<head><title>HCO-InfinityRAT</title><link rel="icon" href="https://i.imgur.com/Vh3Yh4B.png"></head>
<h2>🔐 Enter Access Key</h2>
<form method="POST">
    <input type="password" name="key" placeholder="Access Key" required>
    <input type="submit" value="Unlock">
</form>
<p>📩 DM <b>@HackersColony</b> on Telegram or WhatsApp <b>+91 8420611159</b> to get your key.</p>
'''

panel_html = '''
<h1>✅ Welcome to HCO-InfinityRAT Control Panel</h1>
<ul>
    <li><a href="/gps">📍 GPS Location</a></li>
    <li><a href="/webcam">📷 Capture Webcam</a></li>
    <li><a href="/files">📁 File Browser</a></li>
    <li><a href="/calls">📞 Call Logs</a></li>
    <li><a href="/logout">🚪 Logout</a></li>
</ul>
'''

# ===== ROUTES =====
@app.route("/", methods=["GET", "POST"])
def home():
    client_ip = request.remote_addr
    if request.method == "POST":
        key = request.form.get("key")
        if key == ACCESS_KEY:
            authenticated_clients.add(client_ip)
            log_login(client_ip)
        else:
            return "<h3>❌ Invalid Key</h3><p>Ask @HackersColony on Telegram for a valid access key.</p>"

    if client_ip not in authenticated_clients:
        return login_html

    return panel_html

@app.route("/logout")
def logout():
    client_ip = request.remote_addr
    authenticated_clients.discard(client_ip)
    return "<h3>👋 Logged out.</h3><a href='/'>Back to login</a>"

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
    return "<h3>📷 Webcam image will be shown here (simulation)</h3>"

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    fake_files = ["Download/", "Pictures/", "Android/", "secret.txt"]
    return "<h4>📁 File List:</h4><pre>" + "\n".join(fake_files) + "</pre>"

@app.route("/calls")
def calls():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    call_logs = [
        "📞 +918888000111 - Incoming - 2 min",
        "📞 +917777000222 - Missed",
        "📞 +919999000333 - Outgoing - 5 min"
    ]
    return "<h4>📞 Call Logs:</h4><pre>" + "\n".join(call_logs) + "</pre>"

# ===== Logger =====
def log_login(ip):
    with open("access_log.txt", "a") as log:
        log.write(f"[{datetime.now()}] Access granted to IP: {ip}\n")

# ===== MAIN =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
