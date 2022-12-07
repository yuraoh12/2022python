import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# 1. 크롬 드라이버 가져오기(크롬을 코드로 제어)
driver = webdriver.Chrome('C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe')

# 2. 크롬 브라우저로 특정 주소 접속하기
driver.get("https://www.naver.com")

# 3. 잠시 대기 하기 위해 time.sleep() 사용
time.sleep(1)

# 4. 필요한 태그 가져오기
tag = driver.find_element(By.ID, 'account')

# 5. 검색 체이닝
login_title = tag.find_element(By.TAG_NAME, 'h2').text
login_link = tag.find_element(By.CLASS_NAME, 'link_login')
login_link_href = login_link.get_attribute('href')

print(login_title)
print(login_link_href)

# 6. 인터랙션
query = driver.find_element(By.ID, 'query')
# 6.1 키보드
query.send_keys('장마')
time.sleep(1)
# query.send_keys(Keys.RETURN)
# time.sleep(3)
## clear - 지우기

# 6.2 마우스
login_link.click()
time.sleep(1)

# 7. 명시적 대기
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "myDynamicElement"))
)
# 8. 암묵적 대기
driver.implicitly_wait(10)


