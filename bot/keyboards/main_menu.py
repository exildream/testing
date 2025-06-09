from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

WEBAPP_URL = "https://example.com/frontend/"

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🚀 Открыть приложение', web_app=WebAppInfo(url=WEBAPP_URL))],
    [InlineKeyboardButton(text='🧑‍🎤 Мой профиль', callback_data='profile')],
    [InlineKeyboardButton(text='📚 Каталог квестов', callback_data='catalog')],
    [InlineKeyboardButton(text='🔍 Рекомендации', callback_data='recommend')],
    [InlineKeyboardButton(text='🔥 Горящие квесты', callback_data='hot')],
])
