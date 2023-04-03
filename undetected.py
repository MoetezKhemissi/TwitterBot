import undetected_chromedriver as uc
from selenium import webdriver
import time
import os
def start_undetected():
    #os.startfile(r"C:\Users\Moetez\Desktop\SeleniumProxy\10minParis.exe")
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--proxy-server=pr.oxylabs.io:7777')
    uc.TARGET_VERSION = 78    
    driver = uc.Chrome()
    driver.get("https://www.google.com")
    
    
    return driver
#customer-Moekhe-cc-fr-city-paris-sessid-02699customer-Moekhe-cc-fr-city-paris-sessid-02699  kQ7LInq8^z73    

driver = start_undetected()
time.sleep(100)
