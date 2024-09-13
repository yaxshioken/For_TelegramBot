
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
contact_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Telefon raqamimni yuboraman", request_contact=True,)]
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
products_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yuzani tozalash gel - 500ml"),
            KeyboardButton(text="Yuzani tozalash sprey - 250ml"),
        ],
        [
            KeyboardButton(text="Yuzani tozalash yuvish qog'ozi"),
            KeyboardButton(text="Yuzani tozalash mikrofibr - 1 dona"),
        ],
        [
            KeyboardButton(text="Yuzani tozalash to'liq paket"),
            KeyboardButton(text="Xona tozalash sprey - 1L"),
        ],
        [
            KeyboardButton(text="Xona tozalash mop - 1 dona"),
            KeyboardButton(text="Xona tozalash mashinasi"),
        ],
        [
            KeyboardButton(text="Xona tozalash qoplama"),
            KeyboardButton(text="Xona tozalash to'liq paket"),
        ],
        [
            KeyboardButton(text="Maxsus tozalash sprey - 500ml"),
            KeyboardButton(text="Maxsus tozalash jel - 1L"),
        ],
        [
            KeyboardButton(text="Maxsus tozalash pastasi"),
            KeyboardButton(text="Maxsus tozalash qog'ozi"),
        ],
        [
            KeyboardButton(text="Maxsus tozalash to'liq paket"),
            KeyboardButton(text="Pudratchi tozalash suyuqligi - 1L"),
        ],
        [
            KeyboardButton(text="Pudratchi mop - 1 dona"),
            KeyboardButton(text="Pudratchi tozalash mashinasi"),
        ],
        [
            KeyboardButton(text="Pudratchi tozalash yuvish qog'ozi"),
            KeyboardButton(text="Pudratchi tozalash to'liq paket"),
        ],
        [
            KeyboardButton(text="Oshxona tozalash sprey - 500ml"),
            KeyboardButton(text="Oshxona tozalash mop - 1 dona"),
        ],
        [
            KeyboardButton(text="Oshxona tozalash jel - 1L"),
            KeyboardButton(text="Oshxona tozalash qog'ozi"),
        ],
        [
            KeyboardButton(text="Oshxona tozalash to'liq paket"),
            KeyboardButton(text="Jismoniy yordamchi sprey - 500ml"),
        ],
        [
            KeyboardButton(text="Jismoniy yordamchi gel - 1L"),
            KeyboardButton(text="Jismoniy yordamchi mikrofibr - 1 dona"),
        ],
        [
            KeyboardButton(text="Jismoniy yordamchi tozalash qog'ozi"),
            KeyboardButton(text="Jismoniy yordamchi to'liq paket"),
        ]
    ],
    resize_keyboard=True
)
