
client_id = "https://lh3.googleusercontent.com/proxy/V0d6PzDACN2-0fdsz7y4bIJYa76wXs-uwFW4ySmdgZnnFnOM2N4ziUtQYjvZWtnof3fCk6MvTioEwYmdCYjHWGHc-ZOOxuH5qwX6oA5wp7IPa3KA6Wbl_PEVJRkYWR-tU36Cdys15zXPQy-XdWVYzi0-bPMpQZKoyX2SyETZq8_pDXD0-54j88EHMeTw=s0-h12-rw"
client_secret = "MB_SBW87gs"

import os
import sys
import urllib.request
import requests

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    #response_body = response.read()
    result = requests.get(response.geturl(),
                          headers= {"X-Naver-Client-Id":client_id,
                                    "X-Naver-Client-Secret" : client_secret})
    news_data.append(result.json())
    #print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


