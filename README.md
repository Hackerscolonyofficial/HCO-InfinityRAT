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

```bash
git clone https://github.com/Hackerscolonyofficial/HCO-InfinityRAT-Final
cd HCO-InfinityRAT-Final
```

Install Termux dependencies:

```bash
pkg update && pkg upgrade -y
pkg install python git openjdk-17 apktool -y
pip install flask
```

Build the APK:

```bash
python apk_builder.py
```

APK Output Location:

```
output/HCO-InfinityRAT.apk
```

---

## 📱 Installing and Running the APK on Target Device

1. Transfer the APK to your phone using USB, Bluetooth, or file-sharing apps.  
2. Open any File Manager app and navigate to:
   - **Download/**
   - **Bluetooth/**
   - **Documents/**
   - Or wherever you placed the APK.
3. Tap `HCO-InfinityRAT.apk` and install it.  
4. Allow unknown sources if prompted.  
5. Open the app after installation to activate.

---

## 🧠 Using the Tool in Termux

Start the Flask control panel:

```bash
python main.py
```

Open a browser and go to:

```
http://localhost:22533
```

You can now:
- 🌍 Track GPS  
- 📷 Capture webcam  
- 📂 Browse & download files  
- 📞 Read call logs  

---

## 🌐 Make Panel Public (Tunnel)

### Option 1: Cloudflare Tunnel

```bash
pkg install cloudflared -y
python tunnel.py
```

Use the URL shown to access from anywhere.

---

### Option 2: Ngrok

1. Install from https://ngrok.com  
2. Start server:

```bash
python main.py
```

3. Then tunnel it:

```bash
ngrok http 22533
```

Use the URL shown in terminal.

---

## 🔐 Access Key System

To use the tool, an **Access Key** is required.  
👉 Contact on **Telegram** or **WhatsApp: +91 8420611159**  
**Subscribe to our YouTube channel & DM for the key.**  
Without the key, the tool **will not function**.

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing purposes only**.  
Do **NOT** use it on unauthorized devices.  
Azhar and Hackers Colony Official are **not responsible** for any misuse.

---

## 📄 License

Licensed under the MIT License.

---

## 📢 Hackers Colony Official

- GitHub: https://github.com/Hackerscolonyofficial  
- YouTube: https://www.youtube.com/@HackersColonyOfficial  
- Instagram: https://www.instagram.com/hackers_colony_official  
- Telegram: https://t.me/hackersColony  
- Discord: https://discord.gg/Xpq9nCGD
