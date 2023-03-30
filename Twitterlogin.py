

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from utils import *
from Regen import *
import validators
from VerifySusMail import go_to_google_and_extract_code_2
from selenium.webdriver.common.action_chains import ActionChains
def start_driver_and_login():
    return 0

def start_driver():
    options = webdriver.EdgeOptions() 
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--start-maximized")
    options.add_argument("inprivate")
    #os.startfile(r"C:\Users\Moetez\Desktop\SeleniumProxy\10minParis.exe")
    #options.add_argument('--proxy-server=pr.oxylabs.io:7777')
    driver = webdriver.Edge(options=options,executable_path="C:\\Users\\Moetez\\Desktop\\UpworkClient\\TwoDriver\\TwitterDriver\\msedgedriver.exe")
    return driver

def go_to_twitter(driver):
    url = "https://twitter.com/"
    driver.get(url)
def non_essential_cookie(driver):
    try:
        non_essential = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/span/span'))).click()
        time.sleep(0.5)
    except :
        print("no cookie needed")
def login(driver,email_value,mdp_value,username_value,email_actual_value,email_actual_pass):
    login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')))
    wait_click(login_button)
    time.sleep(0.5)
    email = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
    slow_type(email, email_value)
    next = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')))
    wait_click(next)
    try:
        username_field  = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
        slow_type(username_field, username_value)
        next = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')))
        wait_click(next)
    except:
        print("no addditional name required")
    Password= WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
    slow_type(Password, mdp_value)
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')))
    wait_click(login_button)
    try:
        confimation_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
        code_final = go_to_google_and_extract_code_2(email_actual_value,email_actual_pass)
        slow_type(confimation_field, code_final)
        confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')))
        wait_click(confirm_button)
    except:
        print("no extra code 2fa")

def scrape_followers(driver,url):
    # Twitter api
    # goto https://twitter.com/elonmusk
    # goto https://twitter.com/elonmusk/followers
    # https://twitter.com/Amina5074349181
    # TODO scraper dynamic
    return 0

def find_n_followers(driver,max):
    print("Finding followers")
    map = {"-1":"test"}
    previous_height = driver.execute_script('return document.body.scrollHeight')
    i=0
    while i<max:
        #implement max number of elements
        i=i+1
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(3)
        new_height = driver.execute_script('return document.body.scrollHeight')
        new_list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div')))
        list = new_list.find_elements(By.XPATH,"//*[@data-testid = 'cellInnerDiv']")
        for element in list:
            try:
                link = element.find_element(By.TAG_NAME,'a').get_attribute('href')
                map[link]= "test"
            except:
                print("no a")
           
            #print(element.find_element(By.TAG_NAME,'a').get_attribute('href'))
        i=len(map)
        if new_height == previous_height:
            print("Done working")
            return map
    return map
            
def go_to_profile(driver,user_id):
    time.sleep(5)
    print("Going To profile ",user_id,"..")
    driver.get( "https://twitter.com/"+user_id)
def get_followers(driver,user_id):
    time.sleep(10)
    driver.get( "https://twitter.com/"+user_id+"/followers")
def get_following(driver,user_id):
    driver.get( "https://twitter.com/"+user_id+"/following")
def get_likes(driver,user_id):
    driver.get( "https://twitter.com/"+user_id+"/likes")
def get_follower_list():
    get_followers(driver,"elonmusk")
def check_if_can_dm(driver,list_url):
    print("Checkingg Dmable followers ..")
    dm_list = []
    for key in list_url.keys():
        print(key)
        if validators.url(key):
            time.sleep(7)
            driver.get(key)
            try:
                make_sure_load = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span/span[1]')))
                try:
                    dm_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label = 'Message']")))
                    dm_list.append(key)
                    print(key)
                except:
                    print("no dm button")
            except:
                print("couldn't load user")
        else:
            print("not a url")
    return dm_list
def dm(driver,username,message):
    go_to_profile(driver,username)
    try:
            make_sure_load = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span/span[1]')))
            print("Sucessfully loaded user")
            try:
                    time.sleep(3)
                    dm_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label = 'Message']")))
                    dm_button.click()
                    try:
                        time.sleep(2)
                        print("started messaging...")
                        write_message_field = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div/div/div[2]/div/div/aside/div[2]/div[2]/div/div/div/div/div/label/div[1]/div/div/div/div/div/div")))
                        print("Still messaging")
                        time.sleep(1)
                        actions = ActionChains(driver)
                        actions.move_to_element(write_message_field).click().perform()
                      
                        print("Sucessfully clicked on button")
                        time.sleep(2)
                        slow_type_action(actions,message)
                        send_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div/div/div[2]/div/div/aside/div[2]/div[3]/div/svg")))
                        actions.move_to_element(send_button).click().perform()
                    except Exception as e:
                        print("Error writing the message")
                        print("Error: ",e)
            except Exception as e:
                    print("no dm button")
                    print("Error: ",e)
    except Exception as e:
        print("couldn't load user")
        print("Error: ",e)
    return 0
heart_code = ':emoji' u'\ue007'
def message_generator(user):
    print("Generating message ..")
    message = "@"+user+" sends free pics to everyone who follows her " + heart_code
    return message
username ="KimberlyWa56645"
email_address_value="twittertesting165+Upwork@gmail.com"
email_actual_value="twittertesting165@gmail.com"
email_actual_pass="twitQKrSAtidsqnssg494"
pass_value="twitQKrSAting494sssdds"
User_to_go_to = "OumarKBa"
regen_driver()
driver=start_driver()
go_to_twitter(driver)
non_essential_cookie(driver)
login(driver,email_address_value,pass_value,username,email_actual_value,email_actual_pass)

#dm(driver,User_to_go_to,message_generator(username))
'''get_followers(driver,"elonmusk")
followers = find_n_followers(driver,100)
print(followers)
print(check_if_can_dm(driver,followers))'''

def follow(driver,user_id):
    go_to_profile(driver,user_id)
    
def tweet(driver,tweet_message):
    return 0
def dm(driver,username,message):
    return 0

def logout(driver):
    return 0
def change_bio():
    return 0
time.sleep(1000)

