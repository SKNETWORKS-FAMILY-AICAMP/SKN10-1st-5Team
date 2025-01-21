# KIA FAQ 크롤링

## 주요 기능
- kia faq 페이지의 데이터를 크롤링
    - https://www.kia.com/kr/customer-service/center/faq
- 질문 카테고리기준 RDB화
    - 컬럼: Category, Question, Answer
- 결과 .csv 저장
    - kia_faq.csv

# 필수 요구사항 설치
두 가지 방법 중 택 1
```shell
pip install selenium beautifulsoup4 pandas
```
```shell
pip install -r requirements.txt
```

# chromedriver.exe
1. 크롬 버전 최신화
2. [크롬 드라이버 다운로드](https://developer.chrome.com/docs/chromedriver/downloads?hl=ko)
3. 프로젝트 하위에 경로 설정

# 크롤링 실행
```shell
python kia_faq_crawling.py
```
---
HoneyWater8