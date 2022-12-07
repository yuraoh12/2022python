from NS import MyScraper, View, JournalSpider, Spider

url = 'https://news.naver.com/main/ranking/popularDay.naver'
sc = MyScraper(url, '20200619')
url2 = 'https://news.naver.com/main/ranking/popularMemo.naver'
sc2 = MyScraper(url2, '20200619')
view = View()

# news = sc.get_all_news()
# view.print_news_list(news)

# jlist = sc.get_all_journal()
# view.print_journal_list(jlist)

# j = sc.get_journal_by_name('뉴스타파')
# view.print_journal(j)
# news_list = sc.get_news_by_journal(j)
# view.print_news_list(news_list)

# news_list1 = sc.get_all_news()
# news_list2 = sc2.get_all_news()

# print(sc.get_accuracy(news_list1, news_list2)) # 오차율 16%...

# view.print_news_list(news_list)
# journal = sc.get_journal_by_name('MBC')
# news_list = sc.get_news_with_comment_rank(journal)
# view.print_news_list(news_list)
# cinfo = sc.get_comment_info_of_news(news_list[0])
# print(cinfo)

# 1. 댓글 많은 순으로 게시물 스크랩핑
sc = MyScraper(url2, '20220622')
journals = sc.get_all_journal()
view.print_journal_list(journals)
news_list = sc.get_news_with_comment_rank(journals[0])
view.print_news_list(news_list)

# 파일로 저장

