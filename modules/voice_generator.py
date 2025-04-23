from gtts import gTTS
import random
import os

def generate_fake_voice(text=None, lang='ar', filename="samples/fake_voice.mp3"):
    if text is None:
        texts = [
            "أرجوكم، هذا الرقم يرسل تهديدات لي ولعائلتي...",
            "الرقم هذا يتحرش في الأطفال... ساعدوني",
            "مرحبا، الرقم هذا نصب علي بمبالغ كبيرة، أرجو اتخاذ إجراء",
            "أواجه مضايقات بشكل يومي من هذا الرقم... أخاف يضرني"
        ]
        text = random.choice(texts)

    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        print(f"[+] تم توليد بلاغ صوتي وهمي: {filename}")
        return filename
    except Exception as e:
        print(f"[!] فشل توليد الصوت: {e}")
        return None
