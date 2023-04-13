
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@sparta.mjqohhf.mongodb.net/?retryWrites=true&w=majority')
db = client.goorm
users_collection = db.news_pj
# doc = {
#         'id_email':999,  
#         'pwd' :"많이 웃기"

#         }
# #doc 데이터 삽입 
# db.news_pj.insert_one(doc)


#users_collection.update_one({'userEmail':"pak926@nate.com"}, {'$set' : {'add':"추가"}})



test = 'sdlfkslkdfj'
test_list =[]
test_list.append(test)
print(test_list)