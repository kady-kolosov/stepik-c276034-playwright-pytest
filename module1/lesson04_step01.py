# Ключевые особенности Playwright:

# 1. Кросс-браузерность
# Playwright поддерживает Chromium, Firefox и WebKit.
# Один и тот же тест можно запускать в разных браузерах.
# Также можно эмулировать мобильные устройства: iPhone, iPad, Android.

# 2. Автоожидания
# Playwright сам ждёт, пока элемент будет готов к действию:
# - появится в DOM
# - станет видимым
# - не будет перекрыт
# - станет доступен для клика/ввода
#
# Поэтому в Playwright почти не используют time.sleep().
# Это считается антипаттерном.

# 3. Отладка
# Для отладки можно использовать:
# - page.pause() — открыть Playwright Inspector
# - логи действий
# - скриншоты

# Playwright Inspector позволяет выполнять тест пошагово,
# проверять локаторы и смотреть состояние страницы.

# 4. Трассировка
# Trace — это запись выполнения теста.
# В неё входят:
# - скриншоты шагов
# - DOM
# - сетевые запросы и ответы
# - ошибки консоли
# - время выполнения действий

# Трассировка помогает быстро понять, почему тест упал.

# Пример:
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Запускаем браузер (дом)
    browser = p.chromium.launch(headless=False)

    # Создаём контекст (квартиру)
    context = browser.new_context()

    # Открываем страницу (комнату) в этом контексте
    page = context.new_page()
    page.goto("https://example.com")

    # Можем открыть ещё одну страницу в том же контексте
    page2 = context.new_page()
    page2.goto("https://google.com")

    # Создадим новый контекст (новую квартиру) — он будет полностью изолирован
    context2 = browser.new_context()
    page3 = context2.new_page()
    page3.goto("https://bing.com")

    # Не забываем закрыть браузер (дом)
    browser.close()
