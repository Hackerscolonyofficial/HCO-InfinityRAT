from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ===== Access Key =====
ACCESS_KEY = "HCO-KEY-8420611159"
authenticated_clients = set()

# ===== Dashboard HTML =====
panel_html = '''
<html>
<head>
    <title>HCO-InfinityRAT Dashboard</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-image: url("https://i.imgur.com/NQ3YhFb.jpg");
            background-size: cover;
            background-position: center;
            font-family: monospace;
            color: #00FF00;
        }
        .overlay {
            background-color: rgba(0,0,0,0.7);
            padding: 40px;
            margin: 50px auto;
            width: 70%;
            border-radius: 10px;
            box-shadow: 0 0 15px #00FF00;
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        .btn {
            display: block;
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            background-color: black;
            border: 2px solid #00FF00;
            color: #00FF00;
            font-size: 18px;
            text-align: center;
            text-decoration: none;
            transition: background 0.3s;
        }
        .btn:hover {
            background-color: #00FF00;
            color: black;
        }
    </style>
</head>
<body>
    <div class="overlay">
        <h1>💻 Hackers Colony Infinity RAT</h1>
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

# ===== Login Page HTML =====
login_html = '''
<html>
<head>
    <title>Enter Access Key</title>
    <style>
        body {
            background-color: black;
            color: #00FF00;
            font-family: monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        input {
            margin: 10px;
            padding: 10px;
            background: #111;
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
        <input type="password" name="key" placeholder="Access Key" required>
        <br>
        <input type="submit" value="Unlock Panel">
    </form>
    <p>📩 DM <b>@HackersColony</b> on Telegram or WhatsApp <b>+91 8420611159</b> to get your access key.</p>
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
            return "<h3 style='color:red;'>❌ Invalid Key</h3><p>Contact us for a valid access key.</p>"
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
    return "<h3 style='color:#00FF00;'>📷 Webcam image will appear here (simulated)</h3>"

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    files = ["Download/", "Pictures/", "Android/", "secret.txt"]
    return "<pre style='color:#00FF00;'>📁 File List:\n" + "\n".join(files) + "</pre>"

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
    return f"<h3 style='color:#00FF00;'>📸 {cam.title()} Camera image captured (simulated)</h3>"

# ===== Run Server =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
