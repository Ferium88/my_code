from telebot.types import *
def welcome_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    button_1 = KeyboardButton("/weather")

    keyboard.add(button_1)
    return keyboard


def weather_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    button_1 = InlineKeyboardButton("/cancel")

    keyboard.add(button_1)
    return keyboard