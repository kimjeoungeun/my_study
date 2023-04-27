# 표준 라이브러리
# 모듈을 모아둔 것
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 때 자동으로 함께 설치
# 따로 설치하지 않고 import 명령어로 불러옴

# datetime
# 날짜 관련 라이브러리
# datetime의 date 객체 사용

# import datetime
# day1=datetime.date(2023,4,17)
# day_end=datetime.date(2023,9,18)
# diff=day_end-day1 # date 숫자형 변수 산술연산자
# print(diff.days)

# 2018년 8월 6일 무슨 요일일까요?
# weekday() ->> 0:월요일 ~ 6:일요일
# import datetime
# day=datetime.date(2018,8,6)
# weekdays=["월요일","화요일","수요일","목요일","금요일","토요일","일요일"] # 리스트랑 함수의 결과값 같이 사용
# print(day.weekday()) # 0은 월요일
# print(weekdays[day.weekday()])

# datetime의 포맷팅 코드
# 날짜랑 시간 표시하는 방법
# 년/월/일
# 월/일/년
# 일/월/년
# 2023년/4월/27일
# 2023-04-27
# 23년 4월 27일

# import datetime
# today=datetime.datetime.today()
# print(today)
# strftime()
# print(today.strftime("%Y년 %m월 %d일")) # 문자열포맷팅코드
# %Y 년 4자리 연도 모두 출력
# %y 년도 2자리
# %m 월
# %d 일
# %H 시간(24시간)
# %I 시간(12시간)
# %M 분(월과 구분할 것)
# %S 초
# %A 요일
# print(today.strftime("%A")) # Thursday 출력

# time 라이브러리
# 시간 관련
# import time
# time_now=time.time()
# print(time_now)
# print(time.strftime("%H:%M:%S", time.localtime(time_now))) # 세계 표준시 기준, 1970년 1월 1일 기준 흘러간 초(53년전)

# import time
# print("before")
# time.sleep(2) # ()초 동안 멈췄다가 실행됨
# print("after")
# for i in range(10):
#     print(i)
#     time.sleep(1)
# 정확한 1초는 아니다

# math
# 수학 관련
# import math
# result=math.ceil(1.1) # 올림 함수
# print(result)
# result=math.floor(1.9) # 내림
# print(result)
# print(math.pi) # 파이값

# random
# 난수 관련
import random
# random.random()
# 0.0~1.0 사이의 실수 중 난수 값 (범위데이터 만들 때 사용)
# random_value=random.random()
# print(random_value)

# random.randint(시작, 끝)
# 시작~끝 사이의 정수 중 난수 값 (rnage와 구별)
# random_value=random.randint(1,10)
# print(random_value)

# random.choice(리스트)
# 리스트의 요소 중 무작위로 하나를 리턴
# foods=["서브웨이","맥도날드","짜장면","국밥","김치찌개"]
# food=random.choice(foods)
# print(food)

# shuffle(리스트)
# 데이터들의 순서, 위치 바꿔줌
# li=[1,2,3,4,5]
# random.shuffle(li)
# print(li)

# 로또번호(자동)
# lotto_numbers=list(range(1,46))
# my_lotto=[]
# for i in range(6):
#     random_value=random.choice(lotto_numbers) # 범위에서 하나 선택이므로 중복가능성이 있음
#     if random_value not in my_lotto: # ~가 ~안에 없으면 True, 있으면 False
#         my_lotto.append(random_value)
# print(my_lotto)

# in 연산자
# a in b (b=문자열,리스트, 튜플 등)
# a가 b에 포함되어 있으면 True
# a가 b에 포함되어 있지 않으면 False

# not in 연산자
# a not in b (b=문자열,리스트, 튜플 등)
# a가 b에 포함되어 있지 않으면 True
# a가 b에 포함되어 있으면 False

# li=[1,2,3,4,5]
# a=10
# for i in li:
#     if a == i :
#         print("이미 있음")

# if a in li:
#     print("이미 있음") # 훨씬 간결, 효율적

# lotto_numbers=list(range(1,46))
# random.shuffle(lotto_numbers)
# my_lotto=lotto_numbers[:6]
# print(my_lotto)

# 색 이름과 음식 이름을 합치면
# 멋진 밴드 이름이 된다고 합니다.
# 색 이름과 음식 이름을 무작위로 뽑아
# 밴드 이름을 추천하는 프로그램을 만들어보세요.

# """
# 베이지 블랙 블루 회색 청색 레드 파란 핑크 그레이
# 쭈꾸미 요거트 오란다 와플 아이스티 떡볶이 커피
# """
# import random

# colors=["베이지", "블랙", "블루", "회색","청색","레드","파란","핑크","그레이"]
# foods=["쭈꾸미","요거트","오란다","와플","아이스티","떡볶이","커피"]

# color=random.choice(colors)
# food=random.choice(foods)
# print(f"{color}{food}")

# band_name=(color+food)
# print(band_name)

# 숫자야구 게임
# 1. 정답을 정한다. 정답은 4자리 숫자(랜덤)
# 2. 게임유저가 정답을 입력한다.
# 3. 정답과 비교해서 S/B/OUT 개수를 알려준다
# 4. 정답을 맞추거나, 종료를 입력하면 끝낸다.
# 5. 정답을 맞췄을 때 한번 더 하시겠습니까?
# import random
# answer=random.randint(1000,9999) #중복수 제거가 안됨
# numbers=list(range(10)) # 0부터 9까지 중복없이 4개 뽑기
# random.shuffle(numbers)
# answer = numbers[1:5] if numbers[0]==0 else numbers[:4] # 0인덱스에 0이 오면 참값 0인덱스값 제외 1,5인덱스까지 출력, 아니면 거짓값 4인덱스까지 출력


