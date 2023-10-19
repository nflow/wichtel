#!/usr/bin/python3

import sys
import json
import os.path
import getopt
from collections import deque
from random import shuffle
import smtplib
import getpass

SETTINGS_FILE = 'settings.json'

def get(member, partner_list):
    if not member == '':
        for pair in partner_list:
            if member in pair[0]["name"] or member in pair[0]["mail"]:
                return pair[0]["name"] + ' -> ' + pair[1]["name"]
            else:
                return "Not found!"

if __name__ == "__main__":
    if os.path.isfile(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as file:
            settings = json.load(file)
        if settings["output"] != None and os.path.isfile(settings["output"]):
            with open(settings["output"], 'r') as file:
                partner_list = json.load(file)
                while True:
                    user_input = input('Enter name or mail: ')
                    if user_input.strip() == '':
                        break
                    print(get(user_input, partner_list))
                    input('Press any key to clear screen!')
                    if sys.platform == "win32":
                        os.system('cls')
                    else:
                        os.system('clear')
        else:
            print("Generate pairs file first.")
    else:
        print("Settings file not found.")
