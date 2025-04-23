import pyttsx3
import random
import os

def generate_fake_voice(text=None, filename="fake_voice.wav"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', random.choice(voices).id)
    engine.setProperty('rate', 150)

    if not text:
        text = random.choice([
            "Hello, this is a verification call.",
            "Please confirm your identity.",
            "My name is John, I'm here to verify your WhatsApp number.",
            "This is a demo voice message for WhatsApp activation."
        ])

    print(f"[+] Generating voice: '{text}'")
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"[+] Voice saved as {filename}")

if __name__ == "__main__":
    generate_fake_voice()
