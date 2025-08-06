from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()

# Add any desired Chrome options, e.g., headless mode for Jenkins
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox") # Important for Jenkins
chrome_options.add_argument("--disable-dev-shm-usage") # Important for Jenkins
chrome_options.binary_location = "/usr/bin/google-chrome-stable"

# Replace with the actual path to your chromedriver executable
service_driver = Service("/usr/local/bin/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service_driver , options=chrome_options)

driver.get('http://127.0.0.1:8081/login.php')
print(driver.title)
username_input = driver.find_element(By.NAME ,"username")
password_input = driver.find_element(By.NAME ,"password")

username_input.send_keys("admin")
password_input.send_keys("password")

login_button = driver.find_element(By.NAME ,"Login")

login_button.click()
time.sleep(5)

welcome_text = driver.find_element(By.ID ,"welcome_massege").text

#assert "welcome, admin" in welcome_text 
if "welcome, admin" in welcome_text :
    print("login passed !")
else:
    print("login failed !!")

driver.quit()
