from consult_prices import get_dolar, get_pesos

def dolar_to_real(original_price):
  dolar = get_dolar()
  converted_price = original_price * dolar
  return converted_price

def pesos_to_real(original_price):
  pesos = get_pesos()
  converted_price = original_price * pesos
  return converted_price
