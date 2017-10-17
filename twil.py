import datetime
import time
from twilio.rest import Client


accountSID = 'yourSID'
authToken= 'yourAuthToken'
twilio_cli = Client(accountSID, authToken)
twilio_number = '+Twilio'
cell_phone = '+sms_enabled_phone'


def modified_date():
    # Used the lines below to find the most recent Monday based on current date
    current_date = datetime.date.today()
    monday = current_date - datetime.timedelta(days=current_date.weekday())
    month = monday.strftime("%b")
    date = monday.strftime("%d")
    global day
    day = current_date.strftime("%A")
    global scannable
    scannable = (month + " " + date)


def week():
    global color
    gold = ["Aug 21", "Sep 4", "Sep 18", "Oct 9", "Oct 23", "Oct 6", "Oct 20", "Oct 6", "Oct 20", "Dec 4", "Jan 1", "Jan 15", "Jan 29", "Feb 12", "Feb 26", "Mar 12", "Apr 2", "Apr 16", "Apr 30", "May 14"]
    white = ["Aug 28", "Sep 11", "Sep 25", "Oct 2", "Oct 16", "Oct 17", "Oct 30", "Nov 13", "Nov 27", "Dec 11", "Jan 8", "Jan 22", "Feb 5", "Feb 19", "Mar 5", "Mar 19", "Mar 26", "Apr 9", "Apr 23", "May 7"]
    if any(scannable in x for x in gold):
        color = "Gold"
    else:
        color = "White"

def weekly_schedule():
    global ds # Daily schedule var
    if day == "Monday" and color == "White":
        ds = "Today is {} {}.\nYou have the first hour off.".format(color, day)
    elif day == "Tuesday" and color == "White":
        ds = "Today is {} {}.\nYou have the first hour off.".format(color, day)
    elif day == "Wednesday" and color == "White":
        ds = "Today is {} {}.\nYou have the first hour off.".format(color, day)
    elif day == "Thursday" and color == "White":
        ds = "Today is {} {}.\nYou have the last hour off.".format(color, day)
    elif day == "Friday" and color == "White":
        ds = "Today is {} {}.\nYou have the last hour off.".format(color, day)
    elif day == "Monday" and color == "Gold":
        ds = "Today is {} {}day.\nYou have last and first hours off!".format(color, day)
    elif day == "Tuesday" and color == "Gold":
        ds = "Today is {} {}day.\nToday sucks, bro.".format(color, day)
    elif day == "Wednesday" and color == "Gold":
        ds = "Today is {} {}day.\nYou have last and first hours off!".format(color, day)
    elif day == "Thursday" and color == "Gold":
        ds = "Today is {} {}day.\nYou have the first two hours and the last hour off!".format(color, day)
    elif day == "Friday" and color == "Gold":
        ds = "Today is {} {}day.\nYou have last two hours off!".format(color, day)


def send_msg():
    twilio_cli.api.account.messages.create(
    to=cell_phone,
    from_=twilio_number,
    body=ds)

def main():
    modified_date()
    week()
    weekly_schedule()
    send_msg()
    print('Success!')
    quit()

main()
