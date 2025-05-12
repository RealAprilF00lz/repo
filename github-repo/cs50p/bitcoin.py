import sys
import requests

try:
    n=float(sys.argv[1])
except ValueError:
    sys.exit('Argument is not a number')
except IndexError:
    sys.exit('Missing argument')

try:
    response=requests.get('https://api.coincap.io/v2/assets/bitcoin')
except:
    sys.exit('Something went wrong when trying to check the current price of bitcoin. Are you connected to the internet?')

price=float(response.json()['data']['priceUsd'])
print(f"${price*n:,.4f}")
