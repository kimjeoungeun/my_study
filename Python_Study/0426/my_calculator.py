# MyCalculator 클래스로 만들어보세요.
# add, sub, mul, div 메소드
class MyCalculator:
    def __init__(self):
        pass
    def add(self,n1,n2):
        print(f"{n1}+{n2}={n1+n2}")
    def sub(self,n1,n2):
        print(f"{n1}-{n2}={n1-n2}")
    def mul(self,n1,n2):
        print(f"{n1}*{n2}={n1*n2}")
    def div(self,n1,n2):
        print(f"{n1}/{n2}={n1/n2}")

if __name__=="__main__":
    my_calculator=MyCalculator()

    while True:
        print("""
        계산기
        ----------
        1: +(더하기)
        2: -(빼기)
        3. *(곱하기)
        4. /(나누기)
        q. 종료
        """)
        operater=input("계산을 선택하세요:")
        if operater=='q':
            print("종료합니다.")
            break
        n1=int(input("정수1:"))
        n2=int(input("정수2:"))
        if operater=='1':
            my_calculator.add(n1,n2)
        elif operater=='2':
            my_calculator.sub(n1,n2)
        elif operater=='3':
            my_calculator.mul(n1,n2)
        elif operater=='4':
            my_calculator.div(n1,n2)
        else:
            print("잘못입력했습니다.")