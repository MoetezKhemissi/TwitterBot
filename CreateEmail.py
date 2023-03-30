#Todo 
import undetected_chromedriver as uc
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from fake_useragent import UserAgent
from GeneratePerson import generate_person
import time
import Orm
import time
import random
import string

def slow_type(element, text):
    """Send a text to an element one character at a time with a delay."""
    i = 0
    
    for character in text:
        i= i+1
        if i % 3 == 0:
            delay=random.uniform(0.3, 0.4)
        if i % 3 == 1:
            delay=random.uniform(0.1, 0.2)
        if i % 3 == 2:
                delay=random.uniform(0.2, 0.3)
        if i % 5 ==4:
            delay=random.uniform(0.1, 0.3)
            element.send_keys(random.choice(string.ascii_letters))
            delay=random.uniform(0.1, 0.3)
            element.sendKeys(Keys.BACK_SPACE)
        
        element.send_keys(character)
        time.sleep(delay)
def start_driver_stealth():

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    # options.add_argument("--headless")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    
    return driver
def start_undetected():

    driver = uc.Chrome()
    driver.get("https://www.google.com")

    
    return driver
def consent_screen(driver):
    try:
        time.sleep(1)
        iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/iframe')))
        driver.switch_to.frame(iframe)
        iframe2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/iframe')))
        driver.switch_to.frame(iframe2)

        accept_button= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
        time.sleep(1)
        accept_button.click()
        time.sleep(1)
        driver.switch_to.default_content()
    except:
        print("no consent required")
def signup(driver):
    return 0
driver = start_driver_stealth()
#//*[@id="signup-button"]
url = "https://www.google.com"
test_person = generate_person()

driver.get(url)
consent_screen(driver)
time.sleep(1)
def is_email_available(driver):
    message=""
    message_element=WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[1]/onereg-alias/fieldset/onereg-progress-meter/div[2]/div[3]/pos-form-message/div/span/span')))
    return 0
#--------------GET ALL FIELDS-----------------
'''SignupButton= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signup-button"]'))).click()

#driver.refresh()
email_field= WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[1]/onereg-alias/fieldset/onereg-progress-meter/div[2]/div[2]/div/pos-input[1]/input')))
Gender_MR=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/div/div/onereg-radio-wrapper[2]/pos-input-radio/label/i')))
Gender_MS=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/div/div/onereg-radio-wrapper[1]/pos-input-radio/label/span')))
Gender_Other=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/div/div/onereg-radio-wrapper[3]/pos-input-radio/label/span')))
First_Name=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[1]/div/div[2]/pos-input/input')))
Last_Name=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[2]/div/div[2]/pos-input/input')))
Country=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/fieldset/onereg-form-row[1]/div/div/pos-input/select')))
try:
    State=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/fieldset/onereg-form-row[2]/div/div/pos-input/select')))
except:
    print("no state")
mail_type=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[1]/onereg-alias/fieldset/onereg-progress-meter/div[2]/div[2]/div/pos-input[2]/select')))
check_email_good=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[1]/onereg-alias/fieldset/onereg-progress-meter/div[2]/div[2]/div/button')))

#TODO state if statements
Date_Birth_Month=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[1]/input')))
Date_Birth_Day=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[2]/input')))
Date_Birth_Year=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[3]/input')))
Password=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
Reapeat_Password=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirm-password"]')))
SMS_Checkbox=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[5]/onereg-password-recovery/fieldset/onereg-progress-meter/div[3]/onereg-checkbox-wrapper/pos-input-checkbox/label/span')))
Email_Checkbox=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[5]/onereg-password-recovery/fieldset/onereg-progress-meter/div[4]/onereg-checkbox-wrapper/pos-input-checkbox/label/span')))
#Conditional field
Verification_Email=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contactEmail"]')))

#/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/div/div/onereg-radio-wrapper[1]/pos-input-radio/label/span
#'''
'''slow_type(email_field, test_person["name"]["first_name"]+test_person["name"]["last_name"]+"a505")
time.sleep(random.uniform(1.5,2.5))
ActionChains(driver)\
        .click(check_email_good)\
        .perform()
time.sleep(100)
if (test_person["gender"] == "Male"):
    Gender_MR.click()
if(test_person["gender"] == "Female"):
    Gender_MS.click()
if(test_person["gender"]=="Other"):
    Gender_Other.click()
time.sleep(1)
slow_type(First_Name,test_person["name"]["first_name"])
time.sleep(1)
slow_type(Last_Name,test_person["name"]["last_name"])
if(test_person["country"]=="United States"):
    Country.click()
    Country.send_keys("United States")
    Country.send_keys(Keys.RETURN)
    State.click()
    State.send_keys(test_person["state"])
    State.send_keys(Keys.RETURN)'''


#TODO if burned get new proxy

time.sleep(1000)
driver.quit()

#SAVEEMAIL
#pomodoro = Email({'Email': 'imed@mail.com', 'Password': "imed51512", "Gender":"Male", "Birthdate":"12/12/1990"})
#pomodoro.save()
#TODO fix runs only in debug mode