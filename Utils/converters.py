from price_scrapper import get_dolar, get_pesos

dolar = get_dolar()
pesos = get_pesos()

def rent_converter(rent):
    rent_currency = rent.split()[0]
    
    if rent_currency == "USD":
      original_rent = float(rent.split()[1])
      converted_rent = original_rent * dolar
    else:
      original_rent = float(rent.split()[1])
      converted_rent = original_rent * pesos
      
    return converted_rent
  
def expenses_converter(expenses):
    if expenses == None:
      converted_expenses = 0
    else:
      expenses = expenses.text.replace(".", "")
      converted_expenses = float(expenses.split()[1]) * pesos
      
    return converted_expenses