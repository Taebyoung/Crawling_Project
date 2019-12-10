# DC inside 만화갤러리 개념글 리스트
---

> 만갤의 번역 만화 리스트로 만들기


### Requierments
---

```
pip install scrapy
pip install scrapy-fake-useragent
```
- DB : pymongo를 사용한 개인 DB 사용

```
pip install pymongo
```

### 사용법

- 개인 사용자
  - csv 파일 생성 명령어
- AWS 및 DB 사용자
  - 몽고 DB 세팅 안내
  - 몽고 DB IP 등록법


### 제공 DB 예시
- title : 게시글 제목
- date : 날짜
- views : 조회수 (크롤링 시점)
- recommend : 추천수 (크롤링 시점)
- link : 게시글 링크
- img_count : 이미지 개수
- img_link : 이미지 링크 (1개만 제공)


### 주의사항
- 저작권 : 번역된 만화를 공유하는 것은 불법입니다. 해당 프로그램의 이용도 문제가 될 수 있습니다.
- 로봇 정책 위반 : dcinside는 구글을 제외한 크롤링을 제한합니다. 해당 프로그램의 사용은 dcinside의 운영 정책에 따라 IP가 차단될 수 있습니다.


### 추가하고 싶은 기능
- img 다운로드 및 DB화
- 제목 검색 크롤링 (예 : "번역", "만화 제목")
- DB check 및 업데이트
- 이전 만화 갤러리 개념글 다운로드 (현재 url : comic_new2 / 2015.09.25 게시판 변경)
