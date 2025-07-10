from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ===== Access Key (Obfuscated) =====
KEY_CHARS = [72, 67, 79, 45, 75, 69, 89, 45, 56, 52, 50, 48, 54, 49, 49, 49, 53, 57]
ACCESS_KEY = ''.join([chr(c) for c in KEY_CHARS])
authenticated_clients = set()

# ===== HTML Templates =====
login_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>HCO-InfinityRAT Login</title>
    <style>
        body {{
            background-color: black;
            color: #00ff00;
            font-family: monospace;
            text-align: center;
            padding-top: 80px;
        }}
        input {{
            padding: 8px;
            background: #111;
            color: #0f0;
            border: 1px solid #0f0;
        }}
        .btn {{
            padding: 10px 20px;
            background: #0f0;
            color: black;
            border: none;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <h2>🔐 Enter Access Key</h2>
    <form method="POST">
        <input type="password" name="key" placeholder="Access Key" required>
        <br><br>
        <input type="submit" value="Unlock" class="btn">
    </form>
    <p>📩 DM <b>@HackersColony</b> on Telegram or WhatsApp <b>+91 8420611159</b> to get your key.</p>
</body>
</html>
'''

panel_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>HCO-InfinityRAT Dashboard</title>
    <style>
        body {{
            background: url("https://i.imgur.com/6Xd2UeK.jpg") no-repeat center center fixed;
            background-size: cover;
            font-family: monospace;
            color: #00ff00;
            text-align: center;
            padding-top: 80px;
        }}
        h1 {{
            background-color: rgba(0, 0, 0, 0.7);
            display: inline-block;
            padding: 10px 30px;
            border-radius: 10px;
        }}
        .btn {{
            display: inline-block;
            margin: 10px;
            padding: 15px 30px;
            background-color: rgba(0, 255, 0, 0.2);
            color: #0f0;
            border: 1px solid #0f0;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        }}
        .btn:hover {{
            background-color: #0f0;
            color: black;
        }}
    </style>
</head>
<body>
    <h1>☣️ Hackers Colony - InfinityRAT Control Panel ☣️</h1><br><br>
    <a href="/gps" class="btn">📍 GPS Location</a>
    <a href="/webcam" class="btn">📷 Capture Webcam</a>
    <a href="/files" class="btn">📁 File Browser</a>
    <a href="/calls" class="btn">📞 Call Logs</a>
    <a href="/sms" class="btn">💬 Read SMS</a>
    <a href="/camera/front" class="btn">📸 Front Cam</a>
    <a href="/camera/back" class="btn">🎥 Back Cam</a>
</body>
</html>
'''

# ===== Routes =====
@app.route("/", methods=["GET", "POST"])
def home():
    ip = request.remote_addr
    if request.method == "POST":
        key = request.form.get("key")
        if key == ACCESS_KEY:
            authenticated_clients.add(ip)
        else:
            return "<h3 style='color:red;'>❌ Invalid Key</h3><p>Contact @HackersColony for access.</p>"
    if ip not in authenticated_clients:
        return login_html
    return panel_html

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
    return "<h3>📷 Webcam capture simulated here</h3>"

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return "<h3>📁 File list simulated: /Download, /DCIM, /WhatsApp</h3>"

@app.route("/calls")
def calls():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return "<pre>📞 +918888000111 - Incoming\n📞 +917777000222 - Missed\n📞 +919999000333 - Outgoing</pre>"

@app.route("/sms")
def sms():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return "<pre>💬 'OTP is 123456'\n💬 'Recharge successful'</pre>"

@app.route("/camera/<side>")
def camera(side):
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return f"<h3>📷 Capturing from {side} camera (simulated)</h3>"

# ===== Run =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
