from img_mail_time import send_img_email
from url_scraper import get_urls
from selenium import webdriver
from pathlib import Path
import sys
import platform

# Fill with your own information 

Sender_Email = None 
Sender_Pass = None
Target_Email = None
Img_Subject = None
Joke_File = None
Img_File = None
Num_Emails = None

if Sender_Email == None:
	Sender_Email = input("Enter sender's email: ")
if Sender_Pass == None:
	Sender_Pass = input("Enter sender's password: ")
if Target_Email == None:
	Target_Email = input("Enter receiver's email: ")
if Img_Subject == None:
	Img_Subject = input("What does the receiver like ? ")
if Num_Emails == None:
	Num_Emails = input("How many emails do you want to send ? ")


base_path = Path(__file__).parent
if platform.system() == "Windows":
	Driver_Path = (base_path / "./drivers/chromedriver.exe").resolve()
elif platform.system() == "Darwin":
    Driver_Path = (base_path / "./drivers/chromedriver").resolve()
else:
	print("Not supported")
wd = webdriver.Chrome(executable_path = Driver_Path)


get_urls(Img_File, Img_Subject, Num_Emails, wd)
wd.quit()
send_img_email(Num_Emails, Sender_Email, Sender_Pass, Target_Email, Img_Subject, Joke_File, Img_File)
