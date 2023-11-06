import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys





def main():
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    s = Service(executable_path='C:\Python Code\chromedriver-win64\chromedriver.exe', headers=headers)
    driver = webdriver.Chrome(service=s)
    url = f"https://postupi.online/vuzi/"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")


    try:
        user_city = input("Город: ").capitalize()
        driver.maximize_window()
        driver.get('https://postupi.online/vuzi/')
        time.sleep(3)

        city = driver.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/header/div[1]/div[3]/div/div/div[1]/a/span').click()
        city = driver.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/header/div[1]/div[3]/div/div/div[1]/div/p[2]').click()
        time.sleep(1)
        city = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/form/div[1]/input[2]')
        city.send_keys(user_city)
        city = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/form/div[2]/div[2]/ul/li[1]/span/span[2]/span').click()
        time.sleep(2)
        number = 1

        driver.execute_script("window.scrollTo(0, 5600)")
        time.sleep(3)
        while 0 != 1:
            city = driver.find_element(By.CSS_SELECTOR, 'main_form > div.content-wrap > div.content > div.list-cover > div:nth-child(3) > div > a.page_pointer.forward').click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 5600)")
            number += 1
        print(number)

        # main_form > div.content-wrap > div.content > div.list-cover > div:nth-child(3) > div > a.page_pointer.forward

        time.sleep(3)
    except Exception as error:
        print(error)
    finally:
        driver.close()
        driver.quit()










if __name__ == "__main__":
    main()
