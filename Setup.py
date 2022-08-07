from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import messagebox
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

    def magazineLuiza (self):
        #acessando site da magazine e fazendo a pesquisa do produto
        driver.get('https://www.magazineluiza.com.br')
        while True:
            try:
                driver.find_element(*self.inputBusca).send_keys('Cadeira gamer')
                driver.find_element(*self.inputBusca).send_keys(Keys.ENTER)
                break
            except: time.sleep(1)
        time.sleep(10)
        #Lendo os produtos encontrados e escolhendo o melhor
        QuantProdutos = len(driver.find_elements(*self.VlrdoProduto))
        listaValores = {
        }
        for i in range (QuantProdutos):
            vlr = driver.find_elements(*self.VlrdoProduto)[i].text
            comparador = vlr[3:8]
            comparador = comparador.replace('.','')
            comparador = comparador.split(",")
            comparador = comparador[0]
            dicionary = {
                i:comparador,
            }
            listaValores.update(dicionary)
        minimo = min(listaValores, key= listaValores.get)

        #Mensagem exibindo o melhor produto do site
        barato = driver.find_elements(*self.produtos)[minimo].text
        messagebox.showinfo('Produto mais barato encontrado',\
            barato)

executar = Consulta(driver)

executar.magazineLuiza()

