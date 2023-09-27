from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from defs import get_info, change_badge

keyboard = [KeyboardButton("Купить подписку 🤑"), KeyboardButton("Посмотреть информацию ℹ️")]
buy_keyboard = [[InlineKeyboardButton("На 1 месяц", callback_data="1")]]
info_keyboard = [KeyboardButton("Изменить номер бейджика 🪛"),KeyboardButton("Назад 🔙")]
payment_keyboard = [KeyboardButton("Назад 🔙")]
menu_keyboard = [KeyboardButton("Назад 🔙")]

prices = [
    types.LabeledPrice(label='Подписька на месяц', amount=20000),
]

content = {
    "welcome": "Добро пожаловать {nick}👋 !\n\n Что бы продолжить нажми на одну из кнопок в меню",
}

keyboards = {
    "keyboard": ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(*keyboard),
    "Купить подписку 🤑": InlineKeyboardMarkup(inline_keyboard=buy_keyboard),
    "info_keyboard": ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(*info_keyboard),
    "payment_keyboard": ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(*payment_keyboard),
    "menu_keyboard": ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(*menu_keyboard)
}

answers = {
    "Купить подписку 🤑": "Выбери насколько ты хочешь купить подписку",
    "Назад 🔙": "Выбери что то из меню блеа"
}

get_answers = {
    "Посмотреть информацию ℹ️": get_info,
    "Изменить номер бейджика 🪛": change_badge,
}

items = {
    "desk": ["Подписка", "Хватит терпеть унижения тестами, пора стать реал гэнста"]
}

img = {
    "subscribe": "https://i.ytimg.com/vi/Q0xMZmL8zT8/hqdefault.jpg"
}
