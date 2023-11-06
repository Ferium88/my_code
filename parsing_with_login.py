from requests import Session # Для сохранения файлов cookie
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.chrome}

work = Session()

work.get("https://quotes.toscrape.com", headers=headers)

response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

token = soup.find("form").find