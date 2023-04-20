# While 반복문
"""
While 조건:
    반복할 코드
"""
# 조건이 참인 경우에 코드를 계속 반복
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10) # 숫자가 커질수록 반복하기 힘듬
# n=1
# while n <= 10:
#     print(n)
#     n += 1 # n = n+1(같은 의미)
# n값을 출력하고 해당값에 +1이 10이 될때까지 체크해서 출력

# 할당연산자
# += 연산자
# 더하기 연산 후 할당
# n += 1은 n = n+1이라는 의미
# -=
# n -= 1은 n = n-1이라는 의미
# *=
# /=
# **=
# //=
# %=

# S1 = "안녕"
# S1 += "하세요" # 

# while 반복문을 활용하여
# 10부터 1까지 순서대로 출력하세요.
# n1=10
# while n1 > 0: # while n1 >= 1: 과 같음
#     print(n1)
#     n1 -= 1


# money=10000
# price=1000
# coffee=5
# while money >= price: # money-price >= 0:
#      print("커피를 구매했습니다.")
#      money-= price
#      coffee -= 1
#      print("남은 커피:", coffee)
#      if coffee==0: #커피가 0개가 되었을때
#          break # 탈출

# break 
# 반복문을 즉시 종료한다.(반복문 탈출) : 자주 쓰임

# while 반복문을 활용하여
# 1부터 10까지 홀수만 출력한다.

# a=1
# while a <= 10:
#     if a % 2 == 1: # 짝수:2의배수 홀수:나머지1
#         print(a)
#     a += 1

# continue
# 반복문의 제일 처음으로 돌아감
# b=0
# while b < 10:
#     b += 1
#     if b % 2 == 0:
#         continue
#     print(b)


# 무한반복문
# 무한 루프
# 조건식에 True를 입력해 항상 참이되도록 하여 무한히 반복하게 한다.
# while True:
#         print("hi")
# while True:
#     user_input=input("종료하려면 1을 입력해주세요.")
#     if user_input == "1":
#             break

# 무한반복문으로 계산기 만들기
# +,-,*,/ 계산
# 2개의 수를 계산 a+b

# while True:
#     print("""
#         계산기
#     ==============
#     1. 더하기(+)
#     2. 빼기(-)
#     3. 곱하기(*)
#     4. 나누기(/)
#     q. 끝내기
#     """)
    # operator = input("계산을 선택하세요:")
    # n1=input("숫자1을 입력하세요:")
    # n2=input("숫자2를 입력하세요:")
    # if operator=="1": #input(문자)이기 때문에 "1"로 문자로 맞춰줌(파이썬은 데이터타입이 같아야함)
    #     print(int(n1)+int(n2))
    # if operator=="2":
    #     print(int(n1)-int(n2))
    # if operator=="3":
    #     print(int(n1)*int(n2))
    # if operator=="4":
    #     print(int(n1)/int(n2))
    # if operator=="q":
    #     break

# while True:
#     print("""
#         계산기
#     ==============
#     1. 더하기(+)
#     2. 빼기(-)
#     3. 곱하기(*)
#     4. 나누기(/)
#     q. 끝내기
#     """)
#     operator = input("계산을 선택하세요:")
#     n1=int(input("숫자1을 입력하세요:"))
#     n2=int(input("숫자2를 입력하세요:"))
#     if operator=="1": #input(문자)이기 때문에 "1"로 문자로 맞춰줌(파이썬은 데이터타입이 같아야함)
#         print(n1, "+", n2, "=", n1+n2)
#     elif operator=="2":
#         print(n1, "-", n2, "=", n1-n2)
#     elif operator=="3":
#         print(n1, "*", n2, "=", n1*n2)
#     elif operator=="4":
#         print(n1, "/", n2, "=", n1/n2)
#     elif operator=="q":
#         break

# 사용자가 가지고 있는 돈을 입력받는다.
# 구매할 수 있는 커피의 개수와 잔돈을 출력한다.
# 구매할 수 있는 음료수의 개수와 잔돈을 출력한다.
# 구매할 수 있는 콜라의 개수와 잔돈을 출력한다.
# 커피는 500원, 음료수는 700원, 콜라는 930원
# 물품의 개수는 무한하다고 가정한다.
# while 반복문을 사용하여 작성한다.

# idx=0
# prices=[500,700,930]
# money=int(input("돈:"))

# while idx <= len(prices):
#     # while idx <= 2:
#     # while idx < 3:
#     price=prices[idx]
#     print("개수:", money//price)
#     print("잔돈:", money%price)
#     idx += 1


# while 반복문을 사용해서
# scores 리스트에 시험 점수 5개를
# 정수형으로 입력받으세요.

# scores1=[]
# n=0
# while n<5:
#     score=int(input("시험점수:"))
#     scores1.append(score)
#     n += 1
# print(scores1) # 들여쓰기 구분할것

# while 반복문을 사용하여
# 구구단 2단을 출력하세요.

n=1
while n < 10 :
    print("2*", n, "=", 2*n)
    n += 1
