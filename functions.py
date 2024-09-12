import os
from pathlib import Path

from aiogram import Bot, handlers
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, message

from keyboards import menu_button, location_contact_button, channel_list, categories_keyboard
import aiofiles as aiof

tmp_filename = Path(__file__).parent / "users.txt"


async def write_user(chat_id: str, first_name: str):
    async with aiof.open(tmp_filename, "a", encoding='utf-8') as out:
        await out.write(f"id:{chat_id} first_name:{first_name}\n")


async def start_menu(msg: Message, bot: Bot, state: FSMContext):
    first_name = msg.from_user.first_name
    user_id = msg.from_user.id
    await msg.answer(
        f"<b>Assalomu Alaykum <u>{first_name}</u></b> <b>\nBotimizga Xush kelibsiz!!!👋</b>\n"
        f"<i>Quyidagi menulardan birini tanlang:</i>",
        reply_markup=menu_button,
        parse_mode="HTML")


async def echo(message: Message, bot: Bot, state: FSMContext):
    message.answer(message.text)


async def share_menu(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Menulardan birini tanlang", reply_markup=location_contact_button)


async def register_location(message: Message, bot: Bot, state: FSMContext):
    chat_id = os.getenv("CHAT_ID")
    print(message.location.latitude, message.location.longitude)
    if chat_id:
        await bot.send_location(chat_id=chat_id, latitude=message.location.latitude,
                                longitude=message.location.longitude)
        await message.answer(text="Lokatsiya yuborildi, buyurmangiz tez orada yetkiziladi")


async def register_contact(msg: Message, bot: Bot, state: FSMContext):
    chat_id = os.getenv("CHAT_ID")
    if chat_id:
        await bot.send_contact(chat_id=chat_id, phone_number=msg.contact.phone_number,
                               first_name=msg.contact.first_name)
        await msg.answer(text="Kontaktiz yuborildi, admin tez orada aloqaga chiqadi")


async def start(bot: Bot):
    chat_id = os.getenv("CHAT_ID")
    if chat_id:
        await bot.send_message(chat_id=chat_id, text="Bot Ishga tushdi ✅")


async def stop(bot: Bot):
    chat_id = os.getenv("CHAT_ID")
    if chat_id:
        await bot.send_message(chat_id=chat_id, text="Bot To'xtadi ⚠️")
async def process_category(message: Message):
    category = message.text
    await message.answer(f"Tanlangan kategoriya: {category}")