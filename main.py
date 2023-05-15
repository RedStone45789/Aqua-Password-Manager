import os, sys, string

import random, secrets

import redis

import requests, urllib.request, urllib.parse, urllib.error

import hashlib, base64, Cryptodome, cipher, crypto
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad


import time, datetime

import json

import tempfile

from dotenv import load_dotenv

load_dotenv()
#Import done

usrData = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    username=os.getenv("REDIS_USER"),
    password=os.getenv("REDIS_PASSWORD")
)

def check_net():
    try:
        urllib.request.urlopen("http://www.google.com")
        return True
    except:
        return False

with open('config.json') as f:
    config = json.load(f)

print(config["offline_mode"])

if config["offline_mode"] == True:
    print("Offline mode enabled! Some features may not work.")
else:
    if check_net() == False:
        offline_mode = True
        print("No internet connection! Offline mode enabled! Some features may not work.")
    else:
        pass

#Network check done

#Tempfile:

tmp = tempfile.TemporaryFile()


def start(cmd):
    if cmd == 'ntc':
        if input('Login or create account? (reg/log): ') == 'reg':
            register()
        elif input('Login or create account? (reg/log): ') == 'log':
            login()
        else:
            raise Exception('Invalid input')
    else:
        try:
            tmptoken = tmp.readline(1)
            tmptoken_parts = tmptoken.split(b".")
            tmpusername = base64.b64decode(tmptoken_parts[0])
            redis_token = usrData.get(f'{tmpusername}_token')
            if redis_token == None:
                raise ValueError("Token not found!")
                print("Skipping token check!")
                start('ntc')
            else:
                if redis_token == tmptoken:
                    pass

        except:
             
            raise ValueError("Token not found!")
            print("Skipping token check!")
            start('ntc')
        finally:
            main(tmptoken)

    
def main(token):
    if token == None:
        raise ValueError('Token not found! Is this corrupted?')
        main()
    else:
        
        token_parts = token.split(b".")
        redis_token = usrData.get(f'{base64.b64decode(token_parts[0])}_token')
        if redis_token == None:
            raise ValueError('Token not found! Is this corrupted?')
            main()
        else:
            if redis_token == token:
                pass
            else: raise ValueError('Token not found! Is this corrupted?')
    



    print(f'Aqua Password Manager v{config["version"]}\n')
    print(f'Made by RedStone\n')
    cmd = input('Command (Enter help for help): ')
    if cmd == 'help':
        print('Commands:\n')
        print('addpassw - Add a password to the database\n')
        print('delpassw - Delete a password from the database\n')
        print('listpassw - List all passwords in the database\n')
        print('exit - Exit the program\n')
        time.sleep(2.1)
    elif cmd == 'addpassw':
        addpassw(input('Password: '), input('Website or App name: '))
    elif cmd == 'delpassw':
        delpassw(input('Password: '), input('Enter confirm to confirm deletion: '))
    elif cmd == 'listpassw':
        listpassw()
    elif cmd == 'exit':
        exit()
    
def register():
    username = input('Username: ')
    try:
        if usrData.get(f'{username}_name') == None:
            pass
        else:
            raise ValueError('Username already exists!')
    except:
        raise ValueError('Username already exists!')
    finally:
        pass
    password = input('Password: ')
    if input('Confirm password: ') == password:
        pass
    else:
        raise ValueError('Passwords do not match!')
        register()
    
    email = input('Email: ')
    sex = input('Sex (M/F)(Optional): ')
    age = input('Age(Optional): ')
    
    key = get_random_bytes(32)
    print(f'This is your private key: {key}  Write it somewhere safe then press enter!')
    if input('') == '':
        pass
    else:
        pass
    cipher = AES.new(key, AES.MODE_CBC)

    token = f'{base64.b64encode(username.encode("utf-8")).decode()}.{int(time.time())}.{secrets.token_urlsafe(24)}.{base64.b64encode(password.encode("utf-8")).decode()}'
    token = pad(token, 16)
    token = cipher.encrypt(token)
    
    
    password = pad(password.encode('utf-8'), 16)
    password = cipher.encrypt(password)
    password = base64.b64encode(password)
    usrData.set(f'{username}_name', username)
    usrData.set(f'{username}_email', email)
    usrData.set(f'{username}_password', password)
    usrData.set(f'{username}_sex', sex)
    usrData.set(f'{username}_age', age)
    usrData.set(f'{username}_token', token)
    print(f'{username} has been registered!')
    tmp.writelines(token)
    time.sleep(2.1)
    
























if __name__ == "__main__":
    start('ntc')
