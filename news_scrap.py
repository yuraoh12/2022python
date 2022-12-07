from bs4 import BeautifulSoup 
import requests 
import journal_scrap as js

url = "https://media.naver.com/press/662/ranking?type=comment" 

def set_url(url_param) :
    global url
    url = url_param

def get_soup() :    

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    res = requests.get(url, headers=headers); 

    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def get_news_id(link) :
    idx = link.rfind('/')   
    nid = link[idx + 1: idx + 11]  
    return nid

def get_my_news(news) :
    
    global url
    jid = js.get_journal_id(url)
    
    a = news.find('a')
    link = a['href']
    nid = get_news_id(link)    
    title = news.find(attrs={'class' : 'list_title'}).text  
        
    my_news = {
        'jid' : jid,
        'nid' : nid,
        'title' : title,
        'link' : link
    }
    
    return my_news

def get_my_news_list(ranking_news_list) :
    
    my_news_list = []
    for news in ranking_news_list :        
        my_news = get_my_news(news)   
        my_news_list.append(my_news)
        
    return my_news_list


def get_new_list_by_journal(journal) :
    set_url(journal['link'])
    soup = get_soup()
    ranking_lists = soup.find_all(attrs={'class' : 'press_ranking_list'})
    
    result_list = []
    
    # list.append(list2) -> list안에 list2 원소가 추가 => 2차원 리스트
    # list.extend(list2) -> list1과 list2를 합쳐서 확장. => 1차원
    
    for ranking_list in ranking_lists :    
        ranking_news_list = ranking_list.find_all(attrs={'class' : 'as_thumb'})        
        my_news_list = get_my_news_list(ranking_news_list)
        result_list.extend(my_news_list)
        
    return result_list
    
    
def print_news_list(news_list) :
    for news in news_list :
        print(f"언론사번호 : {news['jid']}")
        print(f"뉴스번호 : {news['nid']}")
        print(f"제목 : {news['title']}")
        print(f"링크 : {news['link']}")
        print(f"=========================================")