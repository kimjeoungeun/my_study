li_1=["Hello", "world", "Python"]
# li_1의 원소를 사용하여
# Hello world Python 이라고 출력하세요.


print(li_1[0] +" "+ li_1[1] + " " + li_1[2])
#
# 정답
print(li_1[0], li_1[1], li_1[2])

# join(리스트)
# 리스트의 문자열을 합친다.
print(" ".join(li_1))

# li_1의 원소를 사용하여
# Help를 출력하세요.

li_1.append("Help")
print(li_1[3])
# 정답
print(li_1[0][0:3]+li_1[2][0])

li_2=[1,2,3]
# li_1과 li_2를 사용하여
# ["Hello", "world", "Python", 1, 2, 3]
# 를 출력하세요
li_1.remove("Help")
print(li_1+li_2)
# 정답
li_1.extend(li_2) # extend를 사용하면 li_1가 바뀜
print(li_1)

# li_1과 li_2를 사용하여
# ["Hello", 1, "World", 2, "Python", 3]
# 를 출력하세요.
print(li_1[0], li_2[0], li_1[1], li_2[1], li_1[2], li_2[2])
# 정답
li_1.insert(1, li_2[0]) # ★★★★★★★★★★★★★★★★다시 풀어야할 것
li_1.insert(3, li_2[1])
li_1.insert(5, li_2[2])
print(li_1)

li_1=["Hello", "world", "Python"]
li_1.insert(1, li_2[0])
li_1.insert(3, li_2[1])
li_1.append(li_2[2])
print(li_1)


# scores=[] # scores = list() 같이 비어있는 리스트 생성
# scores.append(int(input("영어 점수:"))) # input은 문자형으로 호출되므로 int를 써서 숫자형으로 바꿔줌
# scores.append(int(input("국어 점수:")))
# scores.append(int(input("수학 점수:")))

# avg = (scores[0] + scores[1] + scores[2]) / 3

# # sum()
# # 리스트의 요소를 모두 더한다(숫자끼리만 된다)
# # 글자 넣으면 Error
# avg = sum(scores) / 3

# if avg>=91:
#     print("A")
# elif avg>=81:
#      print("B")
# elif avg>=71:
#      print("C")
# elif avg>=61:
#      print("D")
# else :
#     print("F")

# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건을 몇 개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 500원이다.

age=[]
age.append(input("나이:"))
money=[]
money.append(int(input("돈:")))
item = 500

print(money[0] // item)
print(money[0] % item)

# 다른 방법
# age=input("나이:")
# money=int(input("돈:"))
# prices=500
# print(money // prices)
# print(money % prices)


# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건별로 각각 몇 개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 1번 물건 1000원이다.
# 2번 물건 50원, 3번 물건 120원이다.

age_2=[]
age_2.append(input("나이:"))
money_2=[]
money_2.append(int(input("돈:")))
item_2=[1000, 50, 120]

print((money_2[0] // item_2[0]), (money_2[0] % item_2[0]))
print((money_2[0] // item_2[1]), (money_2[0] % item_2[1]))
print((money_2[0] // item_2[2]), (money_2[0] % item_2[2]))

# 다른방법
# age=input("나이:")
# money=int(input("돈:"))
# prices=[1000,50,120]
# print((money // prices[0]), (money % prices[0]))
# print((money // prices[1]), (money % prices[1]))
# print((money // prices[2]), (money % prices[2]))