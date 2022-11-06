#!coding: utf-8
import smtplib
import imaplib
import yaml
import sys

from random import shuffle
from datetime import datetime

class Sender():

    def __init__(self, from_address, password, destination, subject):

        self.sent_from = from_address
        self.gmail_password = password

        self.to = [destination]
        self.subject = subject

    def send(self, body):

        email_text = """From: %s\nTo: %s\nSubject: %s\n\n%s\n""" % (self.sent_from, ", ".join(self.to), self.subject, body)
    

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.sent_from, self.gmail_password)
            server.sendmail(self.sent_from, self.to, email_text.encode('utf-8'))
            server.close()

            print('Email sent!')
        except:
            print('Something went wrong...')


def check(decision, members):

    for k in range(len(decision)):
        if members[k]["name"] == decision[k]:
            return False
    return True


def remove_sent_emails(address, password, folder):

    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(address, password)

    imap.select(folder)

    t = datetime.now()

    status, messages = imap.search(None, f'SINCE "{t.strftime("%d-%b-%Y").upper()}"')

    messages = messages[0].split(b" ")

    for mail in messages:

        imap.store(mail, "+FLAGS", "\\Deleted")


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage : python3 secret_santa.py <config.yaml>")
        sys.exit()

    with open(sys.argv[1], "r") as f:
        config = yaml.safe_load(f)

    decision = [m["name"] for m in config["members"]]

    
    while not check(decision, config["members"]):
        shuffle(decision)

    for k in range(len(decision)):

        email = config["members"][k]["address"]
    
        s = Sender(config["from"]["address"], config["from"]["password"], email, config["email"]["subject"])

        s.send(config["email"]["body"].format(EMAIL=decision[k], PRICE=config["email"]["price"]))

    remove_sent_emails(config["from"]["address"], config["from"]["password"], config["email"]["sent_items_folder"])
