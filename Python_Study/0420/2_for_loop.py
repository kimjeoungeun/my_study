# for문
"""
for 변수 in iterable값: # iterable 한개씩 꺼내서 변수에 대입하면서 반복
    반복할 코드
"""
# 반복횟수가 정해져있을 때 사용하면 효율적 (while문은 조건 식을 체크하면서 반복)
# li_1=["one", "two", "three"]
# for i in li_1:
#     print(i)
# 첫번째 요소부터 마지막 요소까지 변수에 대입하면서 반복

# s1="hello"
# for i in s1:
#     print(i)

# 무한반복문은 while만 가능

number=[1,2,3,4,5,6,7,8,9,10] # 리스트타입

for i in number:
    print(i)

number.reverse()
for i in number:
    print(i)

# range()
# 숫자(정수) range 객체를 만들어주는 함수
# range(끝 정수)
# 0~ 끝정수 -1
# range(시작, 끝)
# 시작~끝 -1
# range(시작, 끝, 스텝)
# 시작~끝-1 까지인데 스텝(증감)만큼 차이나게 해줌
# 시작 정수부터 끝 정수까지 iterable한 값을 줌

# for i in range(10): # 0~9까지
#     print(i)

# for i in range(1,11): # 1~10 사이
#     print(i)

# for i in range(1, 21, 3):
#     print(i)

# for문을 사용하여 2부터 30까지 출력해보세요.
# for i in range(1,31):
#     print(i)
# for문을 사용하여 2부터 30까지 숫자 중 짝수만 출력해보세요.
# for i in range(2, 31, 2):
#     print(i)

# for i in range(2, 31):
#     if i%2==0: #짝수
#         print(i)

# for i in range(2, 31):
#     if 1%2==1:
#         #continue
#         pass # 아무것도안하고 그냥 넘어갈 때
#     else:
#         print(i)
    # print("반복") # pass는 출력되고 continue는 출력되지않음

# pass
# 아무런 동작도 하지않고 넘어갈때 사용
# if 1 == 1:
#     pass
# print("완료")

# for i in range(5):
#     pass
# print("완료")


# for문을 사용하여 10부터 1까지 출력해보세요.
# for i in range(10, 0, -1):
#     print(i)
# for i in reversed(range(1, 11)):
#     print(i)
# for i in range(1, 11)[::-1]: #슬라이싱 [시작인덱스:끝인덱스:방향]
#     print(i)

# reversed
# 뒤집는 함수(내장함수)

# money=2000
# price=1000
# coffee=5
# for i in range(coffee): # 반복을 원하는 횟수(0~4)
#     print("커피를 구매했습니다.")
#     money-=price
#     print("남은커피:", coffee -1 -i) # 4~0
#     if money <price : # 0 이하로 떨어졌을 때 탈출(안쓰면 0원 밑으로 내려가도 계속 반복)
#         break
# 반복하면 i값이 바뀐다.

# for i in range(1, coffee+1):
#     print("남은커피:", coffee-i) #4~0

# for i in range(coffee):
#     coffee -= 1
#     print("남은커피:", coffee) # 4~0

# prices=[500,700,930]
# money=int(input("돈:"))
# for i in range(len(prices)):
#     price=prices[i]
#     print(money//price)
#     print(money%price)

# for price in prices: #prices 리스트의 값을 바로 꺼내서 price에 바로 대입해 사용_for문의 특징
#     print(money//price)
#     print(money%price)

# scores=[]
# for i in range(5):
#     score=int(input("시험점수:"))
#     scores.append(score)

# for i in range(1,10):
#     print("2 *", i, "=", 2*i)
# 이중 for문

for i in range(2,10): #2~9
    print(i, "단") # i 값이 바뀔때 바뀌어야 되기 때문에 큰 루프 입력 후 위치
    for j in range(1, 10): # 안쪽 for문이 먼저 반복이 이루어짐
        print(i, "*", j, "=", i*j)
    print("------------")# i가 바뀌기 전에 들어가야함
# 큰루프, 작은루프 어느것이 먼저 반복되는지 체크할 것
