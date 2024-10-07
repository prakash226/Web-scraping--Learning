import requests
from bs4 import BeautifulSoup


def filter_products_by_name(url, user_input):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, 'lxml')

  products = []
  for product in soup.find_all('div', class_="sg-col-inner"):
    product_name = product.find('span', class_="a-size-medium a-color-base a-text-normal")
    product_price = product.find('span', class_="a-price-whole")

    if product_name and product_price:
      
      if user_input.lower() in product_name.text.strip().lower():
        products.append({
          'name': product_name.text.strip(),
          'price': product_price.text.strip() + '/-'
        })

  return products


url = 'https://www.amazon.in/s?k=android+mobile+5g&crid=1PNO9MLHBUSUT&sprefix=%2Caps%2C178&ref=nb_sb_ss_recent_1_0_recent'
user_input = input('Enter the Mobile name (or part of the name): ').lower()

print('Fetching...')
filtered_products = filter_products_by_name(url, user_input)

if filtered_products:
  print('Found products:')
  for product in filtered_products:
    print(f'Mobile Name: {product["name"]}')
    print(f'Price: {product["price"]}')
    print('-' * 50)
  print(f'Total items found: {len(filtered_products)}')
else:
  print('No products matching the criteria were found.')
