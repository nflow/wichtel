#!/usr/bin/python3

import sys
import json
import os.path
import getopt
from collections import deque
from random import shuffle
import smtplib
import getpass
from email.mime.text import MIMEText

SETTINGS_FILE = 'settings.json'

def send_mail(settings, partner_list):
    server = smtplib.SMTP(settings['mail']['smtp'])
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(settings['mail']['username'],settings['mail']['password'])

    partner_list = sorted(partner_list, key=lambda x: x[0]["name"])
    for mail in partner_list:
        print(mail[0])
    if input('Type YES to continue: ') == 'YES':
        print('Begin to send E-Mails.')
        for pair in  partner_list:
            name_0 = pair[0]["name"]
            email_0 = pair[0]["mail"]
            name_1 = pair[1]["name"]
            print(email_0)
            if not settings['ask_before_send'] or input('Send mail type Y: ') == 'Y':
                body = """{} dein Wichtelpartner lautet: {}.\n
                        Das Geschenk sollte einen Wert von min {} Euro haben.\n
                        Dies ist eine automatisch generierte E-Mail. Sollte ein 
                        Fehler auftreten, dann schreibt mir bitte.""".format(name_0, name_1.upper(),settings['budget'])

                msg = MIMEText(body.encode("latin-1"), _charset="latin-1")
                msg['Subject'] = "Wichtelpartner für: {}".format(name_0.upper())
                msg['From'] = username
                msg['To'] = email_0
                server.ehlo()
                try:
                    server.sendmail(username, email_0, msg.as_string())
                    print("Mail sent to {}".format(email_0))
                except:
                    print("An error occoured while sending the mail. Contact {} ({}) and send him the partner manually.".format(name_0, email_0))
    server.quit()

if __name__ == "__main__":
    if os.path.isfile(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as file:
            settings = json.load(file)
            if os.path.isfile(settings["output"]):
                    send_mail(settings, partner_list)
    else:
        print("Settings file not found.")
