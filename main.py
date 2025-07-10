from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ASCII-obfuscated access key (HCO-KEY-8420611159)
ACCESS_KEY = ''.join([chr(c) for c in [72,67,79,45,75,69,89,45,56,52,50,48,54,49,49,49,53,57]])
authenticated_clients = set()

# Login HTML with hacker style
login_html = '''
<html>
<head>
    <title>HCO-InfinityRAT Login</title>
    <style>
        body {
            background-color: black;
            color: #00FF00;
            font-family: monospace;
            text-align: center;
            margin-top: 100px;
        }
        input[type=password], input[type=submit] {
            padding: 10px;
            margin: 10px;
            font-size: 16px;
        }
        .box {
            border: 2px solid #00FF00;
            display: inline-block;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.6);
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>🔐 ACCESS PANEL</h2>
        <form method="POST">
            <input type="password" name="key" placeholder="Enter Access Key" required><br>
            <input type="submit" value="Unlock">
        </form>
        <p>📩 DM <b>@HackersColony</b> or WhatsApp <b>+91 8420611159</b> for your key.</p>
    </div>
</body>
</html>
'''

# Panel HTML with working background image
panel_html = '''
<html>
<head>
    <title>HCO-InfinityRAT Dashboard</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-image: url("https://i.imgur.com/6Xd2UeK.jpg");
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

@app.route("/", methods=["GET", "POST"])
def home():
    ip = request.remote_addr
    if request.method == "POST":
        key = request.form.get("key")
        if key == ACCESS_KEY:
            authenticated_clients.add(ip)
        else:
            return "<h3 style='color:red;'>❌ Invalid Key</h3><p>DM @HackersColony for access</p>"

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
    return "<h3 style='color:#00FF00;'>📷 Webcam image would appear here</h3>"

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    fake_files = ["Download/", "DCIM/", "Pictures/", "secret.txt"]
    return "<h3>📁 File List:</h3><pre style='color:#00FF00;'>" + "\n".join(fake_files) + "</pre>"

@app.route("/calls")
def calls():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    logs = [
        "📞 +918888000111 - Incoming - 2 min",
        "📞 +917777000222 - Missed",
        "📞 +919999000333 - Outgoing - 5 min"
    ]
    return "<h3>📞 Call Logs:</h3><pre style='color:#00FF00;'>" + "\n".join(logs) + "</pre>"

@app.route("/sms")
def sms():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    messages = [
        "💬 +911234567890: 'OTP is 456789'",
        "💬 +919876543210: 'Hi where are you?'"
    ]
    return "<h3>💬 SMS Inbox:</h3><pre style='color:#00FF00;'>" + "\n".join(messages) + "</pre>"

@app.route("/camera")
def camera():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    cam = request.args.get("cam", "front")
    return f"<h3 style='color:#00FF00;'>📸 Capturing from {cam} camera... (Simulated)</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
