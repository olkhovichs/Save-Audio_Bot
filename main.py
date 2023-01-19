from pathlib import Path
from aiogram import Bot, types
from aiogram.types import ContentType, File, Message
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN

import telebot
import requests

bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def handle_file(file: File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)
    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")

@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    voice = await message.voice.get_file()
    path = "audio_messages"
    await handle_file(file=voice, file_name=f"{voice.file_id}.ogg", path=path)


if __name__ == '__main__':
    executor.start_polling(dp)