import requests 
from bs4 import BeautifulSoup 
import re
import app


# URL_list = ['https://edition.cnn.com/2023/04/05/politics/donald-trump-court-2024/index.html', 
#             'https://edition.cnn.com/travel/article/worlds-busiest-airports-2022-aci/index.html',
#             'https://edition.cnn.com/2023/04/04/europe/germany-mayor-syrian-refugee-intl/index.html',
#             'http://edition.cnn.com/2023/04/04/europe/russia-military-bloggers-war-machine-intl-cmd/index.html',
#             'https://edition.cnn.com/2023/04/05/asia/japan-overseas-military-aid-intl-hnk/index.html',
#             'https://edition.cnn.com/2023/04/04/business/elon-musk-forbes-billionaire-list/index.html',
#             'https://edition.cnn.com/2023/04/04/business/australia-aesop-loreal-natura-deal-intl-hnk/index.html',
#             'https://edition.cnn.com/2023/04/03/investing/china-renaissance-delays-results-missing-ceo-intl-hnk/index.html'
            
#             # 'https://edition.cnn.com/2023/04/04/football/arsenal-ticket-resale-spt-intl/index.html',
#             # 'https://edition.cnn.com/style/article/vogue-philippines-april-cover-intl-scli/index.html',
#             # 'https://edition.cnn.com/2023/04/04/opinions/march-madness-angel-reese-caitlin-clark-jill-biden-bass-ctrp/index.html',
#             # 'https://edition.cnn.com/2023/04/04/politics/six-week-abortion-ban-florida/index.html',
#             # 'https://edition.cnn.com/2023/04/03/world/artemis-2-astronaut-crew-scn/index.html',
#             # 'https://edition.cnn.com/2023/04/02/investing/tesla-sales/index.html',
#             # 'https://edition.cnn.com/2023/04/04/opinions/workers-strikes-wages-uk-unions-holgate/index.html',
#             # 'https://edition.cnn.com/style/article/dior-fashion-show-india-runway-artisans/index.html',
#             # 'https://edition.cnn.com/style/article/old-masters-da-vinci-egg-yolk-painting-scn/index.html',
#             # 'https://edition.cnn.com/style/article/monet-haze-air-pollution-study-scn/index.html',
#             # 'https://edition.cnn.com/style/article/gold-nugget-huge-australia-intl-scli/index.html',
#             # 'https://edition.cnn.com/2023/03/30/football/wayne-rooney-mls-all-star-arsenal-spt-intl/index.html'
#         ]

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# news_data = []
# cnt=1
# for url in URL_list:
#     news = []
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     title = soup.select_one('#maincontent')
#     title_text=title.text.strip()
   
#     content = soup.select_one('body > div.layout__content-wrapper.layout-with-rail__content-wrapper > section.layout__wrapper.layout-with-rail__wrapper > section.layout__main-wrapper.layout-with-rail__main-wrapper > section.layout__main.layout-with-rail__main > article > section > main > div.article__content-container > div.article__content')
#     context_text = re.sub(r'\s+',' ', content.text)

#     news.append(title_text)
#     news.append(context_text)
#     news_data.append(news)
#     print(cnt)
#     cnt += 1

# print(news_data[0][0]) #제목
# print(news_data[0][1]) #내용

# 22222222222
# URL = "http://edition.cnn.com/2023/04/05/china/macron-von-der-leyen-china-beijing-xi-jinping-visit-intl-hnk/index.html"
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# data = requests.get(URL, headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one('#maincontent')
# title_text=title.text
# title_text=title.text.strip()
# print(len(title_text))


# content = soup.select_one('body > div.layout__content-wrapper.layout-with-rail__content-wrapper > section.layout__wrapper.layout-with-rail__wrapper > section.layout__main-wrapper.layout-with-rail__main-wrapper > section.layout__main.layout-with-rail__main > article > section > main > div.article__content-container > div.article__content')
# context_text = re.sub(r'\s+',' ', content.text)

# print(context_text)
#-------------------------------------------------------------------


URL = "sdfsdf"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one('#maincontent')

title_text=title.text.strip()
print(len(title_text))


content = soup.select_one('body > div.layout__content-wrapper.layout-with-rail__content-wrapper > section.layout__wrapper.layout-with-rail__wrapper > section.layout__main-wrapper.layout-with-rail__main-wrapper > section.layout__main.layout-with-rail__main > article > section > main > div.article__content-container > div.article__content')
context_text = re.sub(r'\s+',' ', content.text)

print(context_text)
