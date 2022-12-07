from bs4 import BeautifulSoup # html형식으로 작성된 문자열을 html구조로 파싱하기 위한 모듈
import requests # 특정 서버에 웹요청 보내기위한 모듈

url = "https://news.naver.com/main/ranking/popularMemo.naver" # 전역변수(모든 함수가 공유하는 변수)

def set_url(url_param) : # 지역변수(해당 함수만 사용하는 변수)
    global url
    url = url_param

# 1. 특정 페이지로 요청보내서 html 문서 받아오기.
def get_soup() :    

    global url
    
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    
    res = requests.get(url, headers=headers); # url에 요청 보냄. 요청에 대한 응답이 리턴

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

def get_journal_id(link) :
    idx = link.rfind('/')        
    jid = link[idx-3:idx:1]
    
    return jid
    
# 언론사 구조화 
def get_my_journal(tag) :
    a = tag.find('a')

    strong = a.find('strong')
    
    link = a['href']
    jid = get_journal_id(link)
 
    name = strong.text

    my_journal = {
        "id" : jid,
        "name" : name,
        "link" : link
    }
    
    return my_journal


def get_journal_list_by_group(group_id) :
    soup = get_soup()
    tag = soup.find(attrs={'class' : group_id})
    alist = tag.find_all(attrs={'class' : 'rankingnews_box'})

    journal_list = []

    for tag in alist :
        
        my_journal = get_my_journal(tag)
        journal_list.append(my_journal)

    return journal_list


def print_journal_list(journal_list) :
    for j in journal_list :
        print(f"번호 : {j['id']}")
        print(f"일름 : {j['name']}")
        print(f"링크 : {j['link']}")
        print("======================")


def get_group_id_list(tags) :
    group_id_list = []
    for tag in tags :    
        group_id = tag['class'][0] + " " + tag['class'][1]
        group_id_list.append(group_id)
    return group_id_list
    

def get_all_journal_list() :
    soup = get_soup()
    print(soup)
    tags = soup.find_all(attrs={'class' : '_officeCard'})
    glist = get_group_id_list(tags)
    
    journal_list = []
    for gid in glist :
        journal_list.extend(get_journal_list_by_group(gid))
    
    return journal_list    

def get_journal_in_list(key, value) :
    for journal in get_all_journal_list() :
        if journal[key] == value:
            return journal

def get_journal_by_id(jid) :
    return get_journal_in_list("id", jid)

def get_journal_by_name(name) :
    return get_journal_in_list("name", name)



# 각 언론사별 기사(댓글정보) => 파일 저장 => 판다스로 읽어옴 => 간단한 분석