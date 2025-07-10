from flask import Flask, request, render_template_string, jsonify
from datetime import datetime

app = Flask(__name__)

# ===== ACCESS KEY SYSTEM =====
ACCESS_KEY = "HCO-KEY-8420611159"
authenticated_clients = set()

# ===== HTML DASHBOARD =====
login_html = '''
<head><title>HCO-InfinityRAT</title></head>
<h2>🔐 Enter Access Key</h2>
<form method="POST">
    <input type="password" name="key" placeholder="Access Key" required>
    <input type="submit" value="Unlock">
</form>
<p>📩 DM <b>@HackersColony</b> on Telegram or WhatsApp <b>+91 8420611159</b> to get your key.</p>
'''

panel_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>HCO-InfinityRAT Panel</title>
    <style>
        body {
            background-image: url('https://i.imgur.com/Vh3Yh4B.png');
            background-size: cover;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 20px;
        }
        .button {
            display: inline-block;
            padding: 15px 25px;
            margin: 10px;
            font-size: 16px;
            font-weight: bold;
            color: white;
            background-color: #333;
            border: none;
            border-radius: 8px;
            text-decoration: none;
        }
        .button:hover {
            background-color: #555;
        }
    </style>
</head>
<body>
    <h1>🚀 HCO-InfinityRAT Control Panel</h1>
    <a class="button" href="/gps">📍 GPS Location</a>
    <a class="button" href="/webcam">📷 Front Camera</a>
    <a class="button" href="/webcam?cam=back">🎥 Back Camera</a>
    <a class="button" href="/files">📁 File Browser</a>
    <a class="button" href="/calls">📞 Call Logs</a>
    <a class="button" href="/sms">💬 SMS Inbox</a>
    <a class="button" href="/logout">🚪 Logout</a>
</body>
</html>
'''

# ===== ROUTES =====
@app.route("/", methods=["GET", "POST"])
def home():
    client_ip = request.remote_addr
    if request.method == "POST":
        key = request.form.get("key")
        if key == ACCESS_KEY:
            authenticated_clients.add(client_ip)
        else:
            return "<h3>❌ Invalid Key</h3><p>Ask @HackersColony on Telegram for your access key.</p>"
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
    cam_type = request.args.get("cam", "front")
    return f"<h3>📷 {cam_type.capitalize()} Camera image shown here (simulation)</h3>"

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    files = ["Download/", "DCIM/", "Android/", "WhatsApp/", "secret_notes.txt"]
    return "<h4>📁 File Browser:</h4><pre>" + "\n".join(files) + "</pre>"

@app.route("/calls")
def calls():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    calls = [
        "📞 +918888000111 - Incoming - 2 min",
        "📞 +917777000222 - Missed",
        "📞 +919999000333 - Outgoing - 5 min"
    ]
    return "<h4>📞 Call Logs:</h4><pre>" + "\n".join(calls) + "</pre>"

@app.route("/sms")
def sms():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    messages = [
        "💬 [Airtel] Recharge successful: ₹199",
        "💬 [Mom] Call me when you're free",
        "💬 [Bank] ₹5,000 credited to your A/C"
    ]
    return "<h4>💬 SMS Inbox:</h4><pre>" + "\n".join(messages) + "</pre>"

# ===== MAIN =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
