import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time
import random

def send_img_email(Num_Emails:int, Sender_Email:str, Sender_Pass:str, Target_Email:str, Img_Subject:str, Joke_File:str, Img_File:str):
    def random_line(file):
        with open(file, "r") as f:
            lines = f.readlines()
            return (random.choice(lines))
    for i in range(Num_Emails):
        time.sleep(2)
        message = MIMEMultipart("alternative")
        message["Subject"] = Img_Subject
        message["From"] = Sender_Email
        message["To"] = Target_Email

        Random_Joke = random_line(Joke_File)
        img_scr = random_line(Img_File)

        text = " " #idk why i need this but it breaks without it
        html = f"<html><body><p>Here\'s a random joke scraped from the interwebs:</p><br><p>{Random_Joke}</p><br><p>I know you like {Img_Subject} so here's some pic's of them</p><img src={img_scr}</body></html>"

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(Sender_Email, Sender_Pass)
            server.sendmail(
                Sender_Email, Target_Email, message.as_string()
            )
    print(f"Email #{i + 1} sent")
