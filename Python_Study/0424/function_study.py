# function 함수
# 입력 -> 처리 -> 출력
# 함수는 input(입력)을 받아서
# 특정 작업(처리)을 수행하고
# output(출력)을 반환한다

# 내장 함수(built-in)
# 파이썬이 기본적으로 제공해주는 함수
# print()
# len()
# zip()
# int()
# float()
# str()
# list()
# range() 

# abs(값)
# absolute의 약자
# 입력한 숫자형 데이터의 절댓값을 반환한다
# print(abs(100)) # 100
# print(abs(-100)) # 100
# print(abs(3.15)) # 3.15
# print(abs(-3.15)) # 3.15
# 부호 빼고 나머지 값을 반환

# sum(리스트)
# 리스트 안의 숫자를 더한 값을 반환한다
# print(sum([1,2,3,4,5])) # 15

# max(리스트)
# 리스트 안에서 최댓값을 찾아 반환한다
# print(max([1,2,3,4,5])) # 5

# min(리스트)
# 리스트 안에서 최솟값을 찾아 반환한다
# print(min([1,2,3,4,5])) # 1

# chr(정수)
# 정수 1개를 입력받고 해당하는
# 유니코드 문자를 반환한다
# print(chr(65)) # A

# ord("문자")
# 문자 1개를 입력받고 해당하는
# 정수를 반환한다
# print(ord("A")) # 65

# round(값)
# round(값, 소수 자릿수) # 소수자릿수 파라미터 기본값
# 반올림 함수
# print(round(1.234)) # 1(소수 첫째자리에서 반올림)
# print(round(1.234, 2)) # 1.23 (소수 셋째자리에서 반올림)
# print(round(1.369,1)) # 1.4(소수 둘째자리에서 반올림)

# 함수 정의(define)
# 함수 이름
# 합수 입력값 parameter
# 함수 결괏값 return value
"""
def 함수이름(함수입력값):
    함수 기능코드
    return 함수 결괏값
"""
# def는 함수를 정의하는 명령어
# 함수 이름도 변수 이름처럼
# 규칙을 지켜서 지어야한다.
# 영어, 숫자, _만 사용
# 숫자로 시작하면 안됨
# 띄어쓰기 하면 안됨
# 키워드 사용하면 안됨
# 기존에 이미 정의된 함수 이름도
# 피하는 것이 좋음

# def print_names(): # 이름지음
#     print("손흥민") 
#     print("황희찬")
#     print("김민재")
#     print("이강인")
# print_names() # 호출

# def get_name(): # 이름 지음
#     return "김정은" # 출력값이 있는 함수
# def print_my_name(): # 내 이름을 출력하는 함수
#     print(get_name()) # 실행하면 내 이름이 출력
# print_my_name() # 호출

# return이 있어도 되고 없어도 되는데 차이가 있다.
# a=print_names() # 정의 함수 안에 return 키워드가 없음 
# b=get_name() # 정의 함수 안에 return 키워드가 있음
# print(a) # None (수행 후 종료)
# print(b) # 김정은 (수행 후 결과 반환 후 종료)

# parameter
# 함수에 입력하는 값 
# 매개변수, argument 혼용

# def add(a,b): # (a,b)는 매개변수
#     return a+b
# def print_add(a,b):
#     print(a+b)

# result=add(1,2) # 1+2 하고 반환함
# print(result) # 3

# print_add(1,2) # 3 print(a+b) 함수가 호출만 하고 종료
# result1=print_add(1,2) # 3 print(a+b) 함수가 호출되어 일단 3이 출력되고 result1은 return이 없어 None
# print(result1) # None return값이 없어 종료

# print_add("안녕", 1) # Error str+int는 안됨(같은 타입끼리만 가능)
# print_add(1,2) # 3
# print_add("안녕", "하세요") # 안녕하세요
# print_add("하세요", "안녕") # 하세요안녕 순서대로 입력되므로 체크
# print_add(b="하세요",a="안녕") # 안녕하세요 변수에 맞게 들어감

# def swap_number(a,b):
#     temp=a
#     a=b
#     b=temp
#     print(a,b)
#     return a,b 

