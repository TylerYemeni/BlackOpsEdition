import time
from modules.vpn.auto_connect import auto_connect_vpn
from modules.security.report_engine import run_reporting_engine
from modules.utils.banner import print_banner

def main():
    print_banner()
    
    print("[*] محاولة الاتصال بـ VPN تلقائيًا...")
    auto_connect_vpn()
    
    try:
        while True:
            run_reporting_engine()
    except KeyboardInterrupt:
        print("\n[!] تم إيقاف الأداة يدويًا.")
    except Exception as e:
        print(f"[!] خطأ غير متوقع: {e}")

if __name__ == "__main__":
    main()
