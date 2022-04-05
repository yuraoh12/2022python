from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_path = 'C:\오유라\chromedriver.exe'
url = 'http://www.naver.com'
browser = webdriver.Chrome(chrome_path)
browser.get(url)

#맨 처음 탭으로 이동
#browser.switch_to.window(window_handles[0])
#새롭게 열린 창, 팝업, 탭으로 전환
#browser.switch_to.window(window_handles[-1])
#스크린샷(현재 켜져있는 크롬 창의 화면 캡쳐 저장)
#browser.get_screenshot_as_file('capture.png')
#브라우저 창 닫음 
#browser.close()