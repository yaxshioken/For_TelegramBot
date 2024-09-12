
from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Mahsulot", ), KeyboardButton(text="Savat")],
        [KeyboardButton(text="Malumot"), KeyboardButton(text="TIL")]
    ],
    resize_keyboard=True
)
categories_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Yuzalarni Tozalash Vositalari")],
        [KeyboardButton(text="Xona Tozalash Vositalari")],
        [KeyboardButton(text="Maxsus Tozalash Vositalari")],
        [KeyboardButton(text="Pudratchi Vositalari")],
        [KeyboardButton(text="Oshxona Tozalash Vositalari")],
        [KeyboardButton(text="Jismoniy Yordamchi Vositalari")]
    ],
    resize_keyboard=True
)
location_contact_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lokatsiya Yuborish", request_location=True),
            KeyboardButton(text="Kontak Yuborish", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

channel_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kanal 1", url="https://t.me/kunuzofficial"),
            InlineKeyboardButton(text="Kanal 2", url="https://t.me/Daryo"),
            InlineKeyboardButton(text="Kanal 3", url="https://t.me/qalampir")
        ],
        [
            InlineKeyboardButton(text="Tekshirish ✅", callback_data="check_subscription")
        ]
    ]
)
