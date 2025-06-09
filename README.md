# QHERO Telegram Bot

Пример прототипа системы для любителей квестов. Используется Python 3 и библиотека `aiogram` 3.

## Запуск
1. Создайте виртуальное окружение и установите зависимости:
   ```bash
   pip install aiogram pydantic sqlalchemy asyncpg
   ```
2. Создайте файл `.env` или переменные окружения `BOT_TOKEN` и `DB_DSN` для указания токена бота и строки подключения к PostgreSQL.
3. Запустите бота:
   ```bash
   python -m qhero_bot.bot
   ```

Минимальный webapp находится в каталоге `webapp/`. Это простая HTML‑заглушка.
