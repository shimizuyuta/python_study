from asyncore import write
from selenium import webdriver
import time
import pandas as pd 
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.common.keys import Keys

CHROMEDRIVER ="C:\\Users\\clean_water\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=CHROMEDRIVER)
google = 'https://www.google.com/'
google_img = 'https://www.google.co.jp/imghp?hl=ja&tab=wi&ogbl'


def export_to_csv():
  browser.get(google)
  print('search google')
  search = browser.find_element_by_name('q').send_keys('東京都',Keys.ENTER)
  time.sleep(1)
  titles = []

  try:
    elms = browser.find_elements_by_xpath("//h3")

    for element in elms:
      titles.append([element.text])
    
    with open('test.csv', 'w', newline='', encoding='CP932', errors='replace') as f:
      write = csv.writer(f,lineterminator="\n")
      write.writerows(titles)        

  except:
    print('error')
    browser.close()

  time.sleep(1)
  browser.quit()

export_to_csv()
