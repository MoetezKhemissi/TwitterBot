import os
from twocaptcha import TwoCaptcha
from config import Two_Captcha_api_key


def solvehCaptcha(url):
    api_key = os.getenv('APIKEY_2CAPTCHA', Two_Captcha_api_key)

    solver = TwoCaptcha(api_key)

    try:
        result = solver.normal(url)

    except Exception as e:
        print(e)
        return False

    else:
        return result

def solve_normal_captcha(url):
    print("Solving normal captcha with url ...",url)
    result = solvehCaptcha(url)
    print("Solved normal captcha!!!!")
    return result['code']


