from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ===== Access Key =====
ACCESS_KEY = "HCO-KEY-8420611159"
authenticated_clients = set()

# ===== Login Page =====
login_html = '''
<html>
<head>
    <title>Access Key Required</title>
    <style>
        body {
            background-color: #000;
            color: #00FF00;
            font-family: monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        input {
            padding: 10px;
            margin: 10px;
            background-color: #111;
            border: 1px solid #00FF00;
            color: #00FF00;
        }
        input[type="submit"] {
            cursor: pointer;
        }
        h2 {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h2>🔐 Enter Access Key</h2>
    <form method="POST">
        <input type="password" name="key" placeholder="Access Key" required><br>
        <input type="submit" value="Unlock">
    </form>
    <p>📩 DM <b>@HackersColony</b> on Telegram or WhatsApp <b>+91 8420611159</b> to get your key.</p>
</body>
</html>
'''

# ===== Control Panel =====
panel_html = '''
<html>
<head>
    <title>HCO-InfinityRAT Dashboard</title>
    <style>
        body {
            background-color: #000000;
            color: #00FF00;
            font-family: monospace;
        }
        .container {
            margin: 50px auto;
            padding: 40px;
            width: 80%;
            background-color: #111111;
            border: 2px solid #00FF00;
            border-radius: 10px;
            box-shadow: 0 0 10px #00FF00;
        }
        h1 {
            text-align: center;
            color: #00FF00;
        }
        .btn {
            display: block;
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            background-color: #000;
            color: #00FF00;
            border: 1px solid #00FF00;
            text-align: center;
            font-size: 16px;
            text-decoration: none;
        }
        .btn:hover {
            background-color: #00FF00;
            color: #000;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>💀 HCO-InfinityRAT Control Panel</h1>
        <a class="btn" href="/gps">📍 GPS Location</a>
        <a class="btn" href="/webcam">📷 Capture Webcam</a>
        <a class="btn" href="/files">📁 File Browser</a>
        <a class="btn" href="/calls">📞 Call Logs</a>
        <a class="btn" href="/sms">💬 SMS Inbox</a>
        <a class="btn" href="/camera?cam=front">📸 Front Camera</a>
        <a class="btn" href="/camera?cam=back">📸 Back Camera</a>
    </div>
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
            return "<h3 style='color:red;'>❌ Invalid Key</h3><p>Contact us for access.</p>"
    if ip not in authenticated_clients:
        return login_html
    return panel_html

@app.route("/gps")
def gps():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return jsonify({"lat": "28.7041", "lon": "77.1025", "time": datetime.now().isoformat()})

@app.route("/webcam")
def webcam():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return "<pre style='color:#00FF00;'>📷 Webcam capture (simulated)</pre>"

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    files = ["Download/", "Pictures/", "DCIM/", "secret.txt"]
    return "<pre style='color:#00FF00;'>📁 Files:\n" + "\n".join(files) + "</pre>"

@app.route("/calls")
def calls():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    logs = [
        "📞 +918888000111 - Incoming - 2 min",
        "📞 +917777000222 - Missed",
        "📞 +919999000333 - Outgoing - 5 min"
    ]
    return "<pre style='color:#00FF00;'>📞 Call Logs:\n" + "\n".join(logs) + "</pre>"

@app.route("/sms")
def sms():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    sms_list = [
        "💬 +918765432100: Your OTP is 123456",
        "💬 Bank: ₹5000 credited to A/C xxxx1234",
        "💬 +911234567890: Meet me at 5 PM"
    ]
    return "<pre style='color:#00FF00;'>📩 SMS Inbox:\n" + "\n".join(sms_list) + "</pre>"

@app.route("/camera")
def camera():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    cam = request.args.get("cam", "front")
    return f"<pre style='color:#00FF00;'>📸 {cam.title()} Camera image captured (simulated)</pre>"

# ===== Start Server =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
