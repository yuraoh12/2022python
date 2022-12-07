from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# options = webdriver.ChromeOptions()
# options.add_argument('headless')

# chrome_driver = 'C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe'

# driver = webdriver.Chrome(chrome_driver, options=options)

# # 긁어갈 사이트 호출
# driver.get("http://www.python.org")

# print(driver.title)
# assert "Python" in driver.title # 테스트 코드

# elem = driver.find_element(By.CLASS_NAME, "shrubbery") # name 속성으로 찾기
# val = elem.get_attribute('class')
# print(val)
# elem = driver.find_element(By.CLASS_NAME, "q") # class 속성으로 찾기
# elem = driver.find_element(By.ID, "q") # id 속성으로 찾기
# elem = driver.find_element(By.TAG_NAME, "q") # 태그명으로 찾기
# input 텍스트 초기화
# elem.clear()

# # 마우스 클릭
# elem.click()

# # 키보드 엔터
# elem.send_keys(Keys.RETURN)


# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


options = webdriver.ChromeOptions()
options.add_argument('headless')

chrome_driver = 'C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe'

driver = webdriver.Chrome(chrome_driver, options=options)

# 긁어갈 사이트 호출
driver.get("https://media.naver.com/press/087/ranking?type=popular")

ranking_date = driver.find_element(By.CLASS_NAME, 'press_ranking_date')
button = ranking_date.find_element(By.CLASS_NAME, 'button_date_prev')
date = ranking_date.find_element(By.TAG_NAME, 'strong').text

print(button)
print(date)

button.click()
time.sleep(0.5)
date = ranking_date.find_element(By.TAG_NAME, 'strong').text
print(date)

button.click()
time.sleep(0.5)
date = ranking_date.find_element(By.TAG_NAME, 'strong').text
print(date)

# ranking_list = driver.find_element(By.CLASS_NAME, 'press_ranking_list')
# ranking_list = ranking_list.find_elements(By.CLASS_NAME, 'as_thumb')

# print(ranking_list[0].find_element(By.TAG_NAME, 'a').get_attribute('href'))
