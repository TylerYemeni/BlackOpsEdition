import time
import random

def fake_whatsapp_login(fake_number):
    print(f"[*] تسجيل دخول برقم وهمي: {fake_number}")
    time.sleep(random.uniform(2, 5))
    print("[+] تم تسجيل الدخول (وهميًا) إلى واتساب.")

def send_whatsapp_report(fake_number, target_number, message):
    print(f"[*] إرسال بلاغ من {fake_number} إلى {target_number}...")
    time.sleep(random.uniform(1, 3))
    print(f"[+] تم إرسال البلاغ: {message}")