# a=1
# b=2
# print("함수 호출 전", a,b) # 1,2 유지 함수 안쪽의 지역변수(매개변수) a,b 와 함수 바깥의 전역변수 a=1, b=2는 이름만 같고 서로 다른 변수
# a,b=swap_number(a,b) # 2 1 호출
# swap_number(a,b) # 1 2 호출(def에 return이 없을때)
# print("함수 호출 후", 1,2) # 1,2 유지 함수 안쪽의 지역변수(매개변수) a,b 와 함수 바깥의 전역변수 a=1, b=2는 이름만 같고 서로 다른 변수
# 이름이 같더라도 서로 다른 변수

# 함수를 정의하세요.
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱

# def mul(n1,n2):
#     return n1 * n2

# print(mul(1,2)) # 2

# result = mul(1,2) # 변수에 담은 다음 출력가능 (리턴값이 존재해서)
# print(result) # 2

# a=1
# b=2
# c=3
# a,b,c=1,2,3
# d,e,f=[4,5,6]
# g,h,i=(7,8,9)

# 기본 값 매개변수 ★중요★
# default value parameter
# 함수 호출 시 n2에 입력된 값이 없으면 기본 값 사용
# def mul (n1, n2=2): 
#     return n1*n2
# print(mul(1,4)) # 4 n2값이 존재해 기본값 사용X
# print(mul(5)) # 10 n2값이 없어 기본값 사용

# 기본값으로 list를 사용 할 수 없다
# def test_func(x, test=[]): # Error (기본값으로 리스트 사용금지)
#     test.append(x)
#     print(x, test)
# test_func(1) # 1 [1] 출력
# test_func(2) # 2 [1, 2]
# test_func(5) # 5 [1, 2, 5] 값이 계속 누적

# 리스트를 기본값으로 쓰고싶을 때
# def test_func2(x, test=None):
#     if test == None:
#         test=[]
#     test.append(x)
#     print(x, test)

# def test_func1(x, test=5):
#     test=test
#     print(x,test)

# test_func1(1) # 1 5 기본값이 출력
# test_func1(2) # 2 5

# 기본값 규칙
# 기본값이 설정되는 매개변수들은 무조건 기본값이 없는 매개변수보다 뒤에 위치해야함.
# def sub(n1, n2=0, n3): # Error
#     print(n1-n2-n3)

# def sub(n1, n3, n2=0): # 기본값이 설정되는 매개변수들은 무조건 기본값이 없는 매개변수보다 뒤에 위치해야함. 
#     print(n1-n2-n3)

# 1~10까지 더한다
# *를 붙여서 사용
# *args 매개변수 (관용적표현)
# 입력값이 몇 개가 될지 모를때 (안정해졌을때)
# def add_many(*args):
#     # 튜플처럼 사용
#     # 인덱싱, 슬라이싱 가능
#     # for문 등 사용 가능
#     result = 0
#     for i in args:
#         result += i
#     return result

# result1=add_many(1,2,3,4,5)
# print(result1)
# result2=add_many(3,2,5,9,1)
# print(result2)
# result3=add_many(1,2)
# print(result3)

# *args 매개변수가 유동적일때 사용
# def calc_many(n1, *args): # (*args, n1)도 가능, 일반매개변수와 사용 가능
#     result = n1
#     for i in args:
#         result += i
#     return n1

# 키워드 매개변수
# **를 붙여서 사용
# **kwargs (관용적 표현)
# keyword arguments
# 딕셔너리로 사용
# def print_kwargs(**kwargs): # 매개변수를 지정해두지않음
#     print_kwargs(n1, *args, **kwargs) ??
#     print(kwargs)

# print_kwargs(a=1, b=2) # {'a':1, 'b':2}
# print_kwargs(name="이름", age=10) # {'name':'이름', 'age':10}
# 들어오는 값들이 유동적일 때 주로 사용

# 함수의 반환
# return 반환값
# return을 만나면 반환값을 반환함과 동시에 함수가 종료
# def test_func4():
#     print(1)
#     print(2)
#     return None # None을 반환하면서 밑의 값 실행 안됨
#     print(3)
#     print(4)
#     print(5)
# 함수의 반환값은 무조건 1개이다.
# def test_func5(a,b):
     # return(a+b, a*b) 튜플로 묶어서 리턴하라는것과 같음
#     return a+b, a*b # 묶어서 한줄에 리턴해야함

