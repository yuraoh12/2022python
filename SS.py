from tkinter import W
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from NS import ScrapUtil
import time

class NewsSpiderSele():

    def __init__(self) :
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.driver_path = 'C:/Users/taeji/Downloads/chrome-driver/chromedriver.exe'
        self.driver = webdriver.Chrome(self.driver_path, options=self.options)

    def get_journal_page(self, url) :
        # 긁어갈 사이트 호출
        print('url' , url)
        self.driver = webdriver.Chrome(self.driver_path, options=self.options)
        page = self.driver.get(url)
        time.sleep(3)
        return page

    def get_news_id(self, string) :
        idx1 = string.rfind('/') 
        idx2 = string.find('?') 
        id = string[idx1 + 1 : idx2]
        return id

    def get_my_news(self, elem) :

        link = elem.find_element(By.TAG_NAME, 'a').get_attribute('href')
        id = self.get_news_id(link) 
        ranking = elem.find_element(By.TAG_NAME, 'em').text
        title = elem.find_element(By.CLASS_NAME, "list_title").text

        news = {
            'id' : id,
            'ranking' : int(ranking),
            'title' : title,
            'link' : link
        }

        return news

    def get_rangking_list(self, url) : 
        # print('page', url)
        # page = self.get_journal_page(url)
        # print('page', page)
        self.driver = webdriver.Chrome(self.driver_path, options=self.options)
        url += '&date=20220622'
        print('url', url)
        self.driver.get(url)
        time.sleep(3)
        li_list = self.driver.find_element(By.CLASS_NAME, 'press_ranking_list').find_elements(By.CLASS_NAME, 'as_thumb')
        date = self.driver.find_element(By.CLASS_NAME, 'press_ranking_date').get_attribute('data-init-date')
        my_news_list = []
        for li in li_list :
            news = self.get_my_news(li)
            news['date'] = ScrapUtil.get_formated_date(date)
            my_news_list.append(news)
        
        return my_news_list
