import time
from modules.ip_manager import ensure_vpn_connected
from modules.identity_generator import generate_identity
from modules.fake_media import prepare_fake_media
from modules.report_engine import send_full_report
from modules.protection import check_whatsapp_response
from modules.logger import log_report

def main():
    print("\n[×] بدء تشغيل مشروع أبو سالم V2 - BlackOps Edition\n")
    
    ensure_vpn_connected()

    for _ in range(5):  # عدد البلاغات، يمكنك تعديله
        print("\n[+] بدء دورة بلاغ جديدة...\n")

        # 1. توليد هوية وهمية
        identity = generate_identity()
        print(f"[•] توليد هوية: {identity['name']}")

        # 2. تجهيز صور وصوت
        media = prepare_fake_media()
        
        # 3. إرسال البلاغ الكامل
        success = send_full_report(identity, media)

        # 4. تسجيل البلاغ
        log_report(identity, success)

        # 5. فحص استجابة واتساب (إذا تم الحظر أو تم الرفض)
        if not check_whatsapp_response():
            print("[!] تم الكشف عن البوت أو الحظر! سيتم تبديل IP...")
            ensure_vpn_connected()

        # 6. تأخير عشوائي لتفادي الحظر
        delay = time.randint(10, 20)
        print(f"[•] تأخير {delay} ثانية قبل البلاغ التالي.")
        time.sleep(delay)

    print("\n[✓] تم تنفيذ جميع البلاغات. راجع التقارير في sessions/reports.log\n")

if __name__ == "__main__":
    main()
