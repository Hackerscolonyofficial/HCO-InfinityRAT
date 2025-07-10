from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
ACCESS_KEY = "HCO-KEY-8420611159"
authenticated_clients = set()

login_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>HCO-InfinityRAT Login</title>
    <style>
        body {
            background: linear-gradient(to right, #000000, #1c1c1c);
            color: #00ff00;
            font-family: monospace;
            text-align: center;
            padding-top: 100px;
        }
        input[type=password], input[type=submit] {
            padding: 10px;
            margin: 5px;
            background-color: #111;
            color: #0f0;
            border: 1px solid #0f0;
        }
    </style>
</head>
<body>
    <h1>🔐 Enter Access Key</h1>
    <form method="POST">
        <input type="password" name="key" placeholder="Access Key" required><br>
        <input type="submit" value="Unlock">
    </form>
    <p>📩 DM <b>@HackersColony</b> or WhatsApp <b>+91 8420611159</b> for your personal access key.</p>
</body>
</html>
'''

panel_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>HCO-InfinityRAT Dashboard</title>
    <style>
        body {
            background: linear-gradient(to right, #000000, #1a1a1a);
            color: #00ffcc;
            font-family: 'Courier New', monospace;
            text-align: center;
            padding-top: 60px;
        }
        h1 {
            color: #00ffcc;
            text-shadow: 0 0 5px #0ff;
        }
        .button {
            display: inline-block;
            margin: 20px;
            padding: 15px 30px;
            background-color: #111;
            border: 2px solid #00ffcc;
            color: #00ffcc;
            font-size: 18px;
            text-decoration: none;
            border-radius: 10px;
            box-shadow: 0 0 10px #00ffcc;
        }
    </style>
</head>
<body>
    <h1>💻 HCO-InfinityRAT Control Panel</h1>
    <a class="button" href="/gps">📍 GPS</a>
    <a class="button" href="/webcam">📷 Camera</a>
    <a class="button" href="/files">📁 Files</a>
    <a class="button" href="/calls">📞 Calls</a>
    <a class="button" href="/logout">🚪 Logout</a>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    client_ip = request.remote_addr
    if request.method == "POST":
        key = request.form.get("key")
        if key == ACCESS_KEY:
            authenticated_clients.add(client_ip)
        else:
            return "<h3 style='color:red'>❌ Invalid Key</h3><p>DM @HackersColony for access</p>"
    if client_ip not in authenticated_clients:
        return login_html
    return panel_html

@app.route("/logout")
def logout():
    authenticated_clients.discard(request.remote_addr)
    return "<h3>Logged out</h3><a href='/'>Login again</a>"

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
    return "<h3>📷 Webcam image (simulation)</h3>"

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return "<pre>📁 Files:\n- Download/\n- DCIM/\n- Android/\n- secret.txt</pre>"

@app.route("/calls")
def calls():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return "<pre>📞 Call Logs:\n- +91 9000000000 (Incoming)\n- +91 8000000000 (Missed)</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
