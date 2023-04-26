# 문자열 포매팅(formatting)
# result=str(a)+"+"+str(b)+"="+str(a+b)
result="%d+%d=%d"%(3,2,5)
print(result)
a,b=1,2
result="%d+%d=%d"%(a,b,a+b)
print(result)

# 포맷코드
# %s 문자열 (string)
# %d 정수 (int)
# %f 실수 (float)
# %o 8진수
# %x 16진수
# %(변수가 들어갈 자리)
# %% %글자 자체


string1="hello"
int1=3
float1=1.2345
print("%s %d %f"%(string1, int1, float1))

# f-string(강력한 기능★)
# python 3.6 이후 버전부터 지원
string1="hello"
int1=3
float1=1.2345
result=f"{string1} {int1} {float1}"
print(result)

# 변수의 값 자체를 문자형으로 바꿔줄때 편하다


def add(a,b):
    result=f"{a} + {b} = {a+b}"
    print(result)
    with open("python_study/0425/calculator_result1.txt","a",encoding="utf-8") as f:
        f.write(result)
def sub(a,b):
    result=f"{a} - {b} = {a-b}"
    print(result)
    with open("python_study/0425/calculator_result1.txt","a",encoding="utf-8") as f:
        f.write(result)
def mul(a,b):
    result=f"{a} * {b} = {a*b}"
    print(result)
    with open("python_study/0425/calculator_result1.txt","a",encoding="utf-8") as f:
        f.write(result)
def div(a,b):
    result=f"{a} / {b} = {a/b}"
    print(result)
    with open("python_study/0425/calculator_result1.txt","a",encoding="utf-8") as f:
        f.write(result)

while True: # 무한반복문 종료되지않고 계속 실행
    print("""
    계산기
    1: +
    2: -
    3: *
    4: /
    q: 종료
    """)
    operator=input("원하는 계산을 입력하세요:")
    if operator=='q':
        break
    a=int(input("정수 1: ")) # input은 문자열이므로 정수형으로 변환
    b=int(input("정수 2: "))
    if operator=='1':
        add(a,b)
    elif operator=='2':
        sub(a,b)
    elif operator=='3':
        mul(a,b)
    elif operator=='4':
        div(a,b)

