import logging
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramAPIError
from app.config import BOT_TOKEN


def parse_channel(channel: str | int) -> str | int:
    """
    Универсально парсит:
    - ссылку https://t.me/xxx
    - @username
    - числовой id (str или int)
    Возвращает @username или id для aiogram.
    """
    if isinstance(channel, int):
        return channel
    if channel.startswith("https://t.me/"):
        username = channel.removeprefix("https://t.me/").split("?")[0]
        if username.isdigit() or username.startswith("-100"):
            return int(username)
        return f"@{username}"
    if channel.startswith("@"):
        return channel
    if channel.lstrip("-").isdigit():
        return int(channel)
    raise ValueError(f"Can't parse channel: {channel}")


async def is_user_subscribed(user_id: int, channel: str | int) -> bool:
    async with Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML")) as bot:
        try:
            chat_ref = parse_channel(channel)
            member = await bot.get_chat_member(chat_ref, user_id)
            return member.status in ("member", "administrator", "creator")
        except TelegramAPIError as e:
            logging.warning(f"Telegram API error: {e}")
        except Exception as e:
            logging.exception(f"Unexpected error while checking subscription: {e}")
        return False
