# Playwright состоит из трёх основных сущностей:
# Browser — сам браузер: Chromium, Firefox или WebKit.
# BrowserContext — изолированная сессия внутри браузера:
# отдельные cookies, localStorage, sessionStorage и настройки устройства.
# Page — отдельная вкладка/страница внутри BrowserContext.

# Упрощённая схема:
# Browser = дом
# BrowserContext = отдельная квартира
# Page = комната/вкладка в квартире

# Зачем нужен BrowserContext:
# - изолирует тесты друг от друга
# - позволяет запускать тесты параллельно
# - позволяет эмулировать разные устройства и окружения
#
# В pytest обычно не создаём всё вручную:
# Playwright даёт готовые фикстуры browser, context и page.
