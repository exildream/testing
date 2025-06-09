from aiogram import Router, types
from aiogram.filters import Command
from sqlalchemy import select

from ..db import get_session
from ..models import Quest

router = Router()

@router.callback_query(lambda c: c.data == 'catalog')
async def catalog_callback(call: types.CallbackQuery):
    async for session in get_session():
        result = await session.execute(select(Quest).limit(5))
        quests = result.scalars().all()
        text = '\n'.join(q.title for q in quests) or 'Каталог пуст'
    await call.message.edit_text(text)
    await call.answer()

@router.message(Command('quests'))
async def quests_cmd(message: types.Message):
    async for session in get_session():
        result = await session.execute(select(Quest).limit(5))
        quests = result.scalars().all()
        text = '\n'.join(q.title for q in quests) or 'Каталог пуст'
    await message.answer(text)
