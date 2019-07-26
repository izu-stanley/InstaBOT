#This bot uses SELENIUM to download ALL pictures for a given Hashtag 
#No login required
#Makesure you are using ipython

!pip install selenium
!apt --fix-broken install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
wait = WebDriverWait(driver, 2)
driver.get('https://www.instagram.com/explore/tags/10yearchallenge/')
soup = BeautifulSoup(driver.page_source,"lxml")

def open_image():
    arguement = "/html[1]/body[1]/span[1]/section[1]/main[1]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]"
    clicker = driver.find_element_by_xpath(arguement)
    clicker.click()
def forward_click():
    arguement = "//a[@class='HBoOv coreSpriteRightPaginationArrow']"
    move_forward = driver.find_element_by_xpath(arguement)
    move_forward.click()

pic_df  = pd.DataFrame(columns = ['username', 'image_link', 'no_people','activity','hastags_present','comment','instagram_url'])

open_image()

total = 100000
for number in range(total):
    if number%50 == 0:
        time.sleep(5)
    try:
        try:
            arguement = "//div[contains(@class,'eLAPa kPFhm')]//img[contains(@class,'FFVAD')]"
            get_pic = wait.until(EC.presence_of_element_located((By.XPATH, arguement)))
            #get_pic = driver.find_element_by_xpath(arguement)
        except Exception as e:
            print(e)
            forward_click()



        string = get_pic.get_attribute('alt')
        string = string.split()
        no_people = string[3]
        activity = string[5:]


        image_link = get_pic.get_attribute('src')


        arguement = "//h2[contains(@class,'BrX75')]"
        username = driver.find_element_by_xpath(arguement)
        soup = username.get_attribute('innerHTML')
        soup = BeautifulSoup(soup,"lxml")
        username = soup.find('a').text


        instagram_url = driver.current_url


        desc = " "
        arguement = "//div[contains(@class,'C4VMK')]"
        description = driver.find_element_by_xpath(arguement)
        soup = description.get_attribute('innerHTML')
        soup = BeautifulSoup(soup,"lxml")
        for item in soup.findAll('a'):
            desc= desc + " " + str(item.string)
        taglist = desc.split()
        taglist = [x for x in taglist if x.startswith('#')]
        index = 0
        while index < len(taglist):
            taglist[index] = taglist[index].strip('#')
            index += 1

        comment = ""
        for x in soup.find('span').text.split('#'):
            if len(x.split()) > 1:
                comment = comment + x + '. '
        df = pd.DataFrame({'username':[username],'image_link':[image_link],'no_people':[no_people],'activity':[activity],'hastags_present':[taglist],'comment':[comment],'instagram_url':instagram_url})
        pic_df = pic_df.append(df, ignore_index=True)
        print('Finished scrapping ', number , ' of ' + str(total))
        time.sleep(0.2)
        forward_click()
    except Exception as e:
        forward_click()
        print(e)

import os, os.path

# simple version for working with CWD
print (len([name for name in os.listdir('.') if os.path.isfile(name)]))

# path joining version for other paths
DIR = '/content'
print (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

!ls -l | grep -v ^l | wc -l
