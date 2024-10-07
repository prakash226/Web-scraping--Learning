from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com/')
time.sleep(2)

search = driver.find_element(By.NAME, 'q')
search.send_keys('Make My Trip')
search.send_keys(Keys.ENTER)
time.sleep(3)

element = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/div/div/div/div[2]/cite')
element.click()
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-cy="closeModal"]')))
    
close_button = driver.find_element(By.CSS_SELECTOR, 'span[data-cy="closeModal"]')
close_button.click()  # Click the close button

hotels_link = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="SW"]/div[1]/div[2]/div/div/nav/ul/li[2]/span/a')))
hotels_link.click()
time.sleep(5)

search_press = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="hsw_search_button"]')))
search_press.click()
time.sleep(5)

# Wait for the hotel listing container to be present
hotel_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'infinite-scroll-component ')))
# Initialize a list to hold hotel information
hotel_info = []

for hotel in hotel_elements:
        # Extract hotel name
    name_element = hotel.find_element(By.XPATH, '//*[@id="hlistpg_hotel_name"]')
    hotel_name = name_element.text 
    
        # Extract hotel price
    price_element = hotel.find_element(By.XPATH, '//*[@id="hlistpg_hotel_shown_price"]')
    hotel_price = price_element.text 

        # Extract hotel rating
    rating_element = hotel.find_element(By.XPATH, '//*[@id="hlistpg_hotel_user_rating"]/span')
    hotel_rating = rating_element.text

        # Store the extracted information in a dictionary
    hotel_info.append({
        'name': hotel_name,
        'price': hotel_price,
        'rating': hotel_rating
    })

    # Print the extracted hotel information
    for info in hotel_info:
        print(info)
        
# Optional wait to observe the output
time.sleep(5)
