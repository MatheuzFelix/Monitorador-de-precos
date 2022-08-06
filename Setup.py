from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver


#Configurando e Atualizando o webdriver
chrome = service=ChromeService(ChromeDriverManager().install())
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--start-maximized')
options_chrome.add_argument('--log-level=3')
driver = webdriver.Chrome(service=chrome, options=options_chrome)

driver.get('https://www.google.com.br')