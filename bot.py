import os
from asyncio import run

from aiogram.filters import Command
from aiogram.types import BotCommand, Message
from dotenv import load_dotenv

from functions import start, stop, vacancy, start_menu, register_name, register_finish, category, product, amount
from states import SignUp, Product

load_dotenv()

from aiogram import Bot, Dispatcher

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


async def main(dp) -> None:
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Bot ni ishga tushirish"),
            BotCommand(command="/info", description="Shaxsiy ma'lumotlarni olish"),
            BotCommand(command="/vacancy", description="Ishga e'lon berish"),
            BotCommand(command="/help", description="Yordam")
        ]
    )
    dp.startup.register(start)
    dp.message.register(category,Product.category)
    dp.message.register(product,Product.product)
    dp.message.register(amount,Product.amount)
    dp.message.register(vacancy, SignUp.vacancy)
    dp.message.register(register_name, SignUp.name)
    dp.message.register(register_finish, SignUp.salary)
    dp.message.register(start_menu, Command('start'))
    dp.shutdown.register(stop)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main(dp))