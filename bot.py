import os
from asyncio import run

from aiogram.filters import CommandStart, Command
from aiogram import F

from aiogram.types import BotCommand, Message
from dotenv import load_dotenv

from functions import start, stop, echo, start_menu, share_menu, register_location, register_contact

load_dotenv()

from aiogram import Bot, Dispatcher, F

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


async def main(dp) -> None:
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Bot ni ishga tushirish"),

            BotCommand(command="/share", description="Ma'lumotlarni yuborish")
        ]
    )
    dp.startup.register(start)
    dp.message.register(start_menu, CommandStart())
    dp.message.register(share_menu, Command('share'))
    dp.message.register(register_location, F.location)
    dp.message.register(register_contact, F.contact)
    # dp.message.register(register_contact, F.text=="xabar")
    dp.message.register(echo)
    # dp.message.register(start_menu, CommandStart())
    dp.shutdown.register(stop)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main(dp))
