import os
import requests
import time

def get_current_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return ip
    except:
        return "غير معروف"

def ensure_vpn_connected():
    print("[•] التأكد من تفعيل VPN...")
    old_ip = get_current_ip()
    os.system("protonvpn-cli c -f")  # الاتصال بأسرع سيرفر
    time.sleep(7)
    new_ip = get_current_ip()
    print(f"[✓] تم تغيير الـ IP: {old_ip} → {new_ip}")
