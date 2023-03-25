from selenium import webdriver
from selenium_stealth import stealth
import time
import os
def start_driver_stealth():

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    #os.startfile(r"C:\Users\Moetez\Desktop\SeleniumProxy\10minParis.exe")
    #options.add_argument('--proxy-server=pr.oxylabs.io:7777')
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

driver = start_driver_stealth()
driver.get("http://www.whatismyproxy.com/")
time.sleep(1000)