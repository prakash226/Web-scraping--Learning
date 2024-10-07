from bs4 import BeautifulSoup
import requests


def fetch_mobiles(user):
    count = 0

    # Android phone
    android_brands = ['samsung', 'oneplus', 'xiaomi', 'vivo', 'oppo', 'realme', 'google', 'motorola', 'redmi']

    for i in range(2, 12):  # 2 to 11
        url = f'https://www.amazon.in/s?k=mobiles&page={i}&crid=J5MYU0GPT6ZM&sprefix=mobile%2Caps%2C211&ref=nb_sb_noss_1'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }
        
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'lxml')
            div_tag = soup.find_all('div', class_="sg-col-inner")
            print('*'*50)
            print(f'Fetching Data from page {i}...')
            print('*'*50)
            
            for tag in div_tag:
                mobile_name = tag.find('span', class_="a-size-medium a-color-base a-text-normal")
                price_tag = tag.find('span', class_="a-price-whole")
                deliver = tag.find('span', class_="a-color-base a-text-bold")
                
                if mobile_name and price_tag and deliver:
                    count += 1
                    mobile_name_text = mobile_name.text.lower()

                    # Check based on user input (iPhone or Android)
                    if user == 'i' and 'iphone' in mobile_name_text:
                        print(f"MobileName: {mobile_name.text.strip()}")
                        print(f"Price: {price_tag.text.strip()}/-")
                        print(f"Delivery By: {deliver.text.strip()}")
                        print('----' * 10)
                    
                    elif user == 'a':
                        # Check if the mobile belongs to an Android brand
                        if any(brand in mobile_name_text for brand in android_brands):
                            print(f"MobileName: {mobile_name.text.strip()}")
                            print(f"Price: {price_tag.text.strip()}/-")
                            print(f"Delivery By: {deliver.text.strip()}")
                            print('----' * 10)
        except Exception as e:
            print(f"Failed to retrieve data from page {i}: {e}")

    print(f'Total mobiles fetched: {count}')


# Get user choice for iPhone or Android
user = input('iPhone or Android, Type I or A: ').lower()
if user not in ['i', 'a']:
    print("Invalid choice! Please type 'I' for iPhone or 'A' for Android.")
else:
    fetch_mobiles(user)


