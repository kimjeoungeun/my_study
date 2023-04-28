# 데이터 수집 단계

# 데이터수집->데이터분석/처리->인공지능모델학습

# http(hypertext transfer protocol)
# request - respone
# client - server
# html(hypertxt markup language)
# 웹사이트를 표현하기 위한 언어
# <html></html>
# html 파싱

# import requests

# url="https://www.naver.com/"

# response=requests.get(url)
# status=response.status_code # 상태 코드
# html=response.text
# print(status) # 200 출력 (상태 코드)
# print(html)

# http 상태 코드
# 200 : OK
# 302 : Redirect 다른페이지로 바로 연결
# 400 : Bad Request 요청이 잘못됨
# 401 : Unauthorized 비인증됨
# 403 : Forbidden 접근 권한 없음
# 404 : Not Found 요청받은 내용이 없음
# 405 : Method Not Allowed 접근 방법이 잘못
# 500 : Interral Server Error 서버에러
# 501 : Not Implemented 서버가 지원안함
# 502 : Bad Gateway 잘못된 응답

# url 구조
# 프로토콜://호스트주소:포트번호/경로?쿼리
# http://naver.com/?~~~~
# 쿼리
# 쿼리이름=값&쿼리이름=값&쿼리이름=값
# import requests
# search_url="https://search.naver.com/search.naver?where=image&sm=tab_jum&query=" # %EC%B9%98%ED%82%A8=치킨(16진수)
# keyword="맥주"
# url=search_url+keyword
# response=requests.get(url)
# print(response.text)
# print(type(response.text))

# BeautifulSoup
# html 파싱(parsing)
# html을 객체 구조화해서 사용

# from bs4 import BeautifulSoup
# html 태그
# <태그이름 속성=속성값>내용</태그이름>
# html.head # html을 객체로 쓸 수 있게 해줌
# html.body
# html= "<html><body>Hello</body></html>"
# soup=BeautifulSoup(html, "html.parser")
# print(soup) # html 파싱 된 형태로 
# print(type(soup))
# print(soup.body) # html 파싱 된 형태로 
# print(type(soup.body))
# print(soup.body.text) # html 파싱 된 형태로 
# print(type(soup.body.text))

# import requests
# from bs4 import BeautifulSoup
# search_url="https://www.google.com/search?tbm=isch&q=" # %EC%B9%98%ED%82%A8=치킨(16진수)
# keyword="맥주"
# url=search_url+keyword
# response=requests.get(url)
# html=response.text
# soup=BeautifulSoup(html, "html.parser")
# imgs=soup.find_all('img')
# print(soup.body.div) # 바디만 가져옴
# import os
# folder_name="imgs"
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
# for idx, img in enumerate(imgs[1:]):
#     print(idx, "번째 이미지 저장")
#     file_name=f"{keyword}_{idx}.jpg"
#     file_path=os.path.join(folder_name, file_name)
#     img_response=requests.get(img['src'])
#     img_data=img_response.content
#     with open(file_path,"wb") as f: # 2진수 데이터로 씀 비트
#         f.write(img_data)

# enumerate(이터러블)
# 이터러블에 번호를 붙임
# 0부터 리스트 끝까지 이터러블을 반환해줌
# li1=["김연아", "류현진", "손흥민"]
# for idx, name in enumerate(li1): #인덱스와 함께 자동적으로 for문을 돌림
#     print(name) # 김연아 류현진 손흥민

# 네이버 IT/과학 뉴스 크롤링
import requests # 웹브라우저 대신 파이썬으로 정보를 받으려고
from bs4 import BeautifulSoup # html을 객체형태로 파싱해줌
url="https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
# headers={"User-Agent":"Mozilla/5.0"} --> 크롤링 방지 회피
response=requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
html=response.text
soup=BeautifulSoup(html, "html.parser")
div=soup.body.find('div', attrs={'class':'list_body'})
headlines=div.find_all('a', attrs={'class':'cluster_text_headline'})
import os
folder_name="crawling_result"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
for headline in headlines:
    print(headline.text.strip())
    with open("crawling_result/headlines.txt","a", encoding="utf-8") as f:
        f.write(headline.text.strip())
        f.write("\n")
    # file_path=os.path.join(folder_name, file_name)
    # print(headline.text.strip())
    article_response=requests.get(headline['href'])
    article_soup=BeautifulSoup(article_response.text, "html.parser")
    article=article_soup.find('div', attrs={"id":"dic_area"})
    print(article.text)


# crawling_result 폴더의 headlines.txt 파일에 저장
# import os
# folder_name="imgs"
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
# for idx, img in enumerate(imgs[1:]):
#     print(idx, "번째 이미지 저장")
#     file_name=f"{keyword}_{idx}.jpg"
#     file_path=os.path.join(folder_name, file_name)