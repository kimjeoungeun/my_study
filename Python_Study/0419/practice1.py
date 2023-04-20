# """
# eng 변수, kor 변수, math 변수를 만들고
# 각 변수는 과목의 시험 점수이다.
# 영어 점수는 80점
# 국어 점수는 60점
# 수학 점수는 50점
# 3과목 점수의 평균을 내고
# 평균 점수에 따라 성적을 출력한다.
# A : 91 ~ 100
# B : 81 ~ 90
# C : 71 ~ 80
# D : 61 ~ 70
# F : 60 이하"""

eng = input("영어 점수:")
eng = int(eng) # 파이썬만 가능
kor = int(input("국어 점수:"))
math = int(input("수학 점수:"))

# if 100 >= (eng+kor+math)/3 >= 91 : 
#     print("A")
# elif 90 >= (eng+kor+math)/3 >= 81 :
#     print("B")
# elif 80 >= (eng+kor+math)/3 >= 71 :
#     print("C")
# elif 70 >= (eng+kor+math)/3 >= 61 :
#     print("D")
# elif (eng+kor+math)/3 <= 60 : 
#     print("F")

avg=(eng+kor+math)/3
if avg>=91:
    print("A")
elif avg>=81:
     print("B")
elif avg>=71:
     print("C")
elif avg>=61:
     print("D")
else :
    print("F")

# input() 함수
# 문자열 타입
# 사용자로부터 정보를 입력받는 함수(터미널에서 입력가능)
# 데이터를 프로그램 외부로부터 받아올 수 있다.
# 사용자가 엔터를 누를때까지 입력받음
# user_input=input()
# print(user_input)

# 정수형 변환 함수
# 정수형, integer형, int형
# int(값)