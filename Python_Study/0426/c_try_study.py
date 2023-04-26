# 예외처리(오류처리)
# 오류 발생을 찾아내서 처리하는 것
# li=[1,2,3,4,5]
# li[100]
# 100/0
# f=open("없는파일",'r')
# 에러발생시 프로그램을 중단하고
# 에러 메세지를 보여준다.

# 예외 처리구문
# try~except
# try 블록에는 오류가 발생할 수 있는 코드
# except 블록에는 오류가 발생했을 때 수행할 코드
# 오류가 발생하지 않으면 except 블록의 코드는 실행되지 않는다.
# try:
#     100/0
# except :
#     print("에러발생")

# print("에러 발생 후")

# try:
#     100/0
# except Exception as e: # Exception(모든 에러 메세지)에러 메세지를 보여줌
#     print(e)

# print("에러 발생 후")

try:
    [1,2,3,4,5][100] # 여러종류의 에러를 명시하거나, Exception을 써야함
except ZeroDivisionError as e: # Exception의 한 종류 (에러 객체가 달라짐)
    print(e, "0으로 나눌 수 없습니다.")
except IndexError as e:
    print(e, "인덱싱할 수 없습니다.")
print("에러 발생 후")