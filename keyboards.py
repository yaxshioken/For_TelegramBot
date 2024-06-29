from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="button-1", ), KeyboardButton(text="button-2")],
        [KeyboardButton(text="button-3"), KeyboardButton(text="button-4")]
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
