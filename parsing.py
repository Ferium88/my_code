import requests
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.chrome}


def get_url():
    for number in range(1, 8):
        url = (f"https://scrapingclub.com/exercise/list_basic/?page={number}")

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, features="lxml")

        model = soup.find("div", class_="grid grid-cols-1 gap-4 sm:grid-cols-3")
        model2 = model.findAll("div", class_="w-full rounded border")
        for i in model2:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url

for card_url in get_url():
    response = requests.get(card_url, headers=headers)
    sleep(3)
    soup = BeautifulSoup(response.content, features="lxml")

    data = soup.find("div", class_="my-8 w-full rounded border")
    name = data.find("h3", class_="card-title").text
    price = data.find("h4", class_="my-4 card-price").text
    description = data.find("p", class_="card-description").text
    img_url = "https://scrapingclub.com" + data.find("img").get("src")
    print(f"{name} - {price}, {description} Фото: {img_url}. Ссылка: {card_url}")









