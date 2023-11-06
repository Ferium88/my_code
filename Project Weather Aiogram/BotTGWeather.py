from time import sleep
import requests
from aiogram import Bot, Dispatcher, executor
from aiogram.types import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage



api = ("b6683e77227aa69b13b71e3818fd1162")


bot = Bot('6604720616:AAEu4b2t34TYkTGP8F1pGQI9PapslZLQ-h4')

dp = Dispatcher(bot=bot, storage=MemoryStorage())


def get_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Погода")
    keyboard.add(button)

    return keyboard

def get_cancel() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Отмена")
    keyboard.add(button)

    return keyboard
class Form(StatesGroup):
    city = State()

@dp.message_handler(commands=["start"])
async def welcome(message: Message) -> None:
    await message.answer("Выбери один из вариантов:",
                         reply_markup=get_keyboard())

@dp.message_handler(Text(equals="Отмена", ignore_case=True), state="*")
async def cancel(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.reply("Отменино",
                        reply_markup=get_keyboard())
    await state.finish()
    await welcome(message)


@dp.message_handler(Text(equals="Погода", ignore_case=True), state=None)
async def city_start(message: Message) -> None:
    await Form.city.set()
    await message.answer(text="Введите название города: ", reply_markup=get_cancel())

@dp.message_handler(state=Form.city)
async def city_chosen(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await get_weather(api, data['city'], message)
    await state.finish()
    await city_start(message)

async def get_weather(api, city, message: Message):
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric")
    emodji_weather = {
        "Clouds": "Облачно \U00002601",
        "Clear": "Ясно \U00002600",
        "Rain": "Дождь \U0001F327",
        "Snow": "Снег \U00002744",
        "Mist": "Туман \U0001F32B",
        "Thunderstorm": "Гроза \U0001F329",
        "Drizzle": "Дождь \U0001F327"

    }
    try:
        response = requests.get(url)
        inf = response.json()
        print(inf)
        temp = (int(inf["main"]["temp"]))
        temp_round = round(temp, 1)
        pressure = inf["main"]["pressure"]
        humidity = inf["main"]["humidity"]
        pogoda = inf["weather"][0]["main"]
        if pogoda in emodji_weather:
            pogoda_em = emodji_weather[pogoda]
        else:
            pogoda_em = "Я не знаю погоду("
        await message.reply(f"Температура: {temp_round}°C, {pogoda_em}\nДавление: {pressure} мм.рт.ст.\nВлажность: {humidity}%")
        sleep(1)
    except KeyError as error:
        print(error)
        await message.reply(text="Неверное название города.")


if __name__ == "__main__":
    executor.start_polling(dp)
