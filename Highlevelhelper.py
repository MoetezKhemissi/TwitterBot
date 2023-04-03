
from config import *
def email_to_account(email_list):
    accounts=[]
    for email in email_list:
        
        split_email=email['email'].split('@')
        for i in range(Number_of_accounts_per_email):
            account={}
            reconstructed=split_email[0]+'+189'+str(i)+'@'+split_email[1]
            account["email"]    = reconstructed
            account["password"] = email['password']
            account["originalmail"] = email['email']
            accounts.append(account)
    return accounts

