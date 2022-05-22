import time
## import selenium library
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
## web project selenium
from selenium.webdriver.common.by import By



## connect driver to code file with path
c_option = Options()
c_option.add_argument(r"user-data-dir=C:\\Users\\PROGTAMING\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com/')

run = input('enter for run program:')

# Click to contacts in whatsApp
#contacts = driver.find_element_by_xpath('//div[@title = "New chat"]')
#contacts.click()

msg = input('/@Enter msg: ')

input('Enter Anything...')


##accept_cookies = driver.find_element_by_id('onetrust-accept-btn-handler')
##accept_cookies.click()

users = driver.find_elements_by_xpath('//div[@class="lhggkp7q ln8gz9je rx9719la"]')
for user in users:

    # click contact on WhatsApp
    user.click()

    # message box for typing with robot
    ##msg_box = driver.find_element_by_class_name('_13NKt')
    msg_box = driver.find_element_by_xpath('//div[@title = "Type a message"]')

    ## type message in range
    print()
    print("Message sending....")
    print()
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3HQNh ')
    button.click()

    print()
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    print()
    print("Message sent")
    print()
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    print()
