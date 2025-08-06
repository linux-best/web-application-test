from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8081/login.php')
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
