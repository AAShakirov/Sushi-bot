from aiogram import types, Dispatcher
from create_bot import dp, bot
import string, json

# @dp.message_handler() #Пустой handler должен быть в конце
async def answer_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
        .intersection(set(json.load(open('censorsip.json')))): #Можно не пистать !='', потому что ''=False
        await message.reply('Маты запрещены.')
        await message.delete()

def register_handler_other(dp : Dispatcher):
    dp.register_message_handler(answer_send)