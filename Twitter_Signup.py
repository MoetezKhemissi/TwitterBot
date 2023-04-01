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
from databseoperations import *

def signup(user,mp,user_testing_mail):
    print("user :",user)
    print("mp :",mp)
    print("user_testing_mail :",user_testing_mail)
    '''user ="twittertesting165@gmail.com"
    mp ="twitQKrSAtidsqnssg494"
    user_testing_mail="twittertesting165+Upwork111@gmail.com"'''
    twitter_password=mp
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
    time.sleep(0.5)
    upload = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div'))).click()
    time.sleep(2)
    path=os.getcwd()+"\Image_wierd.jpg"
    print(path)
    time.sleep(0.5)
    pyperclip.copy(path)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2)
    validate_image= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div'))).click()
    time.sleep(2)
    image_validator= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')))
    wait_click(image_validator)
    time.sleep(5)
    '''
    time.sleep(5)
    driver.get("https://twitter.com/")
    time.sleep(5)
    input_tweet= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
    print("selected input tweet")
    actions = ActionChains(driver)
    actions.move_to_element(input_tweet)
    actions.click()
    slow_type_action(actions,tweet_message)

    tweet_button= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')))
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
    time.sleep(2)
    '''
    url = "https://twitter.com/"
    driver.get(url)
    username=""
    Account_container = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@data-testid = 'SideNav_AccountSwitcher_Button']")))
    time.sleep(2)
    Div_1 = Account_container.find_elements(By.TAG_NAME, 'span')
    for element in Div_1:
        Full_Text=element.text
        if Full_Text.startswith('@'):
            username=Full_Text[1:]
    print("Username is :",username)
    account_final={'Email': '', 'Password': '','username':'','OriginalMail':''}
    account_final["Email"]=user_testing_mail
    account_final["Password"]=mp
    account_final["username"]=username
    account_final["OriginalMail"]=user
    print("Account created: ",account_final)
    database_write_account(account_final)
    driver.quit()
