from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from create_bot import bot, dp
from keyboards import kb_client

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС. Пожалуйста, напишите ему\n@Sushi_Shakirov_bot')

# @dp.message_handler(commands=['Режим_работы'])
async def sushi_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 дл 21:00, Сб-Вс с 9:00 до 23:00')

# @dp.message_handler(commands=['Расположение'])
async def sushi_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'бул. Александра Грина, 2, Санкт-Петербург', reply_markup=ReplyKeyboardRemove)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(sushi_open_command, commands=['operating_mode'])
    dp.register_message_handler(sushi_place_command, commands=['place'])