# 다음 함수를 정의하세요.
# 정수 n을 입력받고, n보다 
# 작은 수 중 3의 배수와 5의 배수를
# 모두 더한 합을 반환하는 함수
# 함수이름 : sum_3_5

# def sum_3_5(n):
#     result=0 # 
#     for i in range(n): # n-1이므로 n보다 작은 범위 내 i값 
#         if i%3==0 or i%5==0: # 만약 i가 3의배수나 5의 배수라면
#             result += i # 
#     return result
# print(sum_3_5(7))

# def sum_3_5(n):
#     result=0
#     for i in range(n):
#         if i%3==0:
#             result += i
#         elif i%5==0:
#             result += i
#     return result
# print(sum_3_5(7))

# 정육면체 주사위 2개가 있다.
# 2개의 주사위를 던졌을 때
# 나올 수 있는 주사위 눈의 조합을
# 모두 print하는 함수를 정의하세요.
# 함수이름 : draw_dice
# 출력 예시 :
# 1,2
# 6,3
# 입력도 없고 출력도 없는 프린트
# def double_dice():
#     for i in range(1,7): # 1~6
#         for j in range(1,7): # 1~6
#             print(i,j)

# def double_dice():
#     i=1
#     while i<7:
#         j=1
#         while j<7:
#             print(i,j)
#             j += 1
#         i += 1

# 두 수의 차이를 구하는 함수
# 함수에 입력된 두 정수의 차이를 # 차이는 양수
# 계산하고 반환하는 함수를 정의하세요.
# 함수이름 : get_diff
# 파라미터 : a,b
# 반환값 : result
# def get_diff(a,b):
#     result=abs(a-b)
#     return result

# def get_diff(a,b):
#     if a>b:
#         result=a-b
#     else:
#         result=b-a
#     return result
# print(get_diff(1,6))


# 가장 큰 수를 만드는 함수
# 함수에 입력된 5개 정수(0~9)를  # 정렬의 문제(높은 자리에 큰 수가 오게)
# 사용하여 만들 수 있는 가장 큰
# 수를 반환하는 함수를 정의하세요.
# 함수이름 : get_biggest

# def get_biggest(a,b,c,d,e):
#     numbers=[a,b,c,d,e] # 리스트로 만듬
#     numbers.sort() # 작은 수부터 큰 수(오름차순) : 맨앞에오는게 1의자리, 맨뒤에오는게 10000의자리
#     result=0
#     for i in range(len(numbers)) : # i는 0~4까지 코드 한번씩 수행
#         result += numbers[i]*(10**i) # i가 0이면 1번 인덱스 * 10**0=1(1의자리), # i가 1이면 2번 인덱스 * 10**1=10(10의자리)
#     return result

# def get_biggest(a,b,c,d,e):
#     numbers=[a,b,c,d,e]
#     numbers.sort(reverse=True) # 내림차순
#     result="" # 빈문자열에 연결
#     for i in numbers: # 
#         result += str(i) # numbers 리스트의 숫자들을 문자형으로 변환하여 i를 정렬
#     return int(result) # 다시 숫자형

# print(get_biggest(1,2,9,1,9))

# 별찍기 2
# 정수를 함수에 입력하여
# 호출하면 해당 정수 줄의
# 별을 화면에 출력한다.
# 함수이름 : print_stars2
# """
# 출력결과
# n->1
# *
# n->4
#    *
#   **
#  ***
# ****
# """

# def print_stars2(n):
#     for i in range(1, n+1): # 1부터 n까지 범위
#         print(" "*(n-i)+"*"*i) # i에 n까지 들어감 리턴 생략 후 연결
# print_stars2(4)



