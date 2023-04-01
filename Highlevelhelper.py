

def email_to_account(email_list):
    accounts=[]
    for email in email_list:
        
        split_email=email['email'].split('@')
        for i in range(5):
            account={}
            reconstructed=split_email[0]+'+566'+str(i)+'@'+split_email[1]
            account["email"]    = reconstructed
            account["password"] = email['password']
            account["originalmail"] = email['email']
            accounts.append(account)
    return accounts

