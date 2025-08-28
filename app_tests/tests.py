from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException
from loguru import logger
import sys
import time

# Variable Scope
User = "username"
passwd = "password"
Condition = "You have logged in as 'admin'" 
File_Log = "/home/javande/web-application-test/app_tests/Application_Test.log"
chrome_options = Options()

# Logging-Configuration
logger.add(sys.stdout ,
            level="DEBUG" ,
            #format="<yellow>{time}</yellow> -- {level} -- <level>{message}</level> -- <green>{extra}</green>",
            format="{time:MMMM D, YYYY - HH:mm:ss} -- {level} -- {message} -- {extra}",
            colorize=True,
            filter=lambda record: record["level"].name != "TRACE")
logger.add(File_Log ,
            level="TRACE" ,
            format="{time: MMMM D, YYYY - HH:mm:ss} -- {level} -- {message} -- {extra}",
            colorize=True,
            filter=lambda record: record["level"].name == "TRACE")

# Add any desired Chrome options, e.g., headless mode for Jenkins
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox") # Important for Jenkins
chrome_options.add_argument("--disable-dev-shm-usage") # Important for Jenkins
chrome_options.binary_location = "/usr/bin/google-chrome-stable"

# Replace with the actual path to your chromedriver executable
service_driver = Service("/usr/local/bin/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service_driver , options=chrome_options)

with logger.contextualize(Drver_Path="/usr/local/bin/chromedriver-linux64/chromedriver"):
        logger.success("Driver Created !")

@logger.catch("ERROR")
def driver_quit():
    driver.quit()
    return "Done !"

@logger.catch("ERROR")
def Brute_Force_Test_section(username,password):
    global User
    global passwd

    with logger.contextualize(test_stage="Brute_Force_Test_section"):
        logger.info("Test started *")

    WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.XPATH ,"//*[contains(text(),'Brute Force')]"))
    )
    brute_field = driver.find_element(By.XPATH ,"//*[contains(text(),'Brute Force')]")
    brute_field.click()

    with logger.contextualize(Path="DVWA-application/Brute Force"):
        logger.info("Section Located !")

    WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.NAME ,User))
    )
    username_input = driver.find_element(By.NAME ,User)
    WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.NAME ,passwd))
    )
    password_input = driver.find_element(By.NAME ,passwd)
    username_input.send_keys(username)
    password_input.send_keys(password)

    WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.NAME ,"Login"))
    )
    login_button = driver.find_element(By.NAME ,"Login")
    login_button.click()
    WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.ID ,"main_body"))
    )    
    welcome_text = driver.find_element(By.ID ,"main_body").text
    
    with logger.contextualize(Authentication_keys=f"username:{username},password:{password}"):
        logger.success("Access Authurized !")

    # print(welcome_text)
    with logger.contextualize(output="Brute_Force_Test_section"):
        logger.trace(welcome_text)

    if "Welcome to the password protected area admin" in welcome_text :
        return "Welcome to the password protected area admin !"
    else:
        return "access denied !!"

@logger.catch("ERROR")
def CSRF_Test_section(old_password,new_paassword):
    passwd_new = "password_new"
    passwd_conf = "password_conf"
    
    with logger.contextualize(test_stage="CSRF_Test_section"):
        logger.info("Test started *")
    
    WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.XPATH ,"//*[contains(text(),'CSRF')]"))
    )
    brute_field = driver.find_element(By.XPATH ,"//*[contains(text(),'CSRF')]")
    brute_field.click()

    with logger.contextualize(Path="DVWA-application/CSRF"):
        logger.info("Section Located !")
                
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,password_current))
    )
    pass_current = driver.find_element(By.NAME ,password_current)
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,password_new))
    )
    pass_new = driver.find_element(By.NAME ,password_new)
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,password_conf))
    )
    pass_old = driver.find_element(By.NAME ,password_conf)

    pass_current.send_keys(old_password)
    pass_old.send_keys(new_paassword)
    pass_new.send_keys(new_paassword)

    with logger.contextualize(New_Password=new_paassword):
        logger.info("New Password Entered !")

    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,"Change"))
    )
    login_button = driver.find_element(By.NAME ,"Change")
    login_button.click()

    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID ,"main_body"))
    )    
    welcome_text = driver.find_element(By.CLASS_NAME ,"vulnerable_code_area").text
    
    with logger.contextualize(Current_Password=new_paassword):
        logger.success("Passwd Changed !")

    # print(welcome_text)
    with logger.contextualize(output="CSRF_Test_Section"):
        logger.trace(welcome_text)

    with logger.contextualize(tip="CSRF_Test"):
        logger.warning("Make sure to memorize it")

    if "Password Changed." in welcome_text :     
        return "Password Changed !"
    else:
        return "Password Failed to Change !!"

@logger.catch("ERROR")
def login_test_section(login_user,login_passwd):
    assert User == "username"
    assert passwd == "password"

    with logger.contextualize(test_stage="Login_test_section"):
        logger.info("Test started *")

    driver.get('http://127.0.0.1:8081/login.php')
    print(driver.title)

    with logger.contextualize(Web='http://127.0.0.1:8081/login.php'):
        logger.info("Application Reached !")

    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,User))
    )
    username_input = driver.find_element(By.NAME ,User)
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,passwd))
    )
    password_input = driver.find_element(By.NAME ,passwd)

    username_input.send_keys(login_user)
    password_input.send_keys(login_passwd)

    with logger.contextualize(Authentication_keys=f"username:{login_user},password:{login_passwd}"):
        logger.info("Authenticating ..... !")

    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.NAME ,"Login"))
    )
    login_button = driver.find_element(By.NAME ,"Login")

    login_button.click()
    time.sleep(5)

    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID ,"main_body"))
    )
    welcome_text = driver.find_element(By.ID ,"main_body").text
    
    with logger.contextualize(authentication="successful"):
        logger.success("Authenticating Authurized !")    
    
    # print(welcome_text)
    with logger.contextualize(output="login_Test_section"):
        logger.trace(welcome_text)

    assert "Welcome to Damn Vulnerable Web Application!" in welcome_text
    assert Condition in welcome_text
    
    if "Welcome to Damn Vulnerable Web Application!" in welcome_text :
        return "login passed !"
    else:
        return "login failed !!"

#login_test_section(login_user="admin",login_passwd="password") 
#CSRF_Test_section(new_paassword="password")
#Brute_Force_Test_section(username="admin",password="password")
#driver_quit()

