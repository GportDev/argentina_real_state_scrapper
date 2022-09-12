from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

options = Options()
options.add_argument('window-size=360,780')
# options.add_argument('--headless')

# Qual browser será aberto?
browser = webdriver.Chrome(options=options)

# Acessar URL
browser.get('https://www.zonaprop.com.ar/departamentos-alquiler-palermo-con-cocinas-2-ambientes-30-60-m2-cubiertos-orden-precio-ascendente.html')
sleep(2)

content = BeautifulSoup(browser.page_source, 'html.parser')

# Pegar a lista da primeira página
properties = content.find('div', attrs={'class': 'postings-container'})

#Card de apartamento
property_card = properties.find('div', attrs={'data-posting-type': 'PROPERTY'})

#Endereço
property_neighborhood = property_card.find('div', attrs={'data-qa': 'POSTING_CARD_LOCATION'})
property_address = property_neighborhood.previous_sibling

#Preço
property_price = property_card.find('div', attrs={'data-qa': 'POSTING_CARD_PRICE'})
property_expenses = property_card.find('div', attrs={'data-qa': 'expensas'})
# função que converte o valor para reais

#Tamanho
property_features = property_card.find('div', attrs={'data-qa': 'POSTING_CARD_FEATURES'}).findAll('span')
property_total_area = property_features[1]
property_util_area = property_features[3]

#Ambientes
property_rooms = property_features[5]

#Dormitorios
property_bedrooms = property_features[7]

# property_card = [apartment for apartment in property_cards]

print(f'Endereço: {property_address.text}, {property_neighborhood.text}, Buenos Aires' )
print(f'Preço: ')
print(f'Tamanho: {property_total_area.text}total, {property_util_area.text}cobertos.' )
print(f'Ambientes: {property_rooms.text}' )
print(f'Dormitórios: {property_bedrooms.text}' )
# Iterar cada card com o imóvel
  # Receber informações
    # Primeira foto
    # Link
    # Endereço OK
    # Valor total (Aluguel+despesas) convertido para real --OK
    # Metragem OK
    # Qtd de ambientes OK
    # Qtd de dormitórios (se tiver) OK
  # Ações
    # Salvar resultados no banco
    # Verificar distância do CBC e da Faculdade de medicina
