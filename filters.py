import os
from typing import Any, Union, Dict

from aiogram import Bot
from aiogram.filters import Filter
from aiogram.types import Message, User


class CheckSubFilter(Filter):

    async def __call__(self, message: Message, bot: Bot) -> Union[bool, Dict[str, Any]]:
        channel_id = os.getenv("CHANNEL_ID")
        user: User = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
        if user.status in ["member", "adminstrator", "creator"]:
            return False
        else:
            return True
