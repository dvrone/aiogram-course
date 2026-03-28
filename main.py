import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import config

bot = Bot(config.TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def welcome_cmd(message: Message):
    await message.reply(
        f"Hello, this is your ID: {message.from_user.id}, and your name: {message.from_user.first_name}"
    )
    # await message.answer("Hello!")


@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer("This is /help command.")


@dp.message(F.text == "How are you?")
async def feeling(message: Message):
    await message.answer("OK!")


@dp.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f"Photo ID: {message.photo[-1].file_id}")


@dp.message(Command("photo"))
async def send_photo_by_id(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMVacdqgxpVlxjve_8RmApJyCo2khYAAn4Saxtt2zlKkb4NXKNPckABAAMCAAN5AAM6BA",
        caption="This is a picture.",
    )


@dp.message(Command("photo2"))
async def send_photo_by_url(message: Message):
    await message.answer_photo(
        photo="https://i.pinimg.com/736x/a0/33/a6/a033a6d215cfdc41dbfd92c5ac5dc8cf.jpg",
        caption="This picture was uploaded via URL.",
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Goodbye!")
