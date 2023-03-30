import time
import random
import string
from selenium.webdriver.common.keys import Keys
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
    "American Samoa":"AS",
    "District of Columbia":"DC",
    "Federated States of Micronesia":"FM",
    "Guam":"GU",
    "Marshall Islands":"MH",
    "Palau":"PW",

    

}
not_allowed = ["AS","DC","FM","GU","MH","PW","PR","VI","MP","UM"]
us_abbrev_to_state = inv_map = {v: k for k, v in us_state_to_abbrev.items()}

def wait_click(element):
     time.sleep(0.5)
     element.click()
def action_click(element):
     time.sleep(0.5)
     element.click()
def slow_type(element, text):
    """Send a text to an element one character at a time with a delay."""
    i = 0
    
    for character in text:
        i= i+1
        if i % 3 == 0:
            delay=random.uniform(0.25, 0.35)
        if i % 3 == 1:
            delay=random.uniform(0.05, 0.15)
        if i % 3 == 2:
                delay=random.uniform(0.15, 0.25)
        if i % 9 ==7:
            delay=random.uniform(0.1, 0.2)
            element.send_keys(random.choice(string.ascii_letters))
            delay=random.uniform(0.1, 0.2)
            element.send_keys(Keys.BACK_SPACE)
        
        element.send_keys(character)
        time.sleep(delay)

def slow_type_action(actions, tweet_message):
    
    """Send a text to an element one character at a time with a delay."""
    i = 0

    for character in tweet_message:
        i= i+1
        if i % 3 == 0:
            delay=random.uniform(0.25, 0.35)
        if i % 3 == 1:
            delay=random.uniform(0.05, 0.15)
        if i % 3 == 2:
                delay=random.uniform(0.15, 0.25)
        if i % 9 ==7:
            delay=random.uniform(0.1, 0.2)
            actions.send_keys(random.choice(string.ascii_letters)).perform()
            delay=random.uniform(0.1, 0.2)
            actions.send_keys(Keys.BACK_SPACE).perform()
        
        actions.send_keys(character).perform()
        time.sleep(delay)