# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import time, random
from flask import Flask, request, redirect
from O365 import Message

# Find these values at https://twilio.com/user/account


def send_msg(message):
    account_sid = "ACedcd0145b4845089c372f214c82a8668"
    auth_token = "535973c6aee932e5fea22d173dd655b6"
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
            to="+12059151043",
            from_="+12059003070",
            body=message + "  -Ava")
def date():
    return time.ctime()[4:10]

def day():
    return time.ctime()[0:3]

def hour():
    return int(time.ctime()[11:13])

def minute():
    return int(time.ctime()[14:16])

def morning():
    Day = day()
    if Day == "Mon" or Day == "Tue" or Day == "Wed" or Day == "Thu" or Day == "Fri":
        if hour() == 5 and minute() == 45:
            send_msg("Good morning sunshine.")
def week():
    today = date()
    Day = day()
    gold = ["Aug 21", "Sep 4", "Sep 18", "Oct 9", "Oct 23", "Oct 6", "Oct 20", "Oct 6", "Oct 20", "Dec 4", "Jan 1", "Jan 15", "Jan 29", "Feb 12", "Feb 26", "Mar 12", "Apr 2", "Apr 16", "Apr 30", "May 14"]
    white = ["Aug 28", "Sep 11", "Sep 25", "Oct 2", "Oct 16", "Oct 30", "Nov 13", "Nov 27", "Dec 11", "Jan 8", "Jan 22", "Feb 5", "Feb 19", "Mar 5", "Mar 19", "Mar 26", "Apr 9", "Apr 23", "May 7"]
    if Day == "Mon":
        for day_list in gold:
            if today == gold[day_list]:
                return "gold"
        for day_list in white:
            if today == white[day_list]:
                return "white"

def schedule(color):
    send_time = (hour() == 7 and minute() == 15)
    Day = day()
    if Day == "Mon" and send_time and color == "gold":
        send_msg("You have CSA, CSP, and Adv Programming today.")
    if Day == "Tue" and send_time and color == "gold":
        send_msg("You have 3D Print, ECS, CSA, and CSP today.")
    if Day == "Wed" and send_time and color == "gold":
        send_msg("You have 2 classes of ECS today.")
    if Day == "Thu" and send_time and color == "gold":
        send_msg("You have Adv Programming, CSA, and CSP today.")
    if Day == "Fri" and send_time and color == "gold":
        send_msg("You have CSP, ECS, 3D Pring, and CSA today.")
    if Day == "Mon" and send_time and color == "white":
        send_msg("You have Adv Programming today, CSA, and CSP today.")
    if Day == "Tue" and send_time and color == "white":
        send_msg("You have CSA, CSP, and ECS today.")
    if Day == "Wed" and send_time and color == "white":
        send_msg("You have 3D Print, ECS, CSA, and CSP today.")
    if Day == "Thu" and send_time and color == "white":
        send_msg("You have 2 classes of Adv Programming today.")
    if Day == "Fri" and send_time and color == "white":
        send_msg("You have 3D Print, ECS, CSA, and CSP today.")

def quote():
    quote_list = ["Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.",
        "The journey of a thousand miles begins with a single step.",
        "Knowing others is intelligence; knowing yourself is true wisdom. Mastering others is strength; mastering yourself is true power.",
        "A good traveler has no fixed plans and is not intent on arriving.",
        "Life is a series of natural and spontaneous changes. Don't resist them; that only creates sorrow. Let reality be reality. Let things flow naturally forward in whatever way they like.",
        "Those who know do not speak. Those who speak do not know.",
        "When you are content to be simply yourself and don't compare or compete, everyone will respect you.",
        "The truth is not always beautiful, nor beautiful words the truth.",
        "When I let go of what I am, I become what I might be.",
        "Time is a created thing. To say 'I don't have time,' is like saying, 'I don't want to.",
        "A man with outward courage dares to die; a man with inner courage dares to live.",
        "Care about what other people think and you will always be their prisoner."]
    return random.choice(quote_list)

def message():
    # Basic variables for authorization:
    user = "YourName" # For shits and giggles...
    email = 'youremail@altamontschool.org'
    pwd = 'yoursupersecretpassword'
    auth = (email, pwd)
    # Message object:
    m = Message(auth=auth)
    # Recipients
    m.setRecipients('I generally create a list and pass it through here.')
    # Subject:
    m.setSubject('Automation rules')
    # Body:
    m.setBody('Good morning, {}.\n\nHAL-9000'.format(user))
    # Send:
    m.sendMessage()

while True:
    morning()
    schedule(week())
    Hour = hour()
    Min = minute()
    print(str(Hour) + ":" + str(Min))
    if Hour == 7 and Min == 55:
        send_msg(quote())
        print('Good morning message sent.')
        message()
        print('Sent an email, too...')
    time.sleep(60)
