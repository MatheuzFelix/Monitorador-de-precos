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

class Consulta:
    def __init__(self,driver):
        driver = driver

        # elementos do site da Magazine
        self.inputBusca = By.ID, 'input-search'
        self.produtos = By.XPATH, "*//div[@class='sc-iyyVIK gdPMEf']" # Xpath criado com a biblioteca scrapy para acessa todos os preços encontrados na pesquisa 
        self.VlrdoProduto = By.XPATH, "*//div[@class='sc-hKwDye hBjQcp sc-JEhMO epMUid']" # Xpath criado com a biblioteca scrapy para ter acesso a todos os produtos do site
        
    def magazineLuiza(self):
        #definindo algumas variaveis
        self.url = driver.current_url
        self.precoTag = 'p'
        self.precoClasse = "sc-kDTinF zuoFI sc-dcgwPl bvdLco"
        self.produtoTag ='div'
        self.produtoClasse ='sc-iyyVIK gdPMEf'

        #acessando site da magazine e fazendo a pesquisa do produto
        driver.get('https://www.magazineluiza.com.br')
        while True:
            try:
                driver.find_element(*self.inputBusca).send_keys('computador')
                driver.find_element(*self.inputBusca).send_keys(Keys.ENTER)
                break
            except: time.sleep(1)
        time.sleep(10)
        self.url = driver.current_url

        if self.scraping_bs4():
            print ('erro ao se conectar com o site.')

    def scraping_bs4(self):
        #encontrando o produto mais baroto encontrado no site com o webscraping do BeautifulSoup
        print(self.url)
        dicionary = {}
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \ (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
        site = requests.get(self.url, headers=headers)
        if 'validate' in site.url:
            return True
        soup= BeautifulSoup(site.content, 'html.parser')
        quant_produtos = len(soup.find_all(self.precoTag, class_=self.precoClasse))
        print(f'foram encontrados {quant_produtos} produtos')
        for i in range(quant_produtos):
            Valor = soup.find_all(self.precoTag, class_=self.precoClasse)[i].get_text()
            Valor = Valor.replace('R$','')
            index = Valor.find(',')
            preco = Valor[:index]
            preco = preco.replace('.','')
            listaPrecos = {
                i:int(preco),
            }
            dicionary.update(listaPrecos)
        minimo = min(dicionary, key=dicionary.get)
        Valor = soup.find_all(self.precoTag, class_=self.precoClasse)[minimo].get_text()
        melhorProduto = soup.find_all(self.produtoTag, class_=self.produtoClasse)[minimo].get_text()
        print(f'o produto mais barato encontrado no site foi: {melhorProduto} esta na promoção por {Valor}')
executar = Consulta(driver)

executar.magazineLuiza()

