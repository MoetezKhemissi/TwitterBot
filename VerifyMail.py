from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random
import string
from SolveNormalCaptcha import solve_normal_captcha
from utils import *

def split_email(email):
    Split_email=email.text.split("\n")
    email_template ={"sender":"","first_part":""}
    email_template["sender"]=Split_email[0]
    email_template["first_part"]=Split_email[1]
    return email_template
def login_gmail_retrieve_mails(username,mdp):
    beautiful_emails=[]
    options = webdriver.EdgeOptions() 
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--start-maximized")
    options.add_argument("inprivate")
    #os.startfile(r"C:\Users\Moetez\Desktop\SeleniumProxy\10minParis.exe")
    #options.add_argument('--proxy-server=pr.oxylabs.io:7777')
    driver = webdriver.Edge(options=options,executable_path="C:\\Users\\Moetez\\Desktop\\UpworkClient\\TwoDriver\\VerifDriver\\msedgedriver.exe")

    url = "https://gmail.com/"
    driver.get(url)
    email_input = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')))
    slow_type(email_input, username)
    next = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')))
    wait_click(next)
    try:
        captcha_image=WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[4]/div[1]/img')))
        print("Captcha found")
        image_path=captcha_image.get_attribute("src")
        solved =solve_normal_captcha(image_path)
        print("Cracking captcha in progress...")
        print(solved)
        #/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[4]/div[1]/img
        captcha_field=WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[4]/div[2]/div/div[1]/div/div[1]/input')))
        
        slow_type(captcha_field,solved)
        next = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')))
        wait_click(next)
    except:
        print("no captcha")
    password_input = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')))
    slow_type(password_input, mdp)
    nex_password = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')))
    wait_click(nex_password)
    print("detecting twitter verification code ..")
    Emails = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[6]/div[1]/div/table/tbody')))
    for email in Emails.find_elements(By.TAG_NAME, 'tr'):
        transformed_email=split_email(email)
        beautiful_emails.append(transformed_email)
    return beautiful_emails


def extract_mail(mails):
    for email in mails:
        if (email["sender"]=="Twitter" ):
            return email["first_part"].split(" ")[0]
        
def go_to_google_and_extract_code(user,mp):
    Emails=login_gmail_retrieve_mails(user,mp)
    print("Verif code is :",extract_mail(Emails))
    return extract_mail(Emails)



#support for captcha google

