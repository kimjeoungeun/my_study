# 모듈
# 함수, 변수, 클래스 모아놓은 파이썬 파일
# 다른 파이썬 프로그램에서 불러와서 사용
# import 명령어로 불러옴
"""
import 모듈이름
"""
# import my_module 
# my_module.add(1,2) # .(점)을 쓰므로 모듈도 파이썬에서는 객체다
# my_module.sub(1,2)

"""
from 모듈이름 import 모듈함수
from 모듈이름 import 모듈함수1, 모듈함수2
from 모듈이름 import *
""" # (*=모두)
# from my_module import add,sub # 함수를 특정해서 꺼내옴
# add(1,2)
# sub(2,1)
# from my_module import * # 함수전체를 꺼내옴
# add(1,2)
# sub(2,1)

# import my_module_1

# my_module_1 파일
# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# if __name__ == "__main__": name이 main이면 실행되고, main에서 import되면 실행되지않음
#     print(add(1,2))
#     print(sub(3,4))
# else:
#    print(__name__) # 결과 : my_module_1, main에 모듈 이름만 나옴

from my_calculator import MyCalculator
my_calculator=MyCalculator()
my_calculator.div(10,0)
# 컨트롤+메소드(div)클릭하면 정의된 부분으로 이동
# 상속으로 0으로 나누지못하게 하는 법
class ZeroCalculator(MyCalculator): # 새로운 하위 클래스를 만듬
    def div(self,n1,n2): # div만 재정의
        if n2==0: # n2가 0이면 
            print("0으로 나눌 수 없습니다.") # 나눌수없다(에러남)
        else:
            print(f"{n1}/{n2}={n1/n2}") # 아니면 div 함수
zero_calculator=ZeroCalculator()
zero_calculator.div(10,0)

