from asyncore import write
from selenium import webdriver
import time
import pandas as pd 
from bs4 import BeautifulSoup as bs
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import requests

CHROMEDRIVER ="C:\\Users\\clean_water\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=CHROMEDRIVER)
google = 'https://www.google.com/'
google_img = 'https://www.google.co.jp/imghp?hl=ja&tab=wi&ogbl'

#検索してh3を抽出してCSVにエクスポート
def export_to_csv():
  browser.get(google)
  browser.find_element_by_name('q').send_keys('東京都',Keys.ENTER)
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
# export_to_csv()

#imagesフォルダを作成
folder_name = 'images'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

#画像をダウンロード
def download_image(url,folder_name,num):
  res = requests.get(url)
  if res.status_code ==200:
    with open(os.path.join(folder_name,str(num)+".jpg"),'wb') as file:
      file.write(res.content)

#画像を検索してダウンロード
def download_search_img():
  browser.get(google_img)
  browser.find_element_by_name('q').send_keys('icon twitter',Keys.ENTER)
  time.sleep(1)
  page_html = browser.page_source
  pageSoupe = bs(page_html,'html.parser')
  containers = pageSoupe.findAll('div',{'class':'isv-r PNCib MSM1fd BUooTd'},limit=3)
  
  len_containers = len(containers)
  titles = []
  for i in range(1,len_containers+1):
    xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)
    browser.find_element_by_xpath(xPath).click()
    time.sleep(1)
    
    previewImageXPath = """//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img"""
    previewImageElement = browser.find_element_by_xpath(previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")
    download_image(previewImageURL, folder_name, i)


download_search_img()