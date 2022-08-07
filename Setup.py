from itertools import product
from urllib import response
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import scrapy
import time


#Configurando e Atualizando o webdriver
chrome = service=ChromeService(ChromeDriverManager().install())
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--start-maximized')
options_chrome.add_argument('--log-level=3')
driver = webdriver.Chrome(service=chrome, options=options_chrome)


class Consulta:
    def __init__(self,driver):
        driver = driver

        # elementos do site da Magazine
        self.inputBusca = By.ID, 'input-search'
        self.produtos = By.XPATH, "*//div[@class='sc-iyyVIK gdPMEf']"

    def magazineLuiza (self):
        driver.get('https://www.magazineluiza.com.br')
        while True:
            try:
                driver.find_element(*self.inputBusca).send_keys('Sansung a23')
                driver.find_element(*self.inputBusca).send_keys(Keys.ENTER)
                break
            except: time.sleep(1)
        time.sleep(10)
        url = driver.current_url
        response = requests.get(url)
        print(response)
        produtos = driver.find_elements(*self.produtos)[1].text
        print(produtos)

executar = Consulta(driver)

executar.magazineLuiza()

