import os
import smtplib
import datetime as dt
import random
import pandas

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

bday_data = pandas.read_csv("scheduled-tasks\\birthdays.csv")
today_day = dt.datetime.now().day
today_month = dt.datetime.now().month

letters = []
with open("scheduled-tasks\letter_templates\letter_1.txt", "r") as file:
    letters.append(file.read())
with open("scheduled-tasks\letter_templates\letter_2.txt", "r") as file:
    letters.append(file.read())
with open("scheduled-tasks\letter_templates\letter_3.txt", "r") as file:
    letters.append(file.read())

for bday in bday_data.itertuples(index=False):
    if bday[3] == today_month and bday[4] == today_day:
        output_letter = random.choice(letters)
        output_letter = output_letter.replace("[NAME]", bday[0])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=bday[1],
                msg=output_letter)
            