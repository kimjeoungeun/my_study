idx=0
money=int(input("돈을 입력하세요:"))
prices=[500,700,930]

while idx <= len(prices):
    price=prices[idx]
    print("개수:", money//price)
    print("잔돈:", money%price)
    idx -= 1
