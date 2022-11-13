from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher(bot)
# '_______________Client_place_______________'
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС. Пожалуйста, напишите ему\n@Sushi_Shakirov_bot')

@dp.message_handler(commands=['Режим_работы'])
async def sushi_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 дл 21:00, Сб-Вс с 9:00 до 23:00')

@dp.message_handler(commands=['Расположение'])
async def sushi_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'бул. Александра Грина, 2, Санкт-Петербург')


@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привет!':
        await message.answer('И тебе привет!')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True)