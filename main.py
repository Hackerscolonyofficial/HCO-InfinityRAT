from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# === Obfuscated Access Key ===
ascii_key = [72, 67, 79, 45, 75, 69, 89, 45, 56, 52, 50, 48, 54, 49, 49, 49, 53, 57]
ACCESS_KEY = ''.join(chr(c) for c in ascii_key)
authenticated_clients = set()

# === Login Page ===
login_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>HCO-InfinityRAT 🔐</title>
    <link rel="icon" href="https://i.imgur.com/Vh3Yh4B.png">
    <style>
        body {
            background-color: #000;
            color: #00FF00;
            font-family: monospace;
            text-align: center;
            padding-top: 100px;
        }
        h2 {
            font-size: 28px;
        }
        form {
            margin-top: 30px;
        }
        input[type=password], input[type=submit] {
            padding: 14px;
            font-size: 18px;
            border: none;
            margin: 8px;
            border-radius: 8px;
            background: #111;
            color: #00FF00;
        }
        input[type=submit] {
            background-color: #00cc66;
            color: #fff;
            font-weight: bold;
            cursor: pointer;
        }
        p {
            margin-top: 20px;
            color: #ccc;
        }
        b {
            color: #FF0066;
        }
    </style>
</head>
<body>
    <h2>🔐 ACCESS PANEL - HCO INFINITY RAT</h2>
    <form method="POST">
        <input type="password" name="key" placeholder="🔑 Enter Access Key" required><br>
        <input type="submit" value="🚪 UNLOCK TOOL">
    </form>
    <p>📩 Send DM to <b>@HackersColony</b> on Telegram or WhatsApp <b>+91 8420611159</b> to get your key.</p>
</body>
</html>
'''

# === Dashboard Page ===
panel_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>HCO-InfinityRAT Panel</title>
    <link rel="icon" href="https://i.imgur.com/Vh3Yh4B.png">
    <style>
        body {
            background-color: #000000;
            background-image: url('https://i.imgur.com/wK3qkiL.jpeg');
            background-size: cover;
            background-position: center;
            color: #00FF00;
            font-family: monospace;
            text-align: center;
            padding-top: 40px;
        }
        h1 {
            font-size: 36px;
            background-color: rgba(0,0,0,0.7);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            color: #00FF00;
            border: 2px dashed #00ff00;
        }
        .button {
            display: inline-block;
            padding: 16px 28px;
            margin: 12px;
            font-size: 20px;
            font-weight: bold;
            color: #00FF00;
            background-color: rgba(0,0,0,0.6);
            border: 2px solid #00FF00;
            border-radius: 8px;
            text-decoration: none;
        }
        .button:hover {
            background-color: rgba(0,255,0,0.1);
        }
    </style>
</head>
<body>
    <h1>💀 HCO INFINITY RAT CONTROL PANEL 💀</h1>
    <a class="button" href="/gps">📍 GPS</a>
    <a class="button" href="/webcam">📷 Front Cam</a>
    <a class="button" href="/webcam?cam=back">🎥 Back Cam</a>
    <a class="button" href="/files">📁 Files</a>
    <a class="button" href="/calls">📞 Calls</a>
    <a class="button" href="/sms">💬 SMS</a>
    <a class="button" href="/logout">🚪 Logout</a>
</body>
</html>
'''

# === Routes ===
@app.route("/", methods=["GET", "POST"])
def home():
    ip = request.remote_addr
    if request.method == "POST":
        key = request.form.get("key")
        if key == ACCESS_KEY:
            authenticated_clients.add(ip)
        else:
            return "<h3 style='color:red;'>❌ Invalid Access Key</h3><p>Ask @HackersColony for access.</p>"
    if ip not in authenticated_clients:
        return login_html
    return panel_html

@app.route("/logout")
def logout():
    authenticated_clients.discard(request.remote_addr)
    return "<h3>👋 Logged out</h3><a href='/'>Login again</a>"

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
    cam = request.args.get("cam", "front")
    return f"<h3>📸 {cam.capitalize()} Camera Frame (Simulated)</h3>"

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    files = ["Download/", "DCIM/", "Android/", "secret_passwords.txt"]
    return "<h4>📁 Files:</h4><pre>" + "\n".join(files) + "</pre>"

@app.route("/calls")
def calls():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    logs = [
        "📞 +918888000111 - Incoming - 2 min",
        "📞 +917777000222 - Missed",
        "📞 +919999000333 - Outgoing - 5 min"
    ]
    return "<h4>📞 Call Logs:</h4><pre>" + "\n".join(logs) + "</pre>"

@app.route("/sms")
def sms():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    messages = [
        "💬 [Bank] ₹1,000 credited.",
        "💬 [Mom] Where are you?",
        "💬 [Amazon] Delivery arriving today."
    ]
    return "<h4>💬 SMS Inbox:</h4><pre>" + "\n".join(messages) + "</pre>"

# === Run Server ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
