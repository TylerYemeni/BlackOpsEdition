import os
import random
import time
import requests
from modules.ip_manager import change_ip, get_current_ip
from modules.identity.google_voice_tempgen import generate_google_voice_identity
from modules.email_report import send_email_report
from modules.twilio_sms import send_twilio_sms

LOG_FILE = "sessions/reports.log"

def log_report(identity, method, status):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time.ctime()}] {method} | {identity['google_voice_number']} | {status}\n")

def is_whatsapp_blocked():
    try:
        # اختبار بسيط لمحاكاة حظر (مثلاً API واتساب أو أي استجابة)
        response = requests.get("https://web.whatsapp.com/", timeout=5)
        return response.status_code != 200
    except:
        return True

def send_realistic_report(identity):
    message = f"""
    بلاغ عاجل:

    الشخص ({identity['name']}) تلقى رسائل مزعجة من رقم واتساب مشبوه.

    الرقم المشبوه: {identity['google_voice_number']}
    يرجى التحقيق الفوري.
    """
    try:
        send_email_report("abuse@whatsapp.com", identity["name"])
        send_twilio_sms("+14155238886", message)  # رقم واتساب الرسمي
        print("[+] تم إرسال بلاغ عبر Twilio و Email.")
        log_report(identity, "Twilio+Email", "تم الإرسال")
    except Exception as e:
        print(f"[!] فشل الإرسال: {e}")
        log_report(identity, "Twilio+Email", "فشل")

def run_reporting_engine():
    print("[*] تشغيل محرك التقارير الذكي...")
    identity = generate_google_voice_identity()

    if is_whatsapp_blocked():
        print("[!] تم حظر الاتصال أو الموقع. إعادة الاتصال عبر VPN...")
        change_ip()
        time.sleep(4)
        ip = get_current_ip()
        print(f"[+] IP الجديد: {ip}")
    
    send_realistic_report(identity)
    delay = random.randint(10, 30)
    print(f"[*] انتظار {delay} ثانية قبل البلاغ التالي...")
    time.sleep(delay)
