from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

import bot.keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    number = State()
    age = State()


@router.message(CommandStart())
async def welcome_cmd(message: Message):
    await message.reply(
        f"Hello, this is your ID: {message.from_user.id}, and your name: {message.from_user.first_name}\n"
        "🇺🇿 Bot tilini tanlang!\n🇬🇧 Select bot language!\n🇷🇺 Выберите язык бота!",
        # reply_markup=kb.main,
        # reply_markup=kb.language,
        reply_markup=kb.welcome_markup,
    )
    # await message.answer("Hello!")


@router.message(Command("cars"))
async def get_cars(message: Message):
    await message.answer(
        f"Pick a car! 🚙",
        # reply_markup=await kb.reply_buttons(),
        reply_markup=await kb.inline_buttons(),
    )


@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer("This is /help command.")


@router.message(F.text == "How are you?")
async def feeling(message: Message):
    await message.answer("OK!")


@router.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f"Photo ID: {message.photo[-1].file_id}")


@router.message(Command("photo"))
async def send_photo_by_id(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMVacdqgxpVlxjve_8RmApJyCo2khYAAn4Saxtt2zlKkb4NXKNPckABAAMCAAN5AAM6BA",
        caption="This is a picture.",
    )


@router.message(Command("photo2"))
async def send_photo_by_url(message: Message):
    await message.answer_photo(
        photo="https://i.pinimg.com/736x/a0/33/a6/a033a6d215cfdc41dbfd92c5ac5dc8cf.jpg",
        caption="This picture was uploaded via URL.",
    )


@router.callback_query(F.data == "category")
async def category(callback: Callback):
    # await callback.answer("You have selected a category.")
    await callback.answer("This is alert message!", show_alert=True)
    await callback.message.answer("Hello!")


@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("What is your name?")


@router.message(Register.name)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.number)
    await message.answer("Enter your phone number!")


@router.message(Register.number)
async def number_handler(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(Register.age)
    await message.answer("How old are you?")


@router.message(Register.age)
async def age_handler(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer(
        f"Thank you!\nName: {data['name']}\nPhone No.: {data['number']}\nAge: {data['age']}"
    )
