import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import requests
from bs4 import BeautifulSoup

# 1. 크롬 드라이버 가져오기(크롬을 코드로 제어)

# 2. 크롬 브라우저로 특정 주소 접속하기
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
res = requests.get('https://n.news.naver.com/article/comment/056/0011271638', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
rst = soup.find(id='cbox_module')
print(rst.find(class_='u_vc'))

driver = webdriver.Chrome('C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe')
driver.get("https://n.news.naver.com/article/comment/056/0011271638")
time.sleep(4)
rst2 = driver.find_element(By.ID, 'cbox_module')
time.sleep(1)
rst3 = rst2.find_element(By.CLASS_NAME, 'u_cbox_chart_cnt')
print('class', rst3.get_attribute('class'))
print('txt', rst3.text)

rst4 = rst2.find_element(By.CLASS_NAME, 'u_cbox_chart_per')
print('class', rst4.get_attribute('class'))
print('txt', rst4.text)