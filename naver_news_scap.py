import requests as req
from bs4 import BeautifulSoup

url='https://news.naver.com/main/ranking/popularDay.naver'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

res = req.get(url, headers=headers)

html_text = res.text

soup = BeautifulSoup(html_text, 'html.parser')
rs1 = soup.find(attrs={'class' : 'rankingnews_box_wrap _popularRanking'})
rs2 = rs1.find_all(attrs={'class' : '_officeCard'})

card0 = rs2[0]
url2 = card0.find(attrs={'class':'rankingnews_box'}).find('a')['href']

html2 = req.get(url2, headers=headers)
soup2 = BeautifulSoup(html2.text, 'html.parser')
ranking_list = soup2.find(attrs={'class' : 'press_ranking_list'}).find_all('li')
for item in ranking_list :
    link = item.find('a')['href']
    item.find('a').find('em').text
    item.find('')
    
def get_soup(url) :

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    
    html = req.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup

def get_journal_id(string) :
    idx1 = string.rfind('/') 
    id = string[idx1 - 3 : idx1]
    return id

def get_journal_list(tag) :
    boxes = tag.find_all(class_ = 'rankingnews_box')
    journal_list = []
    for box in boxes :
        a = box.find('a')
        link = a['href']
        id = get_journal_id(link)
        name = box.find(class_='rankingnews_name')

        journal ={
            'id' : id,
            'name' : name,
            'link' : link
        }
        journal_list.append(journal)

    return journal_list

    
def get_all_journal_list(url) :
    soup = get_soup(url)
    cards = soup.find_all(class_="_officeCard")
    result = []
    for card in cards :
        journal_list = get_journal_list(card)
        result.extend(journal_list)
    return result 
     
url3 = 'https://news.naver.com/main/ranking/popularDay.naver'
list = get_all_journal_list(url3)
print(list)

def get_article_id(string) :
    idx1 = string.rfind('/') 
    idx2 = string.find('?') 
    id = string[idx1 + 1 : idx2]
    return id

def get_my_article(elem) :

    domain = "https://n.news.naver.com"
    href = elem.find('a')['href'] 

    link = domain + href 
    id = get_article_id(link) 
    ranking = elem.find('em').text
    title = elem.find(class_="list_title").text
    
    article = {
        'id' : id,
        'ranking' : int(ranking),
        'title' : title,
        'link' : link
    }

    return article

def get_rangking_list(url) : 
    soup = get_soup(url)
    li_list = soup.find(class_='press_ranking_list').find_all('li')
    my_articles = []
    for li in li_list :
        article = get_my_article(li)
        my_articles.append(article)
    
    return my_articles
    
url1 = "https://media.naver.com/press/421/ranking?type=popular&date=20220620"
url2 = "https://media.naver.com/press/421/ranking?type=comment&date=20220620"
my_article_by_view = get_rangking_list(url1)   
my_article_by_comm = get_rangking_list(url2)   

def get_ranking_difference(list1, list2) :
    list1.sort(key = lambda element : element['id'])
    list2.sort(key = lambda element : element['id'])
    accu_list = []
    for item1, item2 in zip(list1, list2) :
        accu_list.append(abs(item1['ranking'] - item2['ranking']))
    return accu_list

def get_accuracy(list1, list2):
    ac_list = get_ranking_difference(list1, list2)
    result = []
    for ac in ac_list :
        result.append(100 - (5 * ac))
    
    return sum(result) / len(result)

def print_journal_list(journal_list) :
    for journal in journal_list :
        print(f"번호 : {journal['id']}")
        print(f"이름 : {journal['name']}")
        print(f"링크 : {journal['link']}")
        print("=============================================")
url3 = 'https://news.naver.com/main/ranking/popularDay.naver'
# soup = get_soup(url3)
# cards = soup.find_all(class_="_officeCard")
# result = []
# for card in cards :
jlist = get_all_journal_list(url3)
print_journal_list(jlist)