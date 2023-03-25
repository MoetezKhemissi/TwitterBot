from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import GeneratePerson
import random
import string
import os
import pyautogui
import pyperclip


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
            element.send_keys(Keys.BACK_SPACE)
        
        element.send_keys(character)
        time.sleep(delay)
person1 = GeneratePerson.generate_person()
options = webdriver.EdgeOptions() 
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--start-maximized")
options.add_argument("--incognito")
#os.startfile(r"C:\Users\Moetez\Desktop\SeleniumProxy\10minParis.exe")
#options.add_argument('--proxy-server=pr.oxylabs.io:7777')
driver = webdriver.Edge(options=options,executable_path="C:\\Users\\Moetez\\Desktop\\UpworkClient\\TwoDriver\\msedgedriver.exe")

url = "https://twitter.com/"
driver.get(url)
time.sleep(0.5)
non_essential = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/span/span'))).click()
time.sleep(0.5)
create_account = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/div[3]/a/div'))).click()
time.sleep(0.5)
full_name= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/label/div/div[2]/div/input')))
#use_mail=WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/span')))
#use_mail.click()
slow_type(full_name,person1["name"]["first_name"]+" "+person1["name"]["last_name"])
email= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/label/div/div[2]/div/input')))
slow_type(email,"khemissimoetez+awuawy@gmail.com")
time.sleep(0.5)

month= Select(WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[1]/select')))).select_by_value(str(person1["birthday"]["month"]))

#/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div[3]/div/div[1]/select
time.sleep(0.5)
day= Select(WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[2]/select')))).select_by_value(str(person1["birthday"]["day"]))
time.sleep(0.5)
year= Select(WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[3]/select')))).select_by_value(str(person1["birthday"]["year"]))
time.sleep(2)
next_button= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'))).click()
time.sleep(4)
second_next= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'))).click()
time.sleep(1)
signup_button= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'))).click()
print("started sleeping")
time.sleep(20)
print("fininshed sleeping")
password_field= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')))
slow_type(password_field,"123456789dd")
Next_pass= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div'))).click()
upload = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div'))).click()
time.sleep(2)
path=os.getcwd()+"\Image_wierd.jpg"
print(path)
pyperclip.copy(path)
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')

validate_image= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div'))).click()
another_next= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'))).click()
ignore_username=WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'))).click()
pass_thourgh= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div'))).click()
next = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'))).click()
choice_1= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div[3]/div/div/div/li[1]/div/div/div/div/div/div/div'))).click()
choice_2 = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div[3]/div/div/div/li[2]/div/div/div/div/div/div/div'))).click()
choice_3 = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div[3]/div/div/div/li[3]/div/div/div/div/div/div/div/div/span'))).click()
next = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/span/span'))).click()
another_one = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'))).click()
follow_first= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div/div/span/span'))).click()
#profile_picture=""
#drv.find_element_by_id("IdOfInputTypeFile").send_keys(os.getcwd()+"/image.png")
#/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/label/div/div[2]/div/input full name
#/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/label/div/div[2]/div/input email
#/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[1]/select month
#/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[3]/div/div[2]/select day
#/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[3]/div/div[3]/select year

#/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div
#html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div

#
time.sleep(1000)
driver.quit()

#TODO regenerate driver
#TODO email verification