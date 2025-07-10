from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ===== Access Key System =====
ACCESS_KEY = "HCO-KEY-8420611159"
authenticated_ips = set()

# ===== Dashboard Template =====
dashboard_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>HCO-InfinityRAT Panel</title>
    <style>
        body {{
            background: url("https://raw.githubusercontent.com/Hackerscolonyofficial/HCO-InfinityRAT/main/assets/hco_bg.jpg") no-repeat center center fixed;
            background-size: cover;
            color: #00FF00;
            font-family: monospace;
            text-align: center;
            padding-top: 50px;
        }}
        h1 {{
            font-size: 36px;
            background-color: rgba(0, 0, 0, 0.7);
            padding: 15px;
            border-radius: 10px;
            display: inline-block;
        }}
        .btn {{
            display: inline-block;
            margin: 15px;
            padding: 14px 24px;
            background-color: black;
            border: 2px solid #00FF00;
            color: #00FF00;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
        }}
        .btn:hover {{
            background-color: #00FF00;
            color: black;
        }}
    </style>
</head>
<body>
    <h1>🚀 HCO-InfinityRAT Control Panel</h1><br><br>
    <a href="/gps" class="btn">📍 Location</a>
    <a href="/sms" class="btn">💬 SMS</a>
    <a href="/calls" class="btn">📞 Call Logs</a>
    <a href="/files" class="btn">📁 Files</a>
    <a href="/cam_front" class="btn">📷 Front Camera</a>
    <a href="/cam_back" class="btn">🎥 Back Camera</a>
    <br><br><a href="/logout" class="btn">🚪 Logout</a>
</body>
</html>
'''

# ===== Login Page Template =====
login_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Access Panel</title>
    <style>
        body {{
            background-color: black;
            color: #00FF00;
            font-family: monospace;
            text-align: center;
            padding-top: 100px;
        }}
        input {{
            padding: 10px;
            margin: 10px;
            border-radius: 5px;
            border: 1px solid #00FF00;
            background: transparent;
            color: #00FF00;
        }}
        .submit {{
            background-color: #00FF00;
            color: black;
            font-weight: bold;
        }}
        p {{
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <h2>🔐 Enter Access Key</h2>
    <form method="POST">
        <input type="password" name="key" placeholder="Access Key" required>
        <br>
        <input class="submit" type="submit" value="Unlock">
    </form>
    <p>📩 DM <b>@HackersColony</b> on Telegram or WhatsApp <b>+91 8420611159</b> to get your key.</p>
</body>
</html>
'''

# ===== Routes =====
@app.route("/", methods=["GET", "POST"])
def home():
    ip = request.remote_addr
    if ip not in authenticated_ips:
        if request.method == "POST":
            key = request.form.get("key")
            if key == ACCESS_KEY:
                authenticated_ips.add(ip)
            else:
                return "<h3>❌ Invalid Key</h3><p>DM @HackersColony for valid access.</p>"
        else:
            return login_html
    return dashboard_html

@app.route("/logout")
def logout():
    ip = request.remote_addr
    authenticated_ips.discard(ip)
    return "<h3>✅ Logged out. <a href='/'>Login again</a></h3>"

@app.route("/gps")
def gps():
    if request.remote_addr not in authenticated_ips:
        return "❌ Unauthorized"
    return jsonify({
        "lat": "28.7041",
        "lon": "77.1025",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/sms")
def sms():
    if request.remote_addr not in authenticated_ips:
        return "❌ Unauthorized"
    messages = [
        "📩 +918888000111: Hello there!",
        "📩 +917777000222: Your OTP is 4321",
        "📩 +919999000333: Call me asap."
    ]
    return "<pre>" + "\n".join(messages) + "</pre>"

@app.route("/calls")
def calls():
    if request.remote_addr not in authenticated_ips:
        return "❌ Unauthorized"
    logs = [
        "📞 +918888000111 - Incoming - 2 min",
        "📞 +917777000222 - Missed",
        "📞 +919999000333 - Outgoing - 5 min"
    ]
    return "<pre>" + "\n".join(logs) + "</pre>"

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_ips:
        return "❌ Unauthorized"
    fake_files = ["📁 Download/", "📁 Pictures/", "📁 Android/", "📄 secret.txt"]
    return "<pre>" + "\n".join(fake_files) + "</pre>"

@app.route("/cam_front")
def cam_front():
    if request.remote_addr not in authenticated_ips:
        return "❌ Unauthorized"
    return "<h3>📷 Front camera image will appear here (simulated)</h3>"

@app.route("/cam_back")
def cam_back():
    if request.remote_addr not in authenticated_ips:
        return "❌ Unauthorized"
    return "<h3>🎥 Back camera image will appear here (simulated)</h3>"

# ===== Run Server =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
