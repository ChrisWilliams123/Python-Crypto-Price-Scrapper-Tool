#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import json

def get_price(crypto):
    url = "https://coinmarketcap.com/currencies/" + crypto + "/"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    data = soup.find('script', type="application/ld+json" )
    coin_data = json.loads(data.contents[0])
    ticker, price=coin_data['currency'], coin_data['currentExchangeRate']['price']
    return str(ticker), str(price)


def main():
    filename = 'list_of_cryptos'
    with open(filename) as file:
        coins = [line.strip() for line in file]
    
    entries=[]
    for coin in coins:
        try:
            entries.append(get_price(coin))
        except:
            try:
                entries.append(get_price(coin))
            except:
                entries.append('unknown, 0')


    with open('crypto_prices','w') as file:
        for entry in entries:
            file.write(f"{entry[0]}, {entry[1]}\n")        

if __name__ == '__main__':
    main()
