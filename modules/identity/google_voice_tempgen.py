import random
import time
import string

def generate_temp_email():
    domains = ["@tempmail.dev", "@mail.tm", "@fakeinbox.com"]
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return name + random.choice(domains)

def generate_fake_google_voice():
    numbers_start = ["+1510", "+1408", "+1626", "+1206"]
    number = random.choice(numbers_start) + ''.join(random.choices("0123456789", k=7))
    return number

def generate_google_voice_identity():
    identity = {
        "email": generate_temp_email(),
        "google_voice_number": generate_fake_google_voice(),
        "name": random.choice(["سالم", "راشد", "خالد", "نايف", "فهد"]),
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return identity

def print_identity(identity):
    print("[+] هوية Google Voice وهمية:")
    for k, v in identity.items():
        print(f"   - {k}: {v}")

# مثال على التنفيذ المباشر
if __name__ == "__main__":
    id = generate_google_voice_identity()
    print_identity(id)
