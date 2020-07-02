import requests
from bs4 import BeautifulSoup

URL = "https://pun.me/pages/funny-jokes.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
list = []
ol = soup.ol
for li in ol.findAll('li'):
    x = str(li)
    list.append(str(x[4:-5]))
file = open("jokelist.txt", "w")
for i in list:
    file.write(i + "\n")
file.close()
