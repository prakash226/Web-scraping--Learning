from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.in/s?k=android+mobile+5g&crid=1UJ8P1BF3THA9&sprefix=android+mobile+5g%2Caps%2C608&ref=nb_sb_noss_1'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
products = soup.find_all('div', class_='sg-col-inner')
count=0
for product in products:
    name_tag = product.find('span', class_="a-size-medium a-color-base a-text-normal")
    #price of the product
    price_tag = product.find('span', class_='a-price-whole')

    if name_tag and price_tag:
        count+=1
        print(f'ProductName: {name_tag.text.strip()}')
        
        print(f'Price: {price_tag.text.strip()}')

print(f'Total found products are: {count}')
