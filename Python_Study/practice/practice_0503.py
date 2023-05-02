# list_a = list(range(10))
# list_b = [i if i >= 5 else "under" for i in list_a]  
# print(list_b)# 조건이 2개 이상일땐 맨 앞 i 그리고 for 문이 맨 뒤 그외엔 정순

# list_b = [j for j in range(5) if j > 1 for i in range(3) if i == 2]
# print(list_b) # 2번

# list_b= []
# for i in range(3):
#     if i == 2:
#         for j in range(5) :
#             if j > 1:
#                 list_b.append(j)
# print(list_b) # 2번

list_a = list(range(10))
list_b = [i if i >= 5 else "under" for i in list_a]

list_b = [i if i > 3 else "same" if i == 2 else "under" for i in list_a ]
print(list_b) # 3번

list_a = list(range(10))
list_b = [i if i >= 5 else "under" for i in list_a]
li_b=[]
for i in range(10):
    if i>3:
        li_b.append(i)
    elif i==2:
        b="same"
        li_b.append(b)
    else:
        c="under"
        li_b.append(c)
print(li_b)