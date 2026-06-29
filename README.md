# [Курс Stepik: Автоматизация тестирования с Playwright и PyTest](https://stepik.org/course/276034/promo)

## Стек
- Python
- Pytest
- Playwright
- Allure

## Создать и активировать виртуальное окружение

### Mac OS
```bash
python3 -m venv .venv
source .venv/bin/activate
```
или

```bash
/opt/homebrew/bin/python3.14 -m venv .venv
source .venv/bin/activate
```

### Windows
```bash
python -m venv .venv
source .venv/Scripts/activate
```

или

```bash
"/c/Program Files/Python314/python.exe" -m venv .venv
source .venv/Scripts/activate
```

## Проверка работоспособности

```bash
python --version
which python
pip --version
```

## Установить зависимости

### Mac OS
```bash
.venv/bin/python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Windows
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Установить браузеры Playwright

```bash
playwright install
```

## Зафиксировать новые зависимости в файле `requirements.txt`

```bash
pip freeze > requirements.txt
```
