from aiogram import Router, F, types
from backend.db import get_session
from backend.models import Record

router = Router()

@router.message(F.text.regexp(r'^QR:'))
async def handle_qr(message: types.Message):
    qr_value = message.text[3:].strip()
    async for session in get_session():
        record = await session.get(Record, (message.from_user.id, int(qr_value)))
        if record:
            record.qr_verified = True
            await session.commit()
            await message.answer('Прохождение подтверждено!')
        else:
            await message.answer('Запись не найдена.')
