import requests
import time

def get_temp_email():
    url = "https://www.1secmail.com/api/v1/"
    params = {"action": "genRandomMailbox", "count": 1}
    email = requests.get(url, params=params).json()[0]
    return email

def check_inbox(email):
    login, domain = email.split('@')
    inbox_url = "https://www.1secmail.com/api/v1/"
    params = {
        "action": "getMessages",
        "login": login,
        "domain": domain
    }
    messages = requests.get(inbox_url, params=params).json()
    return messages

if __name__ == "__main__":
    email = get_temp_email()
    print("[*] Temp Email:", email)
    print("[*] Checking inbox...")
    time.sleep(10)
    print(check_inbox(email))
