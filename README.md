# spam-your-friends-with-python

This is a one day project to create a script that emails a selected friend with terrible dad jokes and pictures of your choice. 

## Prerequisites
1. Python (current version 3.8.1)
2. Selenium for webscraping 
3. Python BeautifulSoup
4. Python Requests
5. Google chrome (current version 83.0.4103.116) 
6. Gmail account with **less secure apps** turned off (highly suggest making a test account for this)

**Important** 
This uses a chromedriver to scrape images. 
Please make sure the driver in the package is the same version as the current chrome browser you are using! 
Link =>https://sites.google.com/a/chromium.org/chromedriver/downloads

https://www.python.org/downloads/  
https://selenium-python.readthedocs.io/  
https://support.google.com/accounts/answer/6010255?hl=en  
https://requests.readthedocs.io/en/master/  
https://pypi.org/project/beautifulsoup4/  

```bash
pip install selenium
pip install beautifulsoup4
pip install requests
```

## Installation

1. Clone or download, unzip if you have too
2. Go to driver download as stated before and find the appropriate driver for your system and chrome version.
    Chrome version can be found under settings => about
    Move that to the downloaded folder
3. Mac users will get an alert about the driver cannot be authenticated. Go to settings => security => general => press the button at the bottom


## Usage

Either double click on the main.py and enter details in the terminal or open main.py in an editor and enter your details.

```python
# Enter you're details here
Sender_Email = "" 
Sender_Pass = ""
Target_Email = ""
Img_Subject = "" #This is what will be searched for pictures.
Joke_File = ""
Img_File = ""
Num_Emails = 1
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please enjoy
