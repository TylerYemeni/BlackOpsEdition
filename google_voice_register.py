from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_google_voice():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://voice.google.com")
    time.sleep(5)
    print("[+] Google Voice page opened. Proceed with login manually or via automation.")
    driver.quit()

if __name__ == "__main__":
    open_google_voice()
