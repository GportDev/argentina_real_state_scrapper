from consult_prices import get_dolar, get_pesos

def dolar_to_real(original_price):
  dolar_price = int(get_dolar())
  real_price = original_price * dolar_price

def pesos_to_real(original_price):
  pesos_price = int(get_pesos())
  real_price = original_price * pesos_price