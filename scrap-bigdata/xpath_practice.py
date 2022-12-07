import requests as req
from bs4 import BeautifulSoup

url='https://news.naver.com/main/ranking/popularDay.naver'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

res = req.get(url, headers=headers)

html_text = res.text

soup = BeautifulSoup(html_text, 'html.parser')

# / : 절대 경로
# // : 문서 내에서 검색
# //*[@href] : href 속성이 있는 모든 태그 검색
# //tag[@href="http://google.com"] : tag에 href 속성 중 값이 "http://google.com"인 것 검색
#(//a)[3] : 문서의 세번째 a 선택
#(//a)[position < 3] : 문서의 2번째까지 선택

#ct > div.press_ranking_home > div:nth-child(3) > ul > li:nth-child(1) > a > div.list_content > strong