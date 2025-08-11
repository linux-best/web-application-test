from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

User = "username"
passwd = "password"
Condition = "You have logged in as 'admin'" 

chrome_options = Options()

# Add any desired Chrome options, e.g., headless mode for Jenkins
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox") # Important for Jenkins
chrome_options.add_argument("--disable-dev-shm-usage") # Important for Jenkins
chrome_options.binary_location = "/usr/bin/google-chrome-stable"

# Replace with the actual path to your chromedriver executable
service_driver = Service("/usr/local/bin/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service_driver , options=chrome_options)

print("1")

def driver_quit():
    driver.quit()

def Bute_Force(new_paassword):
    passwd_new = "password_new"
    passwd_conf = "password_conf"
    WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.XPATH ,"//*[contains(text(),'CSRF')]"))
    )
    brute_field = driver.find_element(By.XPATH ,"//*[contains(text(),'CSRF')]")
    brute_field.click()
    print("4")
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,passwd_new))
    )
    pass_new = driver.find_element(By.NAME ,passwd_new)
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,passwd_conf))
    )
    pass_old = driver.find_element(By.NAME ,passwd_conf)

    pass_old.send_keys(new_paassword)
    pass_new.send_keys(new_paassword)

    print("5")

    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,"Change"))
    )
    login_button = driver.find_element(By.NAME ,"Change")
    login_button.click()

    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID ,"main_body"))
    )    
    welcome_text = driver.find_element(By.ID ,"main_body").text

    if "Password Changed." in welcome_text :
        print("Password Changed !")
    else:
        print("Password Failed to Change !!")

def login_test(login_user="admin",login_passwd="123"):
    assert User == "username"
    assert passwd == "password"

    driver.get('http://127.0.0.1:8081/login.php')
    print(driver.title)
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,User))
    )
    username_input = driver.find_element(By.NAME ,User)
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,passwd))
    )
    password_input = driver.find_element(By.NAME ,passwd)

    print("2")

    username_input.send_keys(login_user)
    password_input.send_keys(login_passwd)

    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,"Login"))
    )
    login_button = driver.find_element(By.NAME ,"Login")

    login_button.click()
    time.sleep(5)
  
    welcome_text = driver.find_element(By.ID ,"main_body").text
    print(welcome_text)

    print("3")

    assert "Welcome to Damn Vulnerable Web Application!" in welcome_text
    assert Condition in welcome_text
    
    if "Welcome to Damn Vulnerable Web Application!" in welcome_text :
        print("login passed !")
    else:
        print("login failed !!")
    Brute_Force(new_password="amir")

login_test()
driver_quit()
