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

def pair_partner(member):
    member = deque(member)
    shuffle(member)
    r_member = deque(member)
    r_member.rotate(-1)
    return zip(member, r_member)

if __name__ == "__main__":
    if os.path.isfile(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as file:
            settings = json.load(file)
            
            member_list = settings["member"]
            partner_list = list(pair_partner(member_list))
            
            if settings["output"] == None:
                print(json.dumps(partner_list, indent=4))
            else:
                with open(settings["output"], 'w+') as out:
                    json.dump(partner_list, out, indent=4)
    else:
        print("Settings file not found.")