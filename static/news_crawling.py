import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup

# url = 'https://news.google.com/home?hl=en-US&gl=US&ceid=US:en'
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


# data = requests.get(url,headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')

# a = soup.select_one('#yDmH0d > c-wiz > div > div.c4Stqc > main > div:nth-child(2) > c-wiz > section > div.TDaRVd > div > div:nth-child(3) > c-wiz > c-wiz > div > article > div.XlKvRb > a')

# print(len(a['aria-label']))
# print(a['aria-label'])

# title = soup.select_one("#yDmH0d > c-wiz > div > div.c4Stqc > main > div:nth-child(2) > c-wiz > section > div.TDaRVd > div > div:nth-child(3) > c-wiz > c-wiz > div > article > div.XlKvRb > a")
# print(title["href"])



# second = soup.select_one("#yDmH0d > c-wiz > div > div.c4Stqc > main > div:nth-child(2) > c-wiz > section > div.TDaRVd > div > div:nth-child(4) > c-wiz > c-wiz > div > article > div.XlKvRb > a")
# print(second["aria-label"])


# third = soup.select_one("#yDmH0d > c-wiz > div > div.c4Stqc > main > div:nth-child(2) > c-wiz > section > div.TDaRVd > div > div:nth-child(4) > c-wiz > c-wiz > div > article > div.XlKvRb > a")
# third = soup.select_one("#yDmH0d > c-wiz > div > div.c4Stqc > main > div:nth-child(2) > c-wiz > section > div.TDaRVd > div")

#print(third)

#구글 뉴스 홈
#여기 구조는 왠만하면 안바뀌니깐 크롤링해도 됨, api 사용하면 좋겠지만 빠르게 해야하기 때문에!
#https://news.google.com/home?hl=en-US&gl=US&ceid=US:en
# (1) U.S. (2) World (3) Local (4) Business (5) Technology (6) Entertainment (7) Sports (8) Science (9) Health


# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

# soup = BeautifulSoup(data.text, 'html.parser')

# print(soup)

# a= soup.select_one('#old_content > table > tbody > tr:nth-child(3) > td.title > div > a')

# print(a['href'])
# # 코딩 시작


# 스파르타코딩 크롤링 설명
# https://online.spartacodingclub.kr/enrolleds/640d443260066fa494fc97f3/edetails/640d443360066fa494fc9817?course_id=5f0ae408765dae0006002816

#패스트 캠퍼스 것도 찾아보자




# 뉴스 api
# API키 : 0cd87bf4e15a4747a451db82c9fafac5
# import requests
# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=0cd87bf4e15a4747a451db82c9fafac5')
# response = requests.get(url)
# response = response.json()


# title = response['articles'][0]['title']
# content = response['articles'][0]['content']
# url = response['articles'][0]['url']
# press = response['articles'][0]['source']['name']

# print(content)






import requests #웹에 접속하는 라이브러리
from bs4 import BeautifulSoup #html에서 데이터를 파싱하는 라이브러리


URL = "https://edition.cnn.com/travel/article/worlds-busiest-airports-2022-aci/index.html"

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one('#maincontent')
# title_text=title.text
# title_text=title.text.strip()
# print(len(title_text))

import re

content = soup.select_one('body > div.layout__content-wrapper.layout-with-rail__content-wrapper > section.layout__wrapper.layout-with-rail__wrapper > section.layout__main-wrapper.layout-with-rail__main-wrapper > section.layout__main.layout-with-rail__main > article > section > main > div.article__content-container > div.article__content')
context_text = re.sub(r'\s+',' ', content.text)
# content_text=content.text.replace("  ", "")
# content_text=content_text.replace("\n", " ")
# content_text=content_text.replace("\r", " ")
# content_text=content_text.replace("\t", " ")

print(context_text)