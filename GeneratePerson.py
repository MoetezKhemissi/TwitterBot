from faker import Faker
import utils
from datetime import date
import time


fake = Faker(["en_US"])
def generate_female_us():
    names = [fake.unique.name_female() for i in range(50)]
    addresses = [fake.unique.address() for i in range(50)]
    birthdays = [fake.unique.date_of_birth(tzinfo=None, minimum_age=21, maximum_age=32) for i in range(50)]
    for birthday in birthdays:
        print("full",birthday,"split",split_birthday(birthday))
    
    assert len(set(names)) == len(names)
    '''for address in addresses:
        new_addr=split_address(address)
        if(new_addr["notallowed"]!=True):
            print(new_addr)'''
def split_address(address):
    full_address={"street":None,"city":None,"zip":None,"full_state":None,"short_state":None,"full_address":None,"notallowed":None}
    split_address=address.split("\n")
    try:
        state=split_address[1].split(",")[1].split(" ")[1]
    except:
        full_address["notallowed"]=True
        return full_address
    if(state not in utils.not_allowed):
        street = split_address[0]
        city = split_address[1].split(",")[0]
        zip = split_address[1].split(",")[1].split(" ")[2]
        full_address["street"]=street
        full_address["city"]=city
        full_address["zip"]=zip
        full_address["full_state"]=utils.us_abbrev_to_state[state]
        full_address["short_state"]=state
        full_address["full_address"]=address
        return full_address
    else:
        full_address["notallowed"]=True
        return full_address
def split_birthday(birthday):
    Birthday_Template={"year":None,"month":None,"day":None,"full_birthday":None}
    Birthday_Template["year"]=birthday.year
    Birthday_Template["month"]=birthday.month
    Birthday_Template["day"]=birthday.day
    Birthday_Template["full_birthday"]=birthday
    return Birthday_Template
def good_name(name):
    if(len(name.split(" "))==3):
        return False
    else:
        return True
def choose_address():
    addresses = [fake.unique.address() for i in range(50)]
    for address in addresses:
        new_addr=split_address(address)
        if(new_addr["notallowed"]!=True):
            return new_addr
def choose_name():
    names = [fake.unique.name_female() for i in range(50)]
    for name in names:
        if good_name(name):
            return split_name(name)

def split_name(name):
    final_name={"first_name":None,"last_name":None,"full_name":None}
    temporary_name=name.split(" ")
    final_name["first_name"]=temporary_name[0]
    final_name["last_name"]=temporary_name[1]
    final_name["full_name"]=name
    return final_name
    
def generate_person():
    person={"name":None,"address":None,"birthday":None,"Gender":None}
    person["name"]=choose_name()
    person["address"]=choose_address()
    #always same birth since it is a requirement
    person["birthday"]=split_birthday(fake.unique.date_of_birth(tzinfo=None, minimum_age=21, maximum_age=32))
    #Always female since it is a requirement
    person["gender"]="Female"
    person["country"]="US"
    return person


# GENERATE 1000 PEOPLE IN 14.5 Seconds
#generate_female_us()