# while True:
#     user_input=input("정답은?")
#     if  user_input=="종료":
#         print("종료합니다.")
#         break
    # 공백입력은 어떻게 처리할까요
    # user_input.strip() # 공백제거 함수
    # 숫자가 아니면
    # 오류가 뜨고 다시 입력하세요.->처음으로간다->countiue쓴다
    # isdigit() 숫자로만 이루어진 문자열인지 확인한다.
    # 숫자로만 이루어있으면 True 아니면 False
    # if not user_input.isdigit():
    #     print("4자리 숫자만 입력하세요.")
    #     continue
    # 만약 4자리 숫자가 아니면 다시 입력하게 한다. ->처음으로 간다->countinue
    # elif len(user_input) != 4:
    #     print("4자리 숫자만 입력하세요.")
    #     continue
    # elif user_input[0]=="0":
    #     print("앞자리에 0은 들어갈 수 없습니다.")
    #     continue
    # 중복된 숫자 ex. 8888
    # duplicate=False # 중복이 아니라고 가정 / 중복인지 확인하는 변수 선언
    # for i in range(3): # 3글자확인 4글자중 앞에 3개에서 중복확인하므로
    #     if user_input[i] in user_input[i+1:]: # i가 인덱스0이고 나머지 인덱스 123 중복확인
    #         duplicate=True # 중복이면
    #         break # 빠져나와
    # if duplicate:
    #     print("중복된 숫자가 없게 입력하세요.")
    #     continue # while문으로 가야함
    # strike=0
    # ball=0
    # out=0 # 처음에 다 0개씩
    # for i in range(4): # for문 4번 돌면서 1자리씩 체크
    #     input_value=int(user_input[i]) # 입력받은건 문자열이므로 정수형으로 수정
    #     if input_value not in answer: # 입력된 값이 정답에 포함되는지 여부 확인. answer엔 4자리 숫자가 들어있음
    #         out += 1 # 포함안되어있으면 아웃
    #     elif input_value==answer[i]: # 정답에 숫자가 들어있으면서 자리도 맞다
    #         strike += 1 # 스트라이크를 하나 올린다
    #     else: # 숫자는 포함되어있는데 자리수는 안맞으면 볼
    #         ball += 1
    # print(f"strike:{strike}, ball:{ball}, out:{out}")

    # if strike == 4:
    #     print("정답!")
    #     user_input=input("한번 더 하시겠습니까?[y/n]") # user_input 변수가 다시 할당되어 문자열을 입력해도 상관없다.
    #     if user_input=="y":
    #         numbers=list(range(10)) 
    #         random.shuffle(numbers)
    #         answer = numbers[1:5] if numbers[0]==0 else numbers[:4]
    #         break

# 삼항 연산자
# 연산자가 항을 3개 가짐
# 참일때값 if 조건 else 거짓일때값 (조건이 True면 참일때값, 조건이 False면 거짓일때값 입력)
# result="참" if True else "거짓"
# result="참" if False else "거짓"
# print(result)

# def is_odd_numbers(n):
#     return "홀수" if n%2==1 else "짝수" # 조건이 참이면 홀수, 거짓이면 짝수



# os
# os 자원을 제어
# os.environ
# 시스템의 환경 변수 값을 리턴한다.
# import os
# print(os.environ)

# os.getcwd()
# get current working directory
# 현재작업위치 현재작업공간
# import os
# print(os.getcwd()) # 상대경로 사용하기때문에 현재위치가 중요

# os.mkdir(디렉터리)
# 현재작업공간에 디렉토리(폴더)를 만든다
# import os
# os.mkdir("폴더1")

# os.rename(원래이름, 바꿀이름)
# 파일의 이름을 바꾼다
# import os
# os.rename("파일1", "파일2")

# os.rmdir(디렉터리)
# 디렉터리(폴더)를 지운다.
# 폴더 안이 비어있어야함
# import os
# os.rmdir("폴더1")

# os.unlink(파일)
# 파일을 지운다.
# import os
# os.unlink("파일2") # 상대경로로 지움

# os.path
# os.path.exists("경로")
# 파일이 있으면 True, 파일이 없으면 False
# import os
# if not os.path.exists("없는파일"):
#     f=open("없는파일","r")
# else:
#     print("파일이 없습니다.")

# if not os.path.exists("없는파일"):
#     f=open("없는 파일","w")
#     f.close()
# f=open("없는파일","r")

# os.path.join("경로", "경로", "경로")
# 경로를 합쳐서 1개의 경로로 만들어준다.
# import os
# cwd=os.getcwd()
# my_folder="python_study"
# file_name="test_file.txt"
# file_path=os.path.join(cwd, my_folder, file_name)
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("테스트 파일을 작성합니다.")


# 외부 라이브러리
# 파이썬 표준 라이브러리가 아닌 라이브러리
# pip를 사용해서 설치한다.

# pip
# package installer for python
# 파이썬 모듈, 패키지를 설치하는 도구
# PyPI(python Package Index) 파이썬 소프트웨어 저장 공간
# PyPI에 있는 파이썬 패키지를 설치해준다

# 패키지 설치(최신버전 설치)
# pip install 패키지이름
# 패키지 삭제
# pip uninstall 패키지이름

# 특정 버전으로 설치
# pip install 패키지이름==1.0.5

# 최신 버전으로 업그레이드
# pip install --upgrade 패키지이름

# 설치된 패키지 리스트 확인
# 패키지 리스트, 버전 출력
# pip list

# 터미널 pip list 검색, '' 안 설치
# pip install numpy, pip uninstall numpy

# pip freeze
# pip 기록
