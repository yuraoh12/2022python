from NS import ScrapUtil, MyScraper, View

#1. 댓글 랭킹으로 뉴스 가져오기
url2 = 'https://news.naver.com/main/ranking/popularMemo.naver'
ms = MyScraper(url2)
v = View()

# journal_list = ms.get_all_journal()
# news_list = ms.get_news_with_comment_rank(journal_list[0])
# v.print_news_list(news_list)

#2. 날짜 리스트 만들기
su = ScrapUtil()
result = su.get_date_list('20220612', '20220622')

#3. 날짜로 댓글 랭킹 뉴스 가져오기 - selenium

journals = ms.get_all_journal_by_date('20220612')
news_list = ms.get_news_with_comment_rank(journals[0])
v.print_news_list(news_list)

#4.댓글 정보 가져오기 - selenium


