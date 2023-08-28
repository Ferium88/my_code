import requests
from bs4 import BeautifulSoup
import json


def sait(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="xml")
    print(soup)

sait("https://afisha.yandex.ru/moscow/concert")