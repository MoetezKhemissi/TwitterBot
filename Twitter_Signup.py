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
from VerifyMail import go_to_google_and_extract_code
from selenium.webdriver.common.action_chains import ActionChains
from utils import *

def slow_type_action(actions, tweet_message):
    """Send a text to an element one character at a time with a delay."""
    i = 0

    for character in tweet_message:
        i= i+1
        if i % 3 == 0:
            delay=random.uniform(0.25, 0.35)
        if i % 3 == 1:
            delay=random.uniform(0.05, 0.15)
        if i % 3 == 2:
                delay=random.uniform(0.15, 0.25)
        if i % 9 ==7:
            delay=random.uniform(0.1, 0.2)
            actions.send_keys(random.choice(string.ascii_letters)).perform()
            delay=random.uniform(0.1, 0.2)
            actions.send_keys(Keys.BACK_SPACE).perform()
        
        actions.send_keys(character).perform()
        time.sleep(delay)
user ="twittertesting165@gmail.com"
mp ="twitQKrSAtidsqnssg494"
user_testing_mail="twittertesting165+Upwork@gmail.com"
twitter_password="twitQKrSAting494sssdds"
tweet_message="Hello , i am really new to twitter can anyone help me out ?"
person1 = GeneratePerson.generate_person()
options = webdriver.EdgeOptions() 
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--start-maximized")
options.add_argument("inprivate")
#os.startfile(r"C:\Users\Moetez\Desktop\SeleniumProxy\10minParis.exe")
#options.add_argument('--proxy-server=pr.oxylabs.io:7777')
driver = webdriver.Edge(options=options,executable_path="C:\\Users\\Moetez\\Desktop\\UpworkClient\\TwoDriver\\TwitterDriver\\msedgedriver.exe")

url = "https://twitter.com/"
driver.get(url)
time.sleep(0.5)
try:
    non_essential = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/span/span'))).click()
    time.sleep(0.5)
except :
    print("no cookie needed")
create_account = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/div[3]/a/div'))).click()
time.sleep(0.5)
full_name= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/label/div/div[2]/div/input')))
#use_mail=WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/span')))
#use_mail.click()
slow_type(full_name,person1["name"]["first_name"]+" "+person1["name"]["last_name"])
email= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/label/div/div[2]/div/input')))
slow_type(email,user_testing_mail)
time.sleep(0.5)

month= Select(WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[1]/select')))).select_by_value(str(person1["birthday"]["month"]))
try:
    print("unavailable_mail")
    unavailable_mail= WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/span')))
except:
    print("available mail")
#/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/span
time.sleep(0.5)
day= Select(WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[2]/select')))).select_by_value(str(person1["birthday"]["day"]))
time.sleep(0.5)
year= Select(WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[3]/select')))).select_by_value(str(person1["birthday"]["year"]))
time.sleep(2)
next_button= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')))
wait_click(next_button)
second_next= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')))
wait_click(second_next)
time.sleep(1)
signup_button= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')))
wait_click(signup_button)
verification_code =go_to_google_and_extract_code(user,mp)
try:
    input_verification_code = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
except:
    print("error")
    time.sleep(50)
time.sleep(0.5)
try:
    slow_type(input_verification_code,verification_code)
except:
    print("error unwritable")
next_button= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')))
wait_click(next_button)
password_field= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')))
slow_type(password_field,twitter_password)
time.sleep(1)
confirm_paswwd= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div')))
wait_click(confirm_paswwd)
upload = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div'))).click()
time.sleep(2)
path=os.getcwd()+"\Image_wierd.jpg"
print(path)
pyperclip.copy(path)
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')
time.sleep(2)
validate_image= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div'))).click()
time.sleep(2)
image_validator= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')))
wait_click(image_validator)
time.sleep(5)
driver.get("https://twitter.com/")
time.sleep(5)
input_tweet= WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
print("selected input tweet")
actions = ActionChains(driver)
actions.move_to_element(input_tweet)
actions.click()
slow_type_action(actions,tweet_message)

tweet_button= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')))
wait_click(tweet_button)
try:
    confirm= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span')))
    wait_click(confirm)
except:
    print("no confirm required")
try:
    defintely_not_a_bot= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div')))
    wait_click(defintely_not_a_bot)
except:
    print("no bot notif")
'''try:
    accept_notif= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/span/span'))).click()
except:
     print("no notif")
try:
    accept_notif_without_no = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div')))
    wait_click(accept_notif_without_no)
     #/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div
     #/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div
except :
     print("no wierd notif either")
try :
     another_next= WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'))).click()
except :
     print("no another next")
try:
     ignore_username=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'))).click()
except:
     print("no ignore username")
try:
     pass_thourgh= WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div'))).click()
except:
     print("no pass trhough")
try:
     next = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'))).click()
except:
        print("no next")
choice_1= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div[3]/div/div/div/li[1]/div/div/div/div/div/div/div')))
wait_click(choice_1)
choice_2 = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div[3]/div/div/div/li[2]/div/div/div/div/div/div/div')))
wait_click(choice_2)
choice_3 = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div[3]/div/div/div/li[3]/div/div/div/div/div/div/div/div/span')))
wait_click(choice_3)
time.sleep(0.5)
next = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/span/span'))).click()
another_one = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'))).click()
follow_first= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div/div/span/span'))).click()
final_next = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'))).click()
final_final_next = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'))).click()
print("Done")'''
#
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