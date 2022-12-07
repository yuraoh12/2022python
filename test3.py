from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from NS import ScrapUtil
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver_path = 'C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=options)

page = driver.get('https://media.naver.com/press/011/ranking?type=comment&date=20220622')
# driver.get('https://media.naver.com/press/087/ranking?type=comment&date=20220622')
li_list = page.find_element(By.CLASS_NAME, 'press_ranking_list').find_elements(By.CLASS_NAME, 'as_thumb')
print(li_list)