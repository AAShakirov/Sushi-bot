from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/operating_mode')
b2 = KeyboardButton('/place')
b3 = KeyboardButton('/menu')
b4 = KeyboardButton('Share my phone number', request_contact=True)
b5 = KeyboardButton('Share my location', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.row(b1, b2, b3).add(b4).insert(b5)