# 파일 입출력
# 파이썬에서 파일 생성, 수정
# 
# open()
# 파이썬 내장 함수
# 파일을 열고, 파일 객체를 리턴한다.
# open(파일 이름, 파일 열기 모드)
# f=open("C:/Users/405/my_study/Python_Study/새파일.txt", 'w')
# f.close() # 필수
# 파일의 경로
# 절대 경로 : c:/, d:/ 처럼 최상단 경로부터 나타낸 경로(어느위치에서 실행하든 상관없음)
# 상대 경로 : 현재 작업 위치부터 나타낸 경로(현재 실행한 위치가 중요)

# 파일 열기 모드
# r : 읽기 모드, 파일을 읽기만 할 때 사용 
# w : 쓰기 모드, 파일을 새로 만들거나 파일에 내용을 쓸 때 사용
# a : 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용

# f=open("Python_Study/새파일.txt", 'w', encoding="utf-8") # 쓰기모드
# for i in range(1,11):
#     print(i,"번째 줄") # 모니터화면, 터미널창 화면에 출력
#     f.write(str(i)+"번째 줄\n") # 파일에 데이터 출력
# f.close()
# # w 모드는 덮어쓰기 된다.
# f=open("Python_Study/새파일.txt", 'a', encoding="utf-8")
# for i in range(11,21):
#     print(i, "번째 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close()

# readline() 함수
# 첫번째 줄부터 1줄 읽어온다.
# 커서가 이동하는 것 처럼 읽어옴
# f=open("Python_Study/새파일.txt", 'r', encoding="utf-8")
# while True:
#     line=f.readline() 
#     if line=="": # 끝까지 다 읽었으면 빈문자를 읽을 때
#         break # 탈출
#     print(line)
# f.close()

# readlines() 함수
# 파일의 모든 줄을 읽어서 리스트로 반환
# f=open("Python_Study/새파일.txt", 'r', encoding="utf-8")
# lines=f.readlines()
# print(lines)
# f.close()
# # 리스트 출력
# # 한줄 단위로 끊어져 문자열
# for line in lines:
#     print(line)
# f.close()

# read() 함수
# 파일 내용 전체를 문자열로 리턴한다
# f=open("Python_Study/새파일.txt", 'r', encoding="utf-8")
# data=f.read()# 문자열 한 덩어리로 리턴함
# print(data)
# f.close()

# for문으로 읽기
# f=open("Python_Study/새파일.txt", 'r', encoding="utf-8")
# for line in f:
#     print(line)
# f. close()

# with문
# open - cloese를 자동으로 해준다
# with open("Python_Study/새파일.txt", 'a', encoding="utf-8") as f:
#     f.write("end of file")
#     f.write("2")
#     f.write("3")
#     f.write("4") # close 생략 가능(이미 기능에 부여되어짐)
# f.write("5") # Error 블럭 밖으로 나감

# csv(comma seperated values)
# ,로 구분되는 값들을 모아놓은 파일
# 이름, 입실시간, 퇴실시간
# 김정은, 09:10, 18:10
# 황덕우, 09:20, 18:10
# 용량이 적고 범용성이 좋음
# with open("Python_Study/data.csv", "w", encoding="utf-8") as f:
#     f.write("날짜,날씨,기온\n")
#     f.write("20230424,맑음,10\n")
#     f.write("20230425,비,9\n")
# with open("Python_Study/data.csv", "r", encoding="utf-8") as f:
#     data=f.readlines()
#     print(data)

# 계산 결과 저장 함수
# 정수 2개를 입력받고
# 두 수를 더한 결과를
# add_result.txt 파일에
# 저장하는 함수를 정의하세요.
# 함수 이름: add_write

# def add_write(a,b):
#     result=a+b
#     with open("Python_Study/0425/add_result.txt", "w", encoding="utf-8") as f: # 상대경로 파일 현재 위치에 생김
#         f.write(str(result))
# add_write(1,2)

# 텍스트 파일에 적힌 정수 2개를
# 읽어와서 더하는 함수를 정의하세요
# 텍스트 파일 이름 : add_number.txt
# 경로 : Python_Study/add_number.txt
# 정수 2개를 더한 결과를 print 하세요
# 함수 이름 : read_add_print

def read_add_print():
    with open("Python_Study/add_number.txt","w",encoding="utf-8") as f:
        data=f.read()
        a=int(data[0])
        b=int(data[2])
        print(a+b)
read_add_print()
