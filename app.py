from flask import Flask, render_template, request, jsonify, url_for, redirect
import requests 
from bs4 import BeautifulSoup 
import re
from transformers import M2M100Config, M2M100ForConditionalGeneration, M2M100Tokenizer


app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@sparta.mjqohhf.mongodb.net/?retryWrites=true&w=majority')
db = client.goorm
users_collection = db.news_pj



import requests 
from bs4 import BeautifulSoup 
import re


import pprint as pp
import json
import torch
from transformers import AutoTokenizer, LongT5ForConditionalGeneration
device =  'cpu'

model_name = "pszemraj/long-t5-tglobal-base-16384-book-summary"
model_summary = LongT5ForConditionalGeneration.from_pretrained(model_name)
sum_tokenizer = AutoTokenizer.from_pretrained('t5-base')


@app.route('/')
def registration():
    return render_template('index.html')
    
#요약 모델 실행
def generate_summary(text):
    input_ids = sum_tokenizer.encode(text, return_tensors='pt', max_length=512, truncation=True).to(device)
    summary_ids = model_summary.generate(input_ids.to(device), max_length=150, num_beams=2, early_stopping=True)
    summary = sum_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


@app.route("/newsSummary", methods=["POST"])
def newsSummary():
    src_text = request.form.get("summary")
    print(src_text)
    src_text_list=[]
    src_text_list.append(src_text)
    model.to('cpu')

    summary = generate_summary(src_text_list[0])
    print(summary)
    return jsonify({'summaryResult' : summary}), 200
 





@app.route("/urlGet", methods=["POST"])
def urlGet():
    news_url= request.form.get('urlGet')
    #print(" 1. url 주소",news_url)
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(news_url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    title = soup.select_one('#maincontent')
    title_text=title.text.strip()
    content = soup.select_one('body > div.layout__content-wrapper.layout-with-rail__content-wrapper > section.layout__wrapper.layout-with-rail__wrapper > section.layout__main-wrapper.layout-with-rail__main-wrapper > section.layout__main.layout-with-rail__main > article > section > main > div.article__content-container > div.article__content')
    context_text = re.sub(r'\s+',' ', content.text)
    #context_text = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', context_text)
    #print(title_text)
    return jsonify({'news_summary' : [title_text,context_text]}), 200




from transformers import M2M100Config, M2M100ForConditionalGeneration, M2M100Tokenizer

model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M", src_lang="en", tgt_lang="ko")



@app.route("/newsTranslation", methods=["POST"])
def newsTranslation():
    src_text = request.form.get("translation")
    src_text_list=[]
    src_text_list.append(src_text)

    encoded_en = tokenizer(src_text_list[0], return_tensors="pt")
    generated_tokens = model.generate(**encoded_en, forced_bos_token_id=tokenizer.get_lang_id("ko"))
    answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
 
    return jsonify({'translationResult' : answer}), 200




#https://edition.cnn.com/2023/04/06/business/bob-lee-stabbing-911/index.html

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)











# import hashlib
# #회원가입
# @app.route("/register", methods=["POST"])
# def register():
#     userEmail = request.form.get('userEmail')
#     userPwd = request.form.get('userPwd')

#     # 복호화 비밀번호 digest(바이트 문자열) 또는 hexdigest(바이트 -> 16진수 문자열)  - 해싱코드 문자열 리턴
#     userPwd_hash = hashlib.sha256(userPwd.encode('utf-8')).hexdigest()
#     print("!!!!!!!회원가입중")
#     doc = users_collection.find_one({"userEmail": userEmail})
#     doc2 = {
#         'userEmail': userEmail,
#         'userPwd': userPwd_hash,
#     }
#     if not doc:
#         users_collection.insert_one(doc2)
#         return jsonify({'msg': '회원가입 성공했습니다.'}), 201
#     else:
#         return jsonify({'msg': '이미 존재하는 이메일 입니다'}), 409



# #로그인
# @app.route("/login", methods=["POST"])
# def login():
#     loginEmail = request.form.get('loginEmail')
#     loginPassword = request.form.get('loginPassword')  # store the json body request
#     # search for user in database

#     print("이메일이다 !!!!"+loginEmail)
#     user_from_db = users_collection.find_one({'userEmail': loginEmail})

#     print(user_from_db, "!!!!!!!!!!!!!!!!!")
#     if user_from_db:
#         encrpted_password = hashlib.sha256(
#             loginPassword.encode("utf-8")).hexdigest()
#         print("!!!!!!!!!!!!!!",encrpted_password)
#         if encrpted_password == user_from_db['userPwd']:
#             print("로그인 성공")
            
#             return jsonify({'msg2' : "성공성공"}), 200

#     return jsonify({'msg': 'The userName or password is incorrect'}), 401

