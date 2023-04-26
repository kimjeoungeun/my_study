# my_calculator 모듈의 MyCalculator 클래스를 
# 상속받아서 MaxLimitCalculator 클래스를 정의하세요.
# add, sub, mul, div 메소드를 사용하여 더하기, 빼기, 곱하기 나누기를 할 수 있다.
# 0으로 나눴을때 에러가 발생하지 않도록 처리한다.
# 입력되는 정수가 1개라도 100보다 크면 계산하지 않고 100 이하의 값을 입력하도록 안내메시지를 출력한다.
# 계산결과가 100이상이면 계산하지 않고 100이하의 결과가 나오는 값만 입력하도록 안내 메시지를 출력한다.
from my_calculator import MyCalculator
class MaxLimitCalculator(MyCalculator):
    def add(self,n1,n2):
        self.n1=n1
        self.n2=n2
        if n1>100 or n2>100:
            print("100이하의 값을 입력하세요")
        elif n1+n2>100:
            print("100이하의 결과값을 입력하세요")
        else:
            print(f"{n1}+{n2}={n1+n2}")
    def sub(self,n1,n2):
        self.n1=n1
        self.n2=n2
        if n1>100 or n2>100:
            print("100이하의 값을 입력하세요")
        elif n1-n2>100:
            print("100이하의 결과값을 입력하세요")
        else:
            print(f"{n1}-{n2}={n1-n2}")
    def mul(self,n1,n2):
        self.n1=n1
        self.n2=n2
        if n1>100 or n2>100:
            print("100이하의 값을 입력하세요")
        elif n1*n2>100:
            print("100이하의 결과값을 입력하세요")
        else:
            print(f"{n1}*{n2}={n1*n2}")        
    def div(self,n1,n2):
        self.n1=n1
        self.n2=n2
        if n1>100 or n2>100:
            print("100이하의 값을 입력하세요")
        elif n1/n2>100:
            print("100이하의 결과값을 입력하세요")
        else:
            print(f"{n1}/{n2}={n1/n2}")
    def div(self, n1, n2):
        try:
            n2==0
        except:
            ZeroDivisionError
        else:
            if n2!=0:
                print(f"{n1}/{n2}={n1/n2}")
max_limit=MaxLimitCalculator()
max_limit.div(50,0)

# https://wana.tistory.com/13