# QHERO Platform

Пример минимальной реализации Telegram Mini App для системы QHERO.
Состоит из бэкенда на FastAPI, Telegram‑бота и WebApp на чистом JS.

## Структура
```
backend/   # FastAPI приложение и модели
bot/       # Telegram бот на aiogram
frontend/  # клиентская часть WebApp
```

## Быстрый старт
1. Установите зависимости
   ```bash
   pip install -r requirements.txt
   ```
2. Скопируйте `.env.example` в `.env` и укажите токен бота и DSN базы.
3. Запустите бота:
   ```bash
   python -m bot.bot
   ```
4. Запустите бэкенд:
   ```bash
   uvicorn backend.main:app
   ```

Фронтенд располагается в каталоге `frontend/` и может быть раздаваем любым веб‑сервером.
