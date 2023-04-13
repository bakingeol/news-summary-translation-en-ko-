# news-summary-translation-en-ko-

## CNN news summary and translation en-ko

### 사용방법
- https://edition.cnn.com/ 
- CNN 사이트에서 뉴스기사 url을 메인페이지 url 주소입력에 넣어습니다.
- 좌측 하단의 요약하기 버튼을 누르고 최대 3분을 기다려 주세요 (cpu 환경으로 돌아가게 만들어서 오래 걸릴 수 있습니다.) 
- 요약 내용이 나오면 우측 하단의 번역하기 버튼을 누르시면 한국어로 뉴스기사 요약 및 번역된 정보를 얻을 수 있습니다. 

![MAIN](/news-summary-translation-en-ko-/image/main_image.png)

- LongT5(요약), m2m100(번역) 사전학습 모델 사용 
- 추후 유의미한 번역 및 요약 fine-tuning 모델을 학습시킬 경우 코드가 변경될 수 있습니다. 

