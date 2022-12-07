from NS import MyScraper, View
from SS import NewsSpiderSele

url = 'https://news.naver.com/main/ranking/popularMemo.naver'
nss = NewsSpiderSele()
ms = MyScraper(url)
v = View()

journal_list = ms.get_all_journal()
v.print_journal(journal_list[0])
news_list = nss.get_rangking_list(journal_list[0]['view_link'])
v.print_news_list(news_list)
