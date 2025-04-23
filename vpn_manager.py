import subprocess
import time
import requests
import random

def get_current_ip():
    try:
        ip = requests.get("https://api.ipify.org").text.strip()
        return ip
    except:
        return "IP غير معروف"

def is_whatsapp_blocked():
    try:
        response = requests.get("https://web.whatsapp.com", timeout=5)
        return response.status_code != 200
    except:
        return True

def connect_protonvpn():
    print("[*] الاتصال بـ ProtonVPN...")
    try:
        subprocess.run(["protonvpn-cli", "c", "-f"], check=True)
        time.sleep(5)
        new_ip = get_current_ip()
        print(f"[+] متصل. IP الحالي: {new_ip}")
        if is_whatsapp_blocked():
            print("[!] واتساب محظور، جاري تبديل الخادم...")
            switch_protonvpn_server()
    except subprocess.CalledProcessError:
        print("[!] فشل الاتصال بـ ProtonVPN.")

def switch_protonvpn_server():
    print("[*] تبديل الخادم...")
    try:
        subprocess.run(["protonvpn-cli", "c", "-r"], check=True)
        time.sleep(5)
        new_ip = get_current_ip()
        print(f"[+] تم التبديل. IP الجديد: {new_ip}")
    except:
        print("[!] فشل تبديل الخادم.")

def auto_vpn_check():
    if is_whatsapp_blocked():
        print("[!] تم الكشف عن حظر، جاري تبديل VPN تلقائيًا...")
        switch_protonvpn_server()
