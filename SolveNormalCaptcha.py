import os
from twocaptcha import TwoCaptcha



def solvehCaptcha(url):
    api_key = os.getenv('APIKEY_2CAPTCHA', '555ebaeb969ab933edb4717e2f3a0a0e')

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


