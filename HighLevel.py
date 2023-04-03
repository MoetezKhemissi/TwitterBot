#Backend 
from nordvpn_switcher import initialize_VPN,rotate_VPN
import time
import time
from Twitter_Signup import signup
from Highlevelhelper import *
from Twitterlogin import *
from databseoperations import *
from config import *


instructions = initialize_VPN(area_input=countries_for_nord) # <-- Be aware: the area_input parameter expects a list, not a string
rotate_VPN(instructions)

def Create_n_account(emails):
    accounts_to_create = email_to_account(emails)
    rotate_VPN(instructions)

    i=0
    for account in accounts_to_create:
        
            if i%Number_of_accounts_before_rotation==0:
                rotate_VPN(instructions)
                time.sleep(3)
            try:
                signup(account["originalmail"],account["password"],account["email"])
            except:
                print("Could not create account")
            i=i+1

    # for i in 1->5 signup + create into database
    return 0
    
def like_high_level(link):
    all_accounts=database_read_accounts()
    for account in all_accounts:
        #add nord
        driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])
        post_like(driver,link)
        time.sleep(2)
        driver.quit()

def Comment_high_level(link,Comment_value):
    all_accounts=database_read_accounts()
    for account in all_accounts:
        #add nord
        driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])
        print("Done Connecting ..")
        comment_post(driver,link,Comment_value)
        time.sleep(3)
        driver.quit()


def get_followers_high_level(max,user_id):
    all_accounts=database_read_accounts()
  
    account = random.choice(all_accounts)

    driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])
    print("Done Connecting ..")
    get_followers(driver,user_id)
    follower_links = find_n_followers(driver,max).keys()
    i=0
    for linked in follower_links:
        if i<max:

            follower_template = {"link": linked}
            database_write_follower(follower_template)
            i=i+1
    print("Read followers from databse :")
    print(database_read_followers())
    print("New Length :",len(database_read_followers()))
    driver.quit()
def follow_high_level(user_id):
    all_accounts=database_read_accounts()
    for account in all_accounts:

        driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])
        print("Done Connecting ..")
        follow(driver,user_id)
        driver.quit()

def change_bio_high_level(bio_message):
    all_accounts=database_read_accounts()
    for account in all_accounts:
        driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])
        print("Done Connecting ..")
        change_bio(driver,bio_message)
        driver.quit()
def check_dmable_high_level(max):
    i=0
    list_url=[]
    all_accounts=database_read_accounts()
    all_followers=database_read_followers()
    for follower in all_followers:
        if follower["checked_dmable"] ==1:
            print("Already checked")
        elif i<max:
            list_url.append(follower["link"])
            i=i+1

    chunks = [list_url[x:x+Batch_size_check_dmable] for x in range(0, len(list_url), Batch_size_check_dmable)]
    for chunk in chunks:
        account=random.choice(all_accounts)
        driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])
        check_if_can_dm(driver,chunk)
        driver.quit()

    return 0
def dm_high_level(message):
    
    available_to_dm = get_all_dmable_and_not_dmed()
    all_accounts=database_read_accounts()
    chosen_account={}
    for account in all_accounts:
        if account["VerifiPhone"] == 1:
            chosen_account=account
            break


    driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])

    i=0
    for follower in available_to_dm:
        if i<2:
            dm(driver,follower["link"],message)
            Followed_Status_update(follower["id"])
            i=i+1
    driver.quit()

def is_already_followed(account,user_id):
    the_followers = account["Followed"]

    if len(the_followers.split(","))==0:
        split=the_followers.split(",")
    else:
        split=the_followers.split(",")[:len(the_followers.split(","))-1]
    for follower in split:
        if follower == user_id:
            return True
    return False
def follow_high_level(maxu):
    all_accounts=database_read_accounts()
    all_followers=database_read_followers()
    for account in all_accounts:
        i=0
        list_followers=[]
        # TODO generate list of followers with no followed
        for foll in all_followers:
            extracted_username=extract_user_from_url(foll["link"])
            checker= is_already_followed(account,extracted_username)

            if not(checker) and i<maxu:
                list_followers.append(foll)
                i=i+1

        print("List of followers to follow :")
        print(list_followers)
        driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])
        for follower in list_followers:
            extract_user=extract_user_from_url(follower["link"])
            account["Followed"]= account["Followed"]+ extract_user +","
            account.update()
            try:
                
                follow(driver,extract_user)
                
                
            except:
                print("Could not follow")

        print(account)
        driver.quit()

#rotate_VPN(instructions)



#check_dmable_high_level(15)
#get_followers_high_level(100,Profile_id)
#Comment(post_link,message) 
#like(link)
#follow_high_level(10)
#change_bio_high_level(Message_bio)


#dm_high_level("hi")

#Create_n_account(email_listed)

