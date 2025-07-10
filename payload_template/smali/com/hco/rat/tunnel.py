import os
import shutil

print("[+] Starting Cloudflare Tunnel on port 22533...")

# Check if cloudflared is installed
if not shutil.which("cloudflared"):
    print("[-] Cloudflared not found. Installing...")
    os.system("pkg install cloudflared -y")

# Start the tunnel
os.system("cloudflared tunnel --url http://localhost:22533")
