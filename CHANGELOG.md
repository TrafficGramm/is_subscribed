# Changelog

Все значимые изменения этого проекта документируются в этом файле.

Формат основан на [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
и этот проект придерживается [Семантического Версионирования](https://semver.org/lang/ru/).

## [0.1.0] — 2025-06-22
### Добавлено
- FastAPI-приложение с эндпоинтом `POST /check-subscription` для проверки подписки пользователя на Telegram-канал.
- Асинхронная интеграция с Telegram Bot API через `aiogram`.
- Обработка ошибок Telegram API, включая приватные и несуществующие каналы.
- Поддержка переменных окружения через `.env` и `python-dotenv`.
- Структурированная архитектура проекта (`app/routers`, `app/services`, `app/schemas`, `app/config.py`).
- Поддержка `pyproject.toml` с зависимостями: `aiogram`, `fastapi`, `httpx`, `uvicorn`, `pytest`, и др.
- Тесты на `pytest` + `httpx.AsyncClient` с `ASGITransport` без запуска сервера.
