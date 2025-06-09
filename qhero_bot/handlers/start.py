from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from ..db import get_session
from ..models import User
from ..keyboards.main_menu import main_menu

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    async for session in get_session():
        user = await session.get(User, message.from_user.id)
        if not user:
            user = User(
                id=message.from_user.id,
                nickname=message.from_user.username or message.from_user.full_name,
                avatar=None,
                genres=[],
            )
            session.add(user)
            await session.commit()
    await message.answer(
        'Добро пожаловать в QHERO! Выберите действие:', reply_markup=main_menu
    )
