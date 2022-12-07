import journal_scrap as js
import news_scrap as ns
import file_manager as fm

# 1. 언론사 목록 가져오기
jlist = js.get_all_journal_list()
js.print_journal_list(jlist)

# 2. 언론사별 뉴스 가져오기
journal = jlist[0]
news_list = ns.get_new_list_by_journal(journal)

# 3. 뉴스 목록을 JSON으로 파일저장
file_path = f"C:/work/python/scrap2/data/서울경제.json"
fm.save_news_to_json(file_path, news_list)

# 4. 뉴스 목록을 JSON파일에서 가져오기
file_path = f"C:/work/python/scrap2/data/서울경제.json"
news_list = fm.load_json_to_news(file_path)
ns.print_news_list(news_list)

