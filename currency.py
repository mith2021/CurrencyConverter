import requests

API_KEY = 'fca_live_ksZv6T3XcBdRBWnUg2IuTyBgEMQuanjb45M8hNSK'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR" , "AUD", "INR"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("invalid currency")
        return None

while True:
    base =  input("Enter the base currency (q for quit): ").upper()
    if base == "Q":
        break
    for i, j in enumerate(CURRENCIES, 1):
        print(f"{i}. {j}")
    convert_to = input("what currency would you like to convert to? ").upper()
    conversion_amt = int(input("What amount do you want to convert?  "))

    data = convert_currency(base)
    conv_to = convert_currency(convert_to)
    if (not data) or (not conv_to):
        continue

    if input("Do you want to see other currency values right now?(y/n) ").lower() == 'y':
        del data[base]
        for ticker, value in data.items():
            print(f"{ticker}: {value}")
        
        multiplier = data[convert_to]
        converted_amt = (conversion_amt * multiplier)
        print(f"{conversion_amt} {base} is {converted_amt:.2f} {convert_to}")
    else:
        multiplier = data[convert_to]
        converted_amt = (conversion_amt * multiplier)
        print(f"{conversion_amt} {base} is {converted_amt:.2f} {convert_to}")