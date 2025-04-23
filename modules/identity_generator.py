import random
import requests
from faker import Faker
from PIL import Image
from io import BytesIO
import os
import uuid

faker = Faker('ar_SA')  # توليد بيانات عربية وهمية

IMAGES_DIR = "samples/generated_images"
os.makedirs(IMAGES_DIR, exist_ok=True)

def generate_identity():
    name = faker.name()
    address = faker.address()
    phone = faker.phone_number()
    email = faker.email()
    national_id = str(random.randint(1000000000, 9999999999))
    gender = random.choice(['ذكر', 'أنثى'])

    return {
        "name": name,
        "address": address,
        "phone": phone,
        "email": email,
        "national_id": national_id,
        "gender": gender
    }

def generate_fake_image():
    try:
        response = requests.get("https://picsum.photos/256", timeout=10)
        img = Image.open(BytesIO(response.content))
        file_name = f"{uuid.uuid4()}.jpg"
        img_path = os.path.join(IMAGES_DIR, file_name)
        img.save(img_path)
        return img_path
    except Exception as e:
        print(f"[!] فشل توليد صورة وهمية: {e}")
        return None
