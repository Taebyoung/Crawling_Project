# DC만갤 다운로더 (beta)

> 주의 : 해당 프로그램의 이용은 한국 저작권법 또는 일본 저작권법에 의해 처벌 대상이 될 수 있습니다.


### 목적
DC만갤 다운로더는 [DCinside만화 갤러리 개념글](https://gall.dcinside.com/board/lists?id=comic_new2&exception_mode=recommend) 웹페이지의 게시물 다운로드 및 게시판 분석을 위한 파이썬 프로그램입니다. 프로그램의 사용을 위해서는 파이썬 설치 및 관련 패키지 설치가 필요합니다.


### DC 만갤 소개

DC만갤에는 아직 국내에 정식 출간되지 않은 만화책을 번역하고 공유합니다. 하루에 10 ~ 20건의 게시물이 올라오고 인기가 많은 만화들은 국내에 정식 출간 되어 주목을 받기도 합니다. (예 : "파이어 펀치! 파이어 펀치!") 숨겨진 보석같은 일본 만화를 찾고 싶다면 DC만갤 다운로더를 이용하세요.



## Requierments

```
pip install scrapy
pip install scrapy-fake-useragent

# image download
pip install Pillow

# use mongoDB
pip install pymongo
```



## 사용법
- 개념글 이미지 다운로드 (/comics)
`$ scrapy crawl Comics -a PAGE_NUM (default=1)`
혹은
`$ run.sh`
  - 이미지 파일 저장 경로 : '/comics/images'

- 개념글 페이지 리스트 제작 (csv)
`$ scrapy crawl Comics -o '파일이름.csv `
  - csv 저장경로 : '/comics'


- 몽고 DB 사용자
  - 몽고 DB 기능 사용 설정
    - 기능 활성화
      1. '/comics/comics/setting.py' : 파일 열기
      2. 'Pipe line' 수정
  - 몽고 DB IP 등록 경로
    1. `comics/comics/mongodb.py' : 파일 열기
    2. `client = pymongo.MongoClient('mongodb://MY_IP:MONGODB_PORT/')`
  - 몽고 DB 설정
    1. `client.YOUR_DATABASE_NAME` : 데이터 베이스 이름 설정
    2. `client.YOUR_COLLECTION_NAME` : 컬렉션 이름 설정
  - 프로그램 실행 (/comics)
    1. `scrapy crawl Comincs -a PAGE_NUM`



### 크롤링 제공 데이터
- title : 게시글 제목
- date : 날짜 (년
- views : 조회수 (크롤링 시점)
- recommend : 추천수 (크롤링 시점)
- link : 게시글 링크
- img_count : 이미지 개수
- img_link : 이미지 링크 (1개만 제공)



### 프로그램 사용 주의사항
- 과도한 크롤링 금지 (1회 25 페이지 이상)
  - 해당 프로그램의 과도한 사용은 dcinside의 운영 정책에 따라 IP가 차단될 수 있습니다.
- 일부 이미지 파일 다운로드 불가
  - DCinside 내부 업로드 자료의 경우 다운로드가 불가능합니다.



## UPDATE PLAN
### BUG FIX
1. 다운로드 이미지 파일 이름 추가
2. DCinside 내부 저장소 사용 이미지 파일 다운로드



### UPDATE ROAD MAP
- 제목 검색 기능 지원 (예 : "번역", "만화 제목")
- 이전 만화 갤러리 개념글 다운로드 지원 (현재 url : comic_new2 / 2015.09.25 게시판 변경)
- DB check를 통한 중복 데이터 제외 처리
