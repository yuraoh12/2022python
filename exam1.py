# pip 설명 및 설치 방법

# xml 파일 읽기
# from bs4 import BeautifulSoup

# # requests
# import requests as req
# # session 가져오기
# s = req.Session()

# # request
# # request와 response
# # get request
# r = s.get('https://www.naver.com')
# url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"

# # res = req.get(url)
# headers = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
# }
# r = s.get(url, headers=headers)
# print(r.headers)
# print(r.status_code)
# print(r.text)

# # post request
# s.close()

# header

# get, post 메서드

# ---- bs4 -----
from bs4 import BeautifulSoup

f = open('test.xml', 'r', encoding='utf-8-sig')
soup = BeautifulSoup(f, 'html.parser')
#print(soup.prettify())

# xml 태그 이름으로 찾기 - find or find_all(태그 이름)
tag = soup.find('person')
print(tag)

tags = soup.find_all('person')

# xml 클래스로 찾기 - find or find_all(class_=값), (attrs={"class" : 값})
# tags = soup.find_all( attrs={"no" :})

# xml id로 찾기 - find or find_all(id=값), (attrs={"id" : 값})

# xml 이름으로 찾기 - find or find_all(attrs={"name" : 값})

# 체이닝 - find().find().find()....

# 직계 자손 찾기 - recursive=False
tag = soup.find('person')
print(tag)
# 후손 찾기 - recursive=True

# 같은 항렬의 다음, 이전 - next_sibling, next_siblings, prev_sibling, prev_siblings

# next_element - 자손 태그가 있으면 자손을, 없으면 형제를

# next_elements - 자손 태그가 있으면 자손부터 전부, 없으면 형제 부터 전체 

# 텍스트 가져오기 - .text
# 속성 값 가져오기 - 태그['속성명']
