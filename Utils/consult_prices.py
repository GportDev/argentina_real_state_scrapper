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

  dolar_today = browser.title.split()[1]
  return dolar_today

def get_pesos():
  browser.get('https://www.google.com/finance/quote/ARS-BRL?hl=pt')
  sleep(1)
  content = BeautifulSoup(browser.page_source, 'html.parser')

  pesos_today = browser.title.split()[1]
  return pesos_today