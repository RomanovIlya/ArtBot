from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from main import bot, dp
from get_photo import google_img
import os
from aiogram.dispatcher.filters.state import StatesGroup,State
class Test(StatesGroup):
    Wait=State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    button = KeyboardButton("Начать поиск")
    menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button)
    await bot.send_message(message.from_user.id,
                           "Привет {0.first_name}.Я могу найти любое изображение но только говори четко!Например поза для срисовки".format(message.from_user), reply_markup=menu)

# Button analyzer
@dp.message_handler(state=None)
async def on_button(message: types.Message):
    if message.text == 'Начать поиск':
        await bot.send_message(message.from_user.id, "Пожайлуста, введите что вы хотите найти")
        await Test.Wait.set()

@dp.message_handler(state=Test.Wait)
async def wait(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['wait'] = message.text
    await state.finish()
    google_img(data['wait'])
    sp = os.listdir(path="./img")
    for i in sp:
        doc = open("./img/"+i, 'rb')
        await bot.send_document(message.from_user.id,doc)
        os.remove("./img/"+i)