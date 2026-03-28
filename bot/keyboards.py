from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🗂️ Category")],
        [KeyboardButton(text="🛒 Cart"), KeyboardButton(text="👤 Contact")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose one from the menu below! 📋⬇️",
)

language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbekcha", callback_data="uz"),
            InlineKeyboardButton(text="English", callback_data="en"),
            InlineKeyboardButton(text="Русский", callback_data="ru"),
        ]
    ]
)

cars = ["Tesla", "Mercedes", "BMW"]


async def reply_buttons():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()


async def inline_buttons():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, callback_data=car.lower()))
    return keyboard.adjust(2).as_markup()
