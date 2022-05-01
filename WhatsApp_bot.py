## for get to site
import requests
import time
## for save in databace spacify
import mysql.connector
## other theme
from bs4 import BeautifulSoup
## import selenium library
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip
## web project selenium
from selenium.webdriver.common.by import By
## for create userId random
from random import seed
from random import random
import random


## connect driver to code file with path
#c_option = Options()
#c_option.add_argument(r"user-data-dir=C:\\Users\\Meysam\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4")
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com/')

run = input('enter for run program')
name = input('/@Enter contact name: ')
msg = input('/@Enter msg: ')
count = int(input('/@How many times: '))

input('Enter Anything...')


##accept_cookies = driver.find_element_by_id('onetrust-accept-btn-handler')
##accept_cookies.click()



# click contact on WhatsApp
contact = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
contact.click()

# message box for typing with robot
##msg_box = driver.find_element_by_class_name('_13NKt')
msg_box = driver.find_element_by_xpath('//div[@title = "Type a message"]')

## type message in range
for i in range(count):
    print()
    print("Message sending....")
    print()
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_4sWnG')
    button.click()

    print()
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    print()
    print("Message sent")
    print()
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    print()
