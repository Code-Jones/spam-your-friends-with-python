import smtplib
import os
import time
import random

Host_Email_Address = "happybirthdaybitbh@gmail.com"
Host_Email_Pass = "Hbirthday2020"
Test_Email = "mdjones1793@gmail.com"
Thomas_Email = "thomas.otsig@gmail.com"
Kev_Email = "kevinkicks19@gmail.com"

file = open("jokelist.txt", "r")
jokelist = file.readlines()

try:
    for i in range(12):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(Host_Email_Address, Host_Email_Pass)
            Random_Joke = random.choice(jokelist)

            subject = 'Happy Birthday!!!'
            body = "Here\'s a random joke scraped from the interwebs:\n\n" + Random_Joke
            msg = f'subject: {subject}\n\n\{body}'

            smtp.sendmail(Host_Email_Address, "quilla@shaw.ca", msg)
        time.sleep(random.randint(1,10))
except Exception as e:
    print(e)
