from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command('review'))
async def review_cmd(message: types.Message):
    await message.answer('Оставлять отзывы можно после прохождения двух квестов.')
