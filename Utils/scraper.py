from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
from converters import dolar, pesos, rent_converter, expenses_converter

def create_property():
  apartment = {
    "id": f'{property_id}',
    "first_photo": f'{first_image}',
    "address": f'{address.text}, {neighborhood.text}, Buenos Aires',
    "total_amount": f'R$ {total_amount:.2f}',
    "rent": f'{converted_rent:.2f}',
    "expenses": f'{converted_expenses:.2f}',
    "total_area": f'{total_area.text}',
    "util_area": f'{util_area.text}',
    "rooms": f'{rooms.text}',
    "bedrooms": f'{bedrooms.text}',
    "link": f'{link}'
  }
  return apartment

  
apartments = []

#Scrapper.py
options = Options()
options.add_argument('window-size=360,780')

browser = webdriver.Chrome(options=options)

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

for card in cards:
  property_id = card['data-id']

  image_div = card.find('div', attrs={'data-qa': 'POSTING_CARD_GALLERY'})
  sleep(0.5)
  first_image = image_div.find('img')

  link = 'zonaprop.com.ar' + card['data-to-posting']

  neighborhood = card.find('div', attrs={'data-qa': 'POSTING_CARD_LOCATION'})
  address = neighborhood.previous_sibling

  price = card.find('div', attrs={'data-qa': 'POSTING_CARD_PRICE'}).text.replace(".", "")
  converted_rent = rent_converter(price)

  expenses = card.find('div', attrs={'data-qa': 'expensas'})
  converted_expenses = expenses_converter(expenses)

  total_amount = converted_rent + converted_expenses

  features = card.find('div', attrs={'data-qa': 'POSTING_CARD_FEATURES'}).findAll('span')
  
  total_area = features[1]
  util_area = features[3]

  rooms = features[5]

  bedrooms = features[7]
  
  apartments.append(create_property())
  
print(apartments)
