from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import journal_scrap as js
import news_scrap as ns
import file_manager as fm
url = ""

def get_driver(url_param) :
    global url
    url = url_param
    driver = webdriver.Chrome('C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe')
    driver.get(url)
    driver.implicitly_wait(10)
    return driver

def until_load_wait(target, key, value) :
    element = WebDriverWait(target, 10).until(
        EC.presence_of_element_located((key, value))
    )

    
def click_btn(element) :
    element.click()

def get_news_id(link) :
    idx = link.rfind('/')   
    nid = link[idx + 1: idx + 11]  
    return nid

def get_my_news(news, date) :
    
    global url
    jid = js.get_journal_id(url)
    
    a = news.find_element(By.TAG_NAME, 'a')
    link = a.get_attribute('href')
    nid = get_news_id(link)    
    title = news.find_element(By.CLASS_NAME, 'list_title').text 
    my_news = {
        'jid' : jid,
        'nid' : nid,
        'title' : title,
        'link' : link,
        'date' : date
    }
    
    return my_news

def get_my_news_list(ranking_news_list, date) :
    my_news_list = []
    for news in ranking_news_list :        
        my_news = get_my_news(news, date)   
        my_news_list.append(my_news)
        
    return my_news_list


def get_new_list_by_journal(element, date) :
    ranking_lists = element.find_elements(By.CLASS_NAME, 'press_ranking_list')
    
    result_list = []
    
    # list.append(list2) -> list안에 list2 원소가 추가 => 2차원 리스트
    # list.extend(list2) -> list1과 list2를 합쳐서 확장. => 1차원
    
    for ranking_list in ranking_lists :    
        ranking_news_list = ranking_list.find_elements(By.CLASS_NAME, 'as_thumb')
        my_news_list = get_my_news_list(ranking_news_list, date)
        result_list.extend(my_news_list)
        
    return result_list
    
def get_interval_new_list_by_journal(journal, interval_day) :
    element = get_driver(journal['link'])
    result_list = []
    for i in range(interval_day) :
        until_load_wait(element, By.CLASS_NAME, 'press_ranking_date')
        date = element.find_element(By.CLASS_NAME, 'press_ranking_date').get_attribute('data-init-date')
        btn = element.find_element(By.CLASS_NAME, 'button_date_prev')
        element.implicitly_wait(10)
        news_list = get_new_list_by_journal(element, date)
        result_list.extend(news_list)
        btn.click()

    return result_list
journal = js.get_journal_by_name('KBS')
    
news_list = get_interval_new_list_by_journal(journal, 5)
ns.print_news_list(news_list)

# click_btn(driver, 10, nav_param)
# time.sleep(3)
# click_btn(driver, 10, nav_param)
# time.sleep(3)
# click_btn(driver, 10, nav_param)
# time.sleep(3)



