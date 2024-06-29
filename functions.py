import os

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import menu_button, location_contact_button


async def start_menu(msg: Message, bot: Bot, state: FSMContext):
    await msg.answer("Menulardan birini tanlang ", reply_markup=menu_button)


async def echo(message: Message, bot: Bot, state: FSMContext):
    await message.copy_to(chat_id=message.from_user.id)


async def share_menu(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Menulardan birini tanlang", reply_markup=location_contact_button)


async def register_location(message: Message, bot: Bot, state: FSMContext):
    chat_id = os.getenv("CHAT_ID")
    print(message.location.latitude, message.location.longitude)
    await bot.send_location(chat_id=chat_id, latitude=message.location.latitude, longitude=message.location.longitude)
    await message.answer(text="Lokatsiya yuborildi buyurmangiz tez orada yetkiziladi")


async def register_contact(msg: Message, bot: Bot, state: FSMContext):
    chat_id = os.getenv("CHAT_ID")
    await bot.send_contact(chat_id=chat_id, phone_number=msg.contact.phone_number, first_name=msg.contact.first_name)
    await msg.answer(text="Kontaktiz yuborildi admin tez orada aloqaga chiqadi")


async def start(bot: Bot):
    await bot.send_message(chat_id="751843547", text="Bot Ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id="751843547", text="Bot To'xtadi ⚠️")
