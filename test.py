from asyncore import write
from selenium import webdriver
import time
import pandas as pd 
from bs4 import BeautifulSoup
import csv


CHROMEDRIVER ="C:\\Users\\clean_water\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=CHROMEDRIVER)
google = 'https://www.google.com/'
google_img = 'https://www.google.co.jp/imghp?hl=ja&tab=wi&ogbl'

def export_to_csv():
  browser.get(google_img)
  print('search google')
  time.sleep(1)
  search = browser.find_element_by_name('q')
  search.send_keys('')
  time.sleep(1)
  search.submit()
  titles = []

  try:
    elms = browser.find_elements_by_xpath("//h3")
    print('success')

    for element in elms:
      titles.append([element.text])
    
    with open('test.csv', 'w', newline='', encoding='CP932', errors='replace') as f:
      write = csv.writer(f,lineterminator="\n")
      write.writerows(titles)        

  except:
    print('error')
    browser.close()

  time.sleep(2)
  browser.quit()

export_to_csv()
