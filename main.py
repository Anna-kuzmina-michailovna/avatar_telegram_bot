
import logging

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

TOKEN = '5430024534:AAHtTqGqbygBTC9OyCLrsRYz5Hs3Aau2awY'

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.DEBUG)


# Функция ниже читает все, что пишут в группе (если бота сделать админом)
# или только то, что пишут боту и ждет, когда кто-то напишет ann
@dp.message_handler(Text(equals='ann', ignore_case=True), state="*")
async def cmd_start(message: types.Message, state: FSMContext):
    media = types.InputFile('picture.jpg')  # этот файл должен лежать в корне проекта
    info = '''
    <i>Информация о субъекте:</i>

    <code>Класс:  </code>👽 Гуманоид
    <code>Вид:    </code>🧟 Homo Sapiens
    <code>Рожден: </code>🌏 Планета Земля
    '''

    await message.answer_photo(media)  # отвечаем на сообщение картинкой
    await message.answer(info)  # отвечаем на сообщение текстом





# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