# result=test_func5(1,2)
# print(result) # 통변수에 받은것

# result_add, result_mul=test_func5(1,2)
# result_add, result_mul=(a+b, a*b)와 같음
# print(result_add, result_mul)  # 하나씩 까서 받은 것

# https://legitcode267.tistory.com/13 *args **kwargs

# https://plan2018.tistory.com/203 매개변수

# 홀수 판별 함수
# 정수 1개를 입력받고 홀수인지
# 판별하는 함수
# 함수이름 : is_odd_number
# 파라미터:n
# 반환값 :  홀수면 True
#           짝수면 False

# def is_odd_number(n):
#     if n%2==1:
#         print("True")
#     else:
#         print("False")
#     return 
# is_odd_number(4)

# 1.
# def is_odd_number(n): # 함수정의
#     if n%2==1: # 안쪽에서 정의된 코드 나머지 1 실행
#         return True # if문 체크
#     else:
#         return False
# is_odd_number(5) # 호출
# 2.
# def is_odd_number(n):# 함수 정의
#     if n%2==1: # 홀수는 안쪽  return True
#         return True # 홀수 : 함수 종료
#     return False # 짝수는 if문 밖으로 감
# is_odd_number(4)
# 3.
# def is_odd_number(n):
#     return n%2==1 # 연산 결과가 return, 조건 통채로 리턴
# print(is_odd_number(4))

# 테두리를 출력하는 함수 # 출력: 문자 출력
# 문자열을 입력받고 print 함수를
# 이용해 테두리와 함께 문자를 출력한다
# 함수이름 : get_bordered_str
# 파라미터 : message
# 반환값 : None # 반환값 : 함수가 리턴하는 값
# print만 하면 동작을 출력하므로 리턴값으로 받아올게 없다
# 프린트 예시
"""
*****
Hello
*****
"""
# def get_bordered_str(message):
#     print("*"*len(message))
#     print(message)
#     print("*"*len(message))
#     return # 생략가능 함수를 여기서 끝내라는 뜻으로 더이상 출력될 결과값이 없다
# get_bordered_str("cute")

def get_bordered_str(message):
    # message=str(message) 한줄 추가도 가능
    n=len(str(message)) # len함수(문자열함수)
    print("*"*n)
    print(message)
    print("*"*n)
get_bordered_str(12345)

# https://bunnycode.tistory.com/16 ruturn 사이트

# 속도를 변환하는 함수
# m/s 단위의 속도가 입력되면
# km/h 단위의 속도로 변환한다
# 함수 이름  :  covert_velocity
# 파라미터 : velocity
# 반환값 : km/h로 변환된 속도
# 1초에 1m -> 1m/s
# 1m/s로 1시간동안 가면 몇m?
# 1m/s*3600(1시간)
# 3600m/h
# 1km는 몇 m? 1000m
# 3600m/h는 몇 km/h?
# 3600m/h / 1000(1km)
# 초속 1m/s ==> 시속 3.6km/h
# 초속*3.6=시속
# def covert_velocity(velocity):
#     result=velocity*(3600/1000) # 1m/s * 3600 / 1000
#     return print(result)
# covert_velocity(50)

# def covert_velocity(velocity):
#     result=velocity*3.6 # 1m/s * 3600 / 1000
#     return result
# velocity=covert_velocity(50)
# print(velocity)
# return과 print는 다름
# (차이 검색할 것)

# 별찍기 함수
# 정수를 함수에 입력하여
# 호출하면 해당 정수줄의
# 별을 화면에 출력한다.
# 함수이름 : print_stars
# 파라미터 : n
# 반환값 : None
# 출력결과 n->4
"""
*
**
***
****
"""

def print_stars(n):
    n=n+1
    for i in range(n):
        print("*"*i)
print_stars(4)

def print_stars(n): 
    for i in range(n): # 0부터 n-1만큼 반복
        for j in range(i+1): # j에 0부터 i까지
            print("*", end="") # end:출력하고 줄바꿈
        print() # end 기본값 줄바꿈 출력
print_stars(4)

def print_stars(n): 
    i=0
    while i <n:
        j=0
        while j<i+1:
            print("*", end="")
            j += 1
        print()
        i += 1
print_stars(4)
