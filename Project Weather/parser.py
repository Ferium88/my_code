import requests
from telebot import TeleBot
from telebot.types import Message
from time import sleep
from utils import welcome_keyboard, weather_keyboard

api = ("b6683e77227aa69b13b71e3818fd1162")

bot = TeleBot('6604274757:AAFG13cd00Vwt8CqsPAvAvp4Hp6pVx48O7w')




@bot.message_handler(commands=["start"])
def welcome(message: Message):
    keyboard = welcome_keyboard()
    bot.send_message(message.from_user.id, "Выбери один из вариантов:", reply_markup=keyboard)


@bot.message_handler(commands=['weather'])
def main(message: Message):
    keyboard = weather_keyboard()
    msgi = bot.send_message(message.from_user.id, "Введите название города: ", reply_markup=keyboard)
    bot.register_next_step_handler(msgi, city_user)
def city_user(message: Message):
    city = message.text
    if message.text != "/cancel":
        get_weather(city, api, message)
    elif message.text == "/cancel":
        bot.reply_to(message, "Отменино")
        sleep(0.5)
        return welcome(message)
def get_weather(city, api, message):
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
        temp = (int(inf["main"]["temp"]))
        temp_round = round(temp, 1)
        pressure = inf["main"]["pressure"]
        humidity = inf["main"]["humidity"]
        pogoda = inf["weather"][0]["main"]
        if pogoda in emodji_weather:
            pogoda_em = emodji_weather[pogoda]
        else:
            pogoda_em = "Я не знаю погоду("
        bot.reply_to(message,f"Температура: {temp_round}°C, {pogoda_em}\nДавление: {pressure} мм.рт.ст.\nВлажность: {humidity}%")
        sleep(1)
        main(message)
    except KeyError as error:
            bot.reply_to(message, "Неверное название города.")
            sleep(1)
            main(message)





if __name__ == "__main__":
    bot.polling()
