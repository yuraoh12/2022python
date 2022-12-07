import json
# dic = '''
# {
#     "age" : 20,
#     "name" : "hong",
#     "home" : "Daejeon"
# }
# '''
#dic['age']
#dic = json.loads(dic)

# dic1 = {"no" : 1, "name" : "hong"}
# dic2 = {"no" : 2, "name" : "lee"}

# dic_list = [dic1, dic2]

def save_news_to_json(file_path, news) :
    with open(file_path, "w", encoding='utf-8-sig') as f :
        json.dump(news, f, ensure_ascii=False, indent=4)

def load_json_to_news(file_path) :
    with open(file_path, "r", encoding='utf-8-sig') as f :
        news_list = json.load(f)
        return news_list


