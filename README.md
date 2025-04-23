# أبو حرب - AbuHarb
أقوى أداة بلاغات وهمية تلقائية على أرقام WhatsApp باستخدام هوية مزورة وVPN وحماية من الحظر.

## الميزات:
- اتصال تلقائي بـ VPN (ProtonVPN / NordVPN)
- توليد هويات وصور وهمية
- دعم إرسال بريد إلكتروني وهمي (Gmail)
- إرسال SMS مزيف (Twilio)
- تسجيل بلاغات صوتية وهمية
- توليد حسابات واتساب وهمية مستقبلًا (Google Voice - Temp Mail)
- كشف تلقائي إذا تم الحظر وإعادة محاولة ب IP جديد
- تسجيل كل شيء في reports.log

## المتطلبات:
- Python 3.8 أو أحدث
- حساب Gmail + كلمة مرور تطبيق
- حساب Twilio مجاني (اختياري)
- تثبيت ProtonVPN على جهازك مسبقًا وتفعيله مرة واحدة
- تشغيل الأداة من Kali Linux أو Termux أو Ubuntu

## التثبيت:
```bash
git clone https://github.com/your-user/abuharb
cd abuharb
pip install -r requirements.txt
