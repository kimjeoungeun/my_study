# 거꾸로 배열해도 같은 단어 또는 문장이 되는
# 회문(palindrome)인지 판별하는 함수를 정의하세요.
# 함수에 문자열을 입력받고 회문이면 True
# 아니면 False를 반환하도록 정의하세요
# 함수 이름 : is_palindrome
# 반환값 : True 또는 False

# 1
# def is_palindrome(input_string):
#     input_string=input_string.replace(" ","") # 문자열 공백 제거
#     length=len(input_string) # 길이
#     for i in range(length//2): # range는 정수형, 반만 검사해도 뒤집은 글자 확인 가능
#         length-1
#         if input_string[i]!= input_string[length-1-i]:
#             return False
#     return True
# 2
# def is_palindrome(input_string):
#     input_string=input_string.replace(" ","")
#     return input_string==input_string[::-1]

# result=is_palindrome("다시 합창합시다")
# print(result)

li1=[1,2,3,4,5]
# li1.reverse() # 문자열, immutalbe
# print(li1)
se1=reversed(li1) # 원본이 바뀌지는 않음
print(se1)

# string1="안녕하세요"
# string2=reversed(string1)
# for i in string1:
#     print(i)

# string3="".join(string2)
# print(string3)


# 소프트웨어 익스퍼트 아카데미
# 프로그래머스
# 백준

