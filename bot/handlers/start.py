from aiogram import Router, F
from aiogram.types import Message

from ..keyboards.main_menu import main_menu

router = Router()

@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в QHERO! Выберите действие:', reply_markup=main_menu)

