# QHERO Telegram Bot

Прототип Telegram-приложения для игроков в квесты. Используется `aiogram` 3, `pydantic-settings`, `SQLAlchemy` и `asyncpg`.

## Запуск
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Создайте файл `.env` со значениями `BOT_TOKEN` и `DB_DSN`:
   ```bash
   BOT_TOKEN=your_telegram_token
   DB_DSN=postgresql+asyncpg://user:pass@localhost/qhero
   ```
3. Запустите бота:
   ```bash
   python -m qhero_bot.bot
   ```

Минимальный WebApp-заглушка лежит в каталоге `webapp/`.
