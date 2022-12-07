from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import requests as req
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularMemo.naver" # 전역변수(모든 함수가 공유하는 변수)

def set_url(url_param) : # 지역변수(해당 함수만 사용하는 변수)
    global url
    url = url_param

# 1. 특정 페이지로 요청보내서 html 문서 받아오기.
def get_soup() :    

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    res = req.get(url, headers=headers); # url에 요청 보냄. 요청에 대한 응답이 리턴

    html = res.text # 응답 결과의 문서


    # find(태그이름 , 속성이름)
    # find_all
    # 체이닝
    # 실제 정보 값 -> text
    # 태그의 속성값 -> 태find(태그이름 , 속성이름)
    # find_all
    # 체이닝
    # 실제 정보 값 -> text
    # 태그의 속성값 -> 태그['속성명']

    soup = BeautifulSoup(html, 'html.parser')

    return soup

set_url('https://media.naver.com/press/056/ranking?type=comment')
soup = get_soup()

date = soup.find(class_='press_ranking_date')
button = date.find(class_='button_date_prev')

# 한계 -> 동적 페이지는 스크랩할 수 없다.

# 1. 크롬 드라이버 가져오기(크롬을 코드로 제어)
driver = webdriver.Chrome('C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe')

# 2. 크롬 브라우저로 특정 주소 접속하기
driver.get("https://media.naver.com/press/056/ranking?type=comment")

def click_btn(target, sec, nav_param) :
    element = WebDriverWait(target, sec).until(
        EC.presence_of_element_located((nav_param['By'], nav_param['value'])
    ))

    element.click()

nav_param = {
    'By' : By.CLASS_NAME,
    'value' : 'button_date_prev'
}
click_btn(driver, 10, nav_param)
time.sleep(3)
click_btn(driver, 10, nav_param)
time.sleep(3)
click_btn(driver, 10, nav_param)
time.sleep(3)

