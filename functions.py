import os
from ftplib import all_errors
from pathlib import Path
from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import menu_button, contact_button, categories_keyboard, products_list
from states import SignUp, Product

tmp_filename = Path(__file__).parent / "users.txt"


async def start(bot: Bot):
    chat_id = os.getenv("CHAT_ID")
    if chat_id:
        await bot.send_message(chat_id=chat_id, text="Bot Ishga tushdi ✅")


async def stop(bot: Bot):
    chat_id = os.getenv("CHAT_ID")
    if chat_id:
        await bot.send_message(chat_id=chat_id, text="Bot To'xtadi ⚠️")


async def start_menu(msg: Message, bot: Bot, state: FSMContext):
    first_name = msg.from_user.first_name
    await msg.answer(
        f"<b>Assalomu Alaykum <u>{first_name}</u></b> <b>\nBotimizga Xush kelibsiz!!!👋</b>\n"
        f"<i>Quyidagi menulardan birini tanlang:</i>",
        parse_mode="HTML", reply_markup=menu_button)
    await state.set_state(Product.category)


async def category(msg: Message, bot: Bot, state: FSMContext):
    await msg.answer("Kategoriyalardan birini tanlang:", reply_markup=categories_keyboard)
    await state.set_state(Product.product)


async def product(msg: Message, bot: Bot, state: FSMContext):
    await msg.answer("Mahsulotlardan birini tanlang:", reply_markup=products_list)
    await state.update_data(category=msg.text)
    await state.set_state(Product.amount)


async def amount(msg: Message, bot: Bot, state: FSMContext):
    await msg.answer("Miqdorini kiriting:", reply_markup=None)
    await state.update_data(product=msg.text)
    await state.set_state(SignUp.vacancy)



async def vacancy(message: Message, bot: Bot, state: FSMContext):
    await message.answer(
        "Ismingnizni kiriting: "
    )
    await state.update_data(amount=message.text)
    await state.set_state(SignUp.name)


async def register_name(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamizni kiriting: ",reply_markup=contact_button)
    await state.set_state(SignUp.salary)

#
# async def register_phone(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(phone=message.text)
#     await message.answer("Manzilni kiriting: ")
#     await state.set_state(SignUp.address)
#
#
# async def register_address(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(address=message.text)
#     await message.answer("Lavozimni kiriting: ")
#     await state.set_state(SignUp.position)
#
#
# async def register_position(message: Message, bot: Bot, state: FSMContext):
#     await state.update_data(position=message.text)
#     await message.answer("Maoshni kiriting: ")
#     await state.set_state(SignUp.salary)

async def register_finish(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(phone=message.text)
    data =await state.get_data()
    txt = f'''Ma'lumotlaringiz: 
    Ism: {data.get("name")}
    Telefon: {data.get("phone")}
    Kategoriya: {data.get("category")}
    Mahsulot: {data.get("product")}
    Miqdor: {data.get("amount")} 
    '''
    await message.answer(text=txt, parse_mode="html")
    await message.answer("Tez Orada Kanalda Chop etiladi")
    await bot.send_message(chat_id=os.getenv("CHAT_ID"), text=txt)

    await state.clear()