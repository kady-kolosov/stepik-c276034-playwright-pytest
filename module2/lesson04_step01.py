import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

BASE_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
BASE_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")
HOST = f"https://{BASE_AUTH_USERNAME}:{BASE_AUTH_PASSWORD}@www.stg1.amediateka.tech/"

with sync_playwright() as p:
    # Запускаем браузер (Chromium) в видимом режиме
    browser = p.chromium.launch(headless=True)

    # Создаём новую страницу
    page = browser.new_page()

    # Переходим на сайт
    page.goto(HOST)

    # Делаем скриншот (просто для проверки)
    page.screenshot(path="result_image.png")

    # Ждём 2 секунды, чтобы увидеть результат (необязательно)
    page.wait_for_timeout(2000)

    # Закрываем браузер
    browser.close()

print("✅ Тестирование завершено успешно")
