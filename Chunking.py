# how to update to dmable
from databseoperations import *
#print(database_read_all_accounts())
url_sample="https://twitter.com/DMaadany"
#print(database_read_followers())
def extract_user_from_url(url):
    return url.split("https://twitter.com/")[1]

i=0
stringw="" # initiate with state of variable
for follower in database_read_followers():

    if i<10:
        extract_user=extract_user_from_url(follower["link"])
        stringw= stringw+ extract_user +","

        i=i+1


if len(stringw.split(","))==0:
    split=stringw.split(",")
else:
    split=stringw.split(",")[:len(stringw.split(","))-1]

print(split)



