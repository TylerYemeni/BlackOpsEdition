import os
import uuid
from gtts import gTTS

FAKE_VOICE_DIR = "samples/generated_voices"
os.makedirs(FAKE_VOICE_DIR, exist_ok=True)

def generate_fake_voice(text=None, lang='ar'):
    if not text:
        text = "مرحبًا، هذا بلاغ عاجل بشأن رقم يرسل محتوى مزعج ومسيء. الرجاء اتخاذ إجراء فوري. شكرًا لكم."

    try:
        tts = gTTS(text=text, lang=lang)
        filename = f"{uuid.uuid4()}.mp3"
        path = os.path.join(FAKE_VOICE_DIR, filename)
        tts.save(path)
        return path
    except Exception as e:
        print(f"[!] فشل في توليد الصوت: {e}")
        return None
