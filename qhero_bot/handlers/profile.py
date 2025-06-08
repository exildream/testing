from aiogram import Router, types

from ..db import get_session
from ..models import User

router = Router()

@router.callback_query(lambda c: c.data == 'profile')
async def profile_callback(call: types.CallbackQuery):
    async for session in get_session():
        user = await session.get(User, call.from_user.id)
        if not user:
            user = User(id=call.from_user.id, nickname=call.from_user.username)
            session.add(user)
            await session.commit()
        text = f"Профиль {user.nickname}\nXP: {user.xp}\nУровень: {user.level}"
    await call.message.edit_text(text, reply_markup=None)
    await call.answer()

