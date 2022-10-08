from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')

browser = webdriver.Chrome(options=options)

def get_dolar():
  browser.get('https://www.google.com/finance/quote/USD-BRL')
  sleep(1)
  content = BeautifulSoup(browser.page_source, 'html.parser')

  get_dolar_price = browser.title.split()[1].replace(",", ".")
  dolar_today = float(get_dolar_price)
  return dolar_today

def get_pesos():
  browser.get('https://www.google.com/finance/quote/ARS-BRL?hl=pt')
  sleep(1)
  content = BeautifulSoup(browser.page_source, 'html.parser')

  get_pesos_price = browser.title.split()[1].replace(",", ".")
  pesos_today = float(get_pesos_price)
  return pesos_today

