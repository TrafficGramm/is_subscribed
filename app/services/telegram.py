import logging
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramAPIError
from app.config import BOT_TOKEN


async def is_user_subscribed(user_id: int, channel: str | int) -> bool:
    async with Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML")) as bot:
        try:
            if isinstance(channel, str) and channel.startswith("https://t.me/"):
                username = channel.removeprefix("https://t.me/").split("?")[0]
                chat = await bot.get_chat("@" + username)
                channel = chat.id

            member = await bot.get_chat_member(channel, user_id)
            return member.status in ("member", "administrator", "creator")
        except TelegramAPIError as e:
            logging.warning(f"Telegram API error: {e}")
        except Exception as e:
            logging.exception(f"Unexpected error while checking subscription: {e}")
        return False
