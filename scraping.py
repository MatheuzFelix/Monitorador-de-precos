from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from tkinter import messagebox
import requests
from selenium import webdriver
import time

#Configurando e Atualizando o webdriver
chrome = service=ChromeService(ChromeDriverManager().install())
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--start-maximized')
options_chrome.add_argument('--log-level=3')
driver = webdriver.Chrome(service=chrome, options=options_chrome)

class Scraping:
    def __init__(self,driver):
        driver = driver

        #Pagina de pesquisa
        self.searche = By.NAME, 'conteudo'
        self.btnSearche = By.XPATH, '//*[@id="rsyswpsdk"]/div/header/div[1]/div[1]/div/div[1]/form/button'

        #Raspagem de dados
        self.produto = By.XPATH, "*//div[@class='product-info__Container-sc-1or28up-0 cdKgxb']//h3"
        self.preco = By.XPATH, "*//div[@class='price-info__Wrapper-sc-1xm1xzb-0 clqFWq inStockCard__PriceInfoUI-sc-1ngt5zo-2 QfpEc']//span[@class='src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-h6xgft-1 ctBJlj price-info__ListPriceWithMargin-sc-1xm1xzb-2 liXDNM']"
        self.btnprox = By.XPATH, '//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div/ul/li[10]/button'


    def start(self):
        self.search_page()

    def search_page(self):
        last_Page = 'disabled=""'
        driver.get('https://www.americanas.com.br')

        driver.find_element(*self.searche).send_keys('samsung monitor 21 polegadas')
        driver.find_element(*self.btnSearche).click()

        time.sleep(10)
        self.getting_information()
        while True:
            try:
                if last_Page in driver.find_element(By.XPATH, '//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div/ul/li[10]').get_attribute('innerHTML'):
                    print('last page')
                    break
                else:
                    driver.find_element(*self.btnprox).click()
                    self.getting_information()
            except:
                time.sleep(1)
    
    def getting_information(self):
        quant = len(driver.find_elements(*self.produto))
        for i in range(quant): 
            produto = driver.find_elements(*self.produto)[i].text
            vlr = driver.find_elements(*self.preco)[i].text

            print(produto)
            print(vlr)
        

executar = Scraping(driver)

executar.start()
