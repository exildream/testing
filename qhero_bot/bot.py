import asyncio
from aiogram import Bot, Dispatcher

from .config import settings
from .handlers import all_handlers

async def main():
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    for router in all_handlers:
        dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
