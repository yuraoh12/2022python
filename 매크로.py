from selenium import webdriver
import time
chrome_path = 'C:\오유라\chromedriver.exe'
url = 'http://www.naver.com'

browser = webdriver.Chrome(chrome_path)
browser.get(url)
time.sleep(3)
browser.find_element_by_xpath('//*[@id="u_skip"]/a[5]').click()

#개발자 탭에서 태그에서 xpath 버튼 클릭해서 코드 실행
time.sleep(2)
browser.find_element_by_css_selector('#id').send_keys(id)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="log-in-button"]').click()

#Keys.ENTER = 엔터
#Keys.RETURN = 엔터
#Keys.SPACE = 스페이스
#Keys.ARROW_UP = 방향키 위
#Keys.ARROW_DOWN = 방향키 아래
#Keys.ARROW_LEFT = 방향키 왼쪽
#Keys.ARROW_RIGHT = 방향키 오른쪽 
#Keys.BACK_SPACE = 지우기
#Keys.DELETE = 지우기(딜리트)
#Keys.CONTROL = Ctrl
#Keys.ALT = ALT
#Keys.SHIFT = SHIFT
#Keys.TAB = TAB
#Keys.PAGE_UP = 스크롤 업
#Keys.PAGE_DOWN = 스크롤 다운 
#Keys.F1~9 = F1부터 F9까지 

#find_element_by_id = 'id 속성을 사용하여 접근'
#find_element_by_name = 'name 속성을 사용하여 접근'
#find_element_by_xpath = 'xpath 속성을 사용하여 접근'
#find_element_by_link_text ='앵커태그(a태그)에 사용되는 텍스트로 접근'
#find_element_by_partial_link_text = '앵커태그에 사용되는 일부 텍스트로 접근'
#find_element_by_tag_name = '태그를 사용해서 접근'
#find_element_by_class_name = '클래스를 사용해서 접근'
#find_element_by_css_selector = ' css선택자를 사용하여 접근'
