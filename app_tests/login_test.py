from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://127.0.0.1:3901')
username_input = driver.find_element(By.NAME ,"username")
password_input = driver.find_element(By.NAME ,"password")

username_input.send_keys("admin")
password_input.send_keys("admin123")

login_button = driver.find_element(By.NAME ,"login_button")

login_button.click()
time.sleep(5)

welcome_text = driver.find_element(By.ID ,"welcome_massege").text

assert "welcome, admin" in welcome_text 
#if "welcome, admin" in welcome_text :
#    print("login passed !")
#else:
#    print("login failed !!")

driver.quit()
