from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

from conversor import pesos_to_real, dolar_to_real

options = Options()
options.add_argument('window-size=360,780')

browser = webdriver.Chrome(options=options)

index = 1

# Access URL
URL = 'https://www.zonaprop.com.ar/departamentos-alquiler-palermo-con-cocinas-2-ambientes-30-60-m2-cubiertos-orden-precio-ascendente.html'
browser.get(URL)
sleep(2)

#Convert content to HTML
content = BeautifulSoup(browser.page_source, 'html.parser')

# Take all the properties
properties = content.find('div', attrs={'class': 'postings-container'})

#find all cards in the properties div
cards = properties.find_all('div', attrs={'data-posting-type': 'PROPERTY'})

def price_converter(price):
  
    price_currency = price.split()[0]
    
    if price_currency == "USD":
      price_number = float(price.split()[1])
      converted_price = dolar_to_real(price_number)
    else:
      price_number = float(price.split()[1])
      converted_price = pesos_to_real(price_number)
    return converted_price
  
def expenses_converter(expenses):
    if expenses == None:
      converted_expenses = 0
    else:
      expenses = expenses.text.replace(".", "")
      converted_expenses = pesos_to_real(float(expenses.split()[1]))
    return converted_expenses
  
def print_infos(expenses):
  print(f'========== {index}ª ==========')
  print(f'ID: {property_id}')
  print(f'Foto: {first_image}')
  print(f'Endereço: {address.text}, {neighborhood.text}, Buenos Aires')
  print(f'Preço total: R$ {total_amount:.2f}')
  
  if expenses == 0:
    print(f'Aluguel: R$ {converted_price:.2f}, Sem despesas descritas')
  else:
    print(f'Aluguel: R$ {converted_price:.2f} + Despesas: R$ {converted_expenses :.2f}')
    
  print(f'Tamanho: {total_area.text}total, {util_area.text}cobertos.')
  print(f'Ambientes: {rooms.text}')
  print(f'Dormitórios: {bedrooms.text}')
  print(f'Link: {link} \n')

for card in cards:
  property_id = card['data-id']

  image_div = card.find('div', attrs={'data-qa': 'POSTING_CARD_GALLERY'})
  sleep(0.5)
  first_image = image_div.find('img')

  link = 'zonaprop.com.ar' + card['data-to-posting']

  neighborhood = card.find('div', attrs={'data-qa': 'POSTING_CARD_LOCATION'})
  address = neighborhood.previous_sibling

  price = card.find('div', attrs={'data-qa': 'POSTING_CARD_PRICE'}).text.replace(".", "")
  converted_price = price_converter(price)
 
  expenses = card.find('div', attrs={'data-qa': 'expensas'})
  converted_expenses = expenses_converter(expenses)

  total_amount = converted_price + converted_expenses

  features = card.find('div', attrs={'data-qa': 'POSTING_CARD_FEATURES'}).findAll('span')
  
  total_area = features[1]
  util_area = features[3]

  rooms = features[5]

  bedrooms = features[7]
  
  print_infos(converted_expenses)
  
  index = index +1
