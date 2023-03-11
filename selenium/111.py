from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service('chromedriver.exe')
# chrome_options = Options('chromedriver.exe')
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service = service)

url = 'https://www.scrapethissite.com/login/'

driver.get(url)

my_element = driver.find_element(By.ID, "email")
my_element.send_keys("111@email.com")

my_element = driver.find_element(By.ID, "password")
my_element.send_keys("111")

my_element.send_keys(Keys.ENTER)

# Capturing alert message.    

alert = driver.switch_to.alert.accept()
text = alert.text()
print(text)
