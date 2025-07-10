from flask import Flask, request, render_template_string, jsonify
from datetime import datetime

app = Flask(__name__)

# ===== ACCESS KEY SYSTEM =====
ACCESS_KEY = "HCO-KEY-8420611159"
authenticated_clients = set()

# ===== TEMPLATES =====
login_html = '''
<head>
  <title>HCO-InfinityRAT Login</title>
  <style>
    body { background: #0f0f0f; color: white; font-family: Arial; text-align: center; padding-top: 100px; }
    input { padding: 10px; margin: 10px; }
    form { background: #1c1c1c; display: inline-block; padding: 20px; border-radius: 10px; }
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
'''

panel_html = '''
<head>
  <title>HCO-InfinityRAT Dashboard</title>
  <link rel="icon" href="https://i.imgur.com/Vh3Yh4B.png">
  <style>
    body {
      margin: 0; padding: 0;
      background: url('https://i.imgur.com/Vh3Yh4B.png') no-repeat center center fixed;
      background-size: cover;
      font-family: Arial, sans-serif;
      text-align: center;
      color: white;
    }
    .overlay {
      background-color: rgba(0, 0, 0, 0.8);
      padding: 50px 20px;
      min-height: 100vh;
    }
    h1 { margin-bottom: 40px; }
    .btn {
      display: inline-block;
      margin: 15px;
      padding: 15px 25px;
      font-size: 18px;
      border: none;
      border-radius: 10px;
      color: white;
      background-color: #1f1f1f;
      text-decoration: none;
      transition: background 0.3s;
    }
    .btn:hover { background-color: #333; }
  </style>
</head>
<body>
  <div class="overlay">
    <h1>🚀 Hackers Colony InfinityRAT</h1>
    <a class="btn" href="/gps">📍 GPS</a>
    <a class="btn" href="/files">📁 Files</a>
    <a class="btn" href="/calls">📞 Call Logs</a>
    <a class="btn" href="/sms">💬 SMS</a>
    <a class="btn" href="/webcam/front">📷 Front Cam</a>
    <a class="btn" href="/webcam/back">📷 Back Cam</a>
    <br><br>
    <a href="/logout" style="color:#ccc;">🚪 Logout</a>
  </div>
</body>
'''

# ===== ROUTES =====
@app.route("/", methods=["GET", "POST"])
def home():
    ip = request.remote_addr
    if request.method == "POST":
        if request.form.get("key") == ACCESS_KEY:
            authenticated_clients.add(ip)
        else:
            return "<h3>❌ Invalid Key</h3><p>Ask @HackersColony for a valid access key.</p>"
    if ip not in authenticated_clients:
        return login_html
    return panel_html

@app.route("/logout")
def logout():
    ip = request.remote_addr
    authenticated_clients.discard(ip)
    return "<h3>👋 Logged out. <a href='/'>Back to login</a></h3>"

@app.route("/gps")
def gps():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return jsonify({
        "lat": "28.6139",
        "lon": "77.2090",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/files")
def files():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    files = ["📁 /Download", "📁 /DCIM", "📄 secret_notes.txt"]
    return "<h4>📁 File List:</h4><pre>" + "\n".join(files) + "</pre>"

@app.route("/calls")
def calls():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    logs = ["📞 +91 9999999999 - Incoming", "📞 +91 8888888888 - Outgoing"]
    return "<h4>📞 Call Logs:</h4><pre>" + "\n".join(logs) + "</pre>"

@app.route("/sms")
def sms():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    messages = ["💬 +91 9876543210: Hi", "💬 +91 1234567890: Send me the code"]
    return "<h4>💬 SMS Logs:</h4><pre>" + "\n".join(messages) + "</pre>"

@app.route("/webcam/front")
def front_cam():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return "<h3>📷 Front Camera Image (simulated)</h3>"

@app.route("/webcam/back")
def back_cam():
    if request.remote_addr not in authenticated_clients:
        return "❌ Unauthorized"
    return "<h3>📷 Back Camera Image (simulated)</h3>"

# ===== MAIN =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=22533)
