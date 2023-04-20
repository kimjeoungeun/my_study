# if문 : 형태가 존재
"""
if 조건:
    실행하려는 코드
    코드2줄
    코드3줄
코드4줄

if문은 조건이 True(참)일 때 안쪽 코드 블럭을 실행
if 조건:
    조건이 True(참)일 때 실행하려는 코드
else:
    아닐때 실행하려는 코드(if와 같이 써야함)
else는 조건이 False(거짓)일 때 안쪽 코드 블럭을 실행
if 조건1:
    조건1이 True(참)일때 실행
elif 조건2:
    조건1은 False, 조건2는 Ture일때 실행
else:
    조건1 False 조건2 False일때 실행
"""
# else나 elif(조건식이 1개 더 있을때 씀)는 if조건과 같이 써야함
# 파이썬은 들여쓰기_탭(1)이나 띄어쓰기(4)로 구분_로 코드블럭을 구분한다.
# if 조건(식이나 값):
#   실행하려는 코드(조건이 참일때 실행)
#   코드2줄

# -------------------

# bool 타입변수
#     True(참), False(거짓)_예약어(첫글자 대문자)

number1 = 6 # 숫자형 변수(정수형변수), 피연산자
number2 = 6
if number1 > number2 : # 넘버1, 넘버2 피연산자, 부등호 : 연산자
    print(number1 > number2) #맞으면 True
    print("number1이 더 크다.")
elif number1 == number2 : 
    print("같다.")
else : 
    print(number1 > number2)
    print("number2가 더 크다.")

# 비교 연산자(a, b는 변수) : True or False가 나온다
# (등호(=) 하나 사용시 대입연산자,할당연산자)
# a > b     a가 b보다 크다.
# a >= b    a가 b보다 크거나 같다.
# a < b     a가 b보다 작다.
# a <= b    a가 b보다 작거나 같다.
# a == b    a와 b가 같다.
# a != b    a와 b가 같지 않다.
print(2 > 3) # False
print(2 >= 3) # False
print(2 < 3) # True
print(2 <= 3) # True
print(2 == 3) # False
print(2 != 3) # True

# 문자의 크기비교 : 사전순(알파벳순:대문자먼저)
# a가 제일 작고 z가 제일 크다
# A가 앞에 나오고 a가 나중에 나옴(a가 더 큼)
print("a" < "b") # True
print("CAT" < "DOG") # True
print("COW" > "CAT") # True
print("DOG" > "dog") # False
print("DOG" < "dog") # True 
print("DOG" == "dog") # False

# 논리 연산자(True, False에 적용)
# and    a and b 논리곱
#        a와 b 둘 다 True일때 True 아니면 False(변수 a,b는 피연산자)

# or     a or b
#        a와 b 중 하나라도 True면 True 둘다  False면 False

# not    not a(반항연산자:항(변수)이 한 개 밖에 없음)
#        Ture면 False로 False면 True로 바꾼다.

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True

# 응용
age = 16
money = 10000
if age >= 20 and money >= 10000 :
    print("성인이고 부자입니다.")
if age >= 20 or money >= 10000 :
    print("성인 또는 부자입니다.")

if "안녕" : 
    print("안녕하세요")
# 문자열에 값이 있으면 True 없으면 False
if 0 :
    print(0)
# 숫자 0은 False, 나머진 True