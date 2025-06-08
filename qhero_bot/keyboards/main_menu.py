from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='\ud83d\udc64 Мой профиль', callback_data='profile')],
    [InlineKeyboardButton(text='\ud83d\udcda Каталог квестов', callback_data='catalog')],
    [InlineKeyboardButton(text='\ud83d\udd0d Рекомендации', callback_data='recommend')],
    [InlineKeyboardButton(text='\ud83d\udd25 Горящие квесты', callback_data='hot')],
])

