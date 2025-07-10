# HCO-InfinityRAT-Final

📱 Follow Hackers Colony Official:  
🔗 [GitHub](https://github.com/Hackerscolonyofficial) • [YouTube](https://www.youtube.com/@HackersColonyOfficial) • [Instagram](https://www.instagram.com/hackers_colony_official) • [Telegram](https://t.me/hackersColony) • [Discord](https://discord.gg/Xpq9nCGD)

---

**HCO-InfinityRAT** is a Termux-based Remote Access Trojan (RAT) by Azhar, created for educational and ethical testing only.

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

Update Termux and install dependencies:
pkg update && pkg upgrade -y
pkg install python git openjdk-17 apktool -y
pip install flask

Build the APK:
python apk_builder.py

The generated APK will be saved at:
output/HCO-InfinityRAT.apk

Install it on the target device manually for testing.

---

## 🧠 Using the Tool

1. Start the control server:
python main.py

2. Open your browser and visit:
http://localhost:22533

3. Use the web control panel to:
- View real-time GPS location
- Capture images from webcam
- Browse and download files
- Access target call logs

---

## ⚠️ Disclaimer

This tool is for educational and authorized testing purposes only.  
Do not use it on devices you do not own or have permission to test.  
The creator (Azhar) and Hackers Colony Official are not responsible for misuse.

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

---

© 2025 Azhar | Hackers Colony Official
