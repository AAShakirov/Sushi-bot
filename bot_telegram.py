from aiogram.utils import executor
from create_bot import dp
from handlers import admin, client, other
from keyboards import client_kb

async def on_startup(_):
    print('The bot has started.')

client.register_handlers_client(dp)
other.register_handler_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)