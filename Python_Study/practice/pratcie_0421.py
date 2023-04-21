idx=0
money=int(input("돈을 입력하세요:"))
prices=[500,700,930]

while idx <= len(prices):
    price=prices[idx]
    print("개수:", money//price)
    print("잔돈:", money%price)
    idx -= 1


scores=[]
n=0
while n<5:
    score=int(input("시험점수:"))
    scores.appedn(score)
    n+=1
print(scores)


n=1
while n<10:
    print("2*",n,"=",2*n)
    n+=1 # n이 1일때부터 1씩 더하는 것을 반복

while True: 
  print("hi")