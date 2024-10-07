from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Open the Cookie Clicker game
driver.get('https://orteil.dashnet.org/cookieclicker/')

# Wait for the language selection and click 'English'
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Wait for the cookie element to be present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'bigCookie'))
)

# Click the cookie repeatedly
try:
    while True:
        cookie = driver.find_element(By.ID, 'bigCookie')
        cookie.click()
        time.sleep(0.1)  # Adjust the sleep duration as needed

except KeyboardInterrupt:
    print("Stopped clicking the cookie.")

# Optional: Close the driver after use
driver.quit()
