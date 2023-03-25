from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import string
import os
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
options = webdriver.EdgeOptions() 
options.add_argument('--disable-blink-features=AutomationControlled')
#os.startfile(r"C:\Users\Moetez\Desktop\SeleniumProxy\10minParis.exe")
#options.add_argument('--proxy-server=pr.oxylabs.io:7777')
driver = webdriver.Edge(options=options,executable_path="C:\\Users\\Moetez\\Desktop\\UpworkClient\\TwoDriver\\msedgedriver.exe")
driver.get("https://www.bing.com/")
'''try:
     cookies_accept= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[2]/button[1]'))).click()
except:
     print("no cookie")
search_bing = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/form/div[1]/div/textarea')))
search_bing.click()
slow_type(search_bing,"mail.com")
search_bing.send_keys(Keys.ENTER)

go_to_mail= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/ol/li[1]/h2')))

go_to_mail.click()
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
SignupButton= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signup-button"]'))).click()
email_field=WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[1]/onereg-alias/fieldset/onereg-progress-meter/div[2]/div[2]/div/pos-input[1]/input')))
email_field.click()
slow_type(email_field,"Bestclickworker125")
#Gender_MR=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/div/div/onereg-radio-wrapper[2]/pos-input-radio/label/i')))
#Gender_MR.click()
#email_field.send_keys(Keys.TAB)
#/html/body/div[2]/main/ol/li[2]/div[1]/h2/a'''

print("test")
time.sleep(10000)