# 객체지향(oop, object orientd programming)
# 객체와 객체 사이의 상호작용으로 
# 프로그램을 구성하는 프로그래밍 패러다임
# 프로그램 구현에 필요한 객체를 파악하고
# 각각의 객체들의 역할이 무엇인지를 정의하여
# 객체들간의 상호작용을 통해 프로그램을 만드는 것

# 객체지향의 특징(추상화,캡슐화 꼭 알아두기)
# 추상화 : 공통된 속성이나 기능 도출
# 캡슐화 : 데이터의 구조와 연산을 결합
# 상속 : 상위 개념의 특징이 하위 개념에 전달(파생)
# 다형성 : 유사 객체의 사용성을 그대로 유지

# https://jeong-pro.tistory.com/95

# 객체는 추상화와 캡슐화의 결과 ex. 붕어빵
# 객체는 데이터 필드와 메소드를 가진다.

# 클래스는 객체를 정의한 것(객체의 설계도) ex.붕어빵틀
# 객체를 만들기 위한 메타정보
# 데이터필드(멤버 변수, 개체 속성)
# 객체가 가지고 있는 변수
# 메소드(멤버 함수)
# 객체가 가지고 있는 함수
"""
class 클래스이름:
    클래스 멤버 변수
    메소드
"""
# 클래스 이름도 변수 이름 규칙 적용
# 클래스 이름 컨벤션(관용)
# 첫 글자 대문자
# 언더바(_) 안쓰기
# 단어 구분될 때 대문자
# class Car: # Car라고 하는 클래스 안에서만 사용 가능
#     def move(self): # 함수정의
#         print("move") # 메소드:클래스 안에 정의된 함수

# class SportsCar: 
    # pass
# self는 바로 그 클래스의 객체를 가리킴
# 메소드 정의할 때 항상 사용

# 인스턴스
# 객체 중에서 클래스를 통해 생성된 객체
# my_car=Car() # car class의 설계대로 객체가 만들어져 my_car라는 변수에 할당됨
# my_car.move()
# .(점) ---> 객체 멤버 접근 연산자
# 리스트도 객체라 . 사용
# li=[1,2,3,4,5]
# li.append(6)
# 파이썬에서는 모든게 객체다(순수객체지향)
# 객체는 설계도 클래스로부터 나온다
# 내장함수 type()
# 데이터의 자료형을 반환한다
# print(type(li)) # 클래스로 만들어진 객체

# n=10
# print(type(n)) # 정수도 클래스로 만들어진 객체
# print(type("Hello")) # 문자열도 클래스로 만들어진 객체

# str(문자열) 메소드
# upper()
# 모두 대문자로 변경
# s="Hello"
# print(s.upper())
# lower()
# 모두 소문자로 변경
# print(s.lower())
# strip()
# 문자열 양쪽 끝의 특정 문자를 제거(보통 공백 지울때 사용)
# s1="      Hello      "
# print(s1.strip())
# lstrip(), rstrip()
# 왼쪽, 오른쪽 끝의 특정 문자 제거
# print(s1.lstrip())
# print(s1.rstrip())
# split() -> 자주 쓰이는 함수
# 구분자로 분할하여 리스트로 반환
# s2="Hello,World,Python"
# print(s2.split(','))
# replace()
# 문자열의 특정 부분을 대체
# print(s2.replace(',',' ')) # (기존문자, 바꿀문자)
# print(s2)
# 파이썬에서 string 객체는 immutable해서 수정 불가능
# 문자열은 한번 확정되면 수정 불가능
# s1, s2는 바뀌지 않고 리턴값만 출력
# 원본을 수정해서 값을 변경한게 아닌 새로운 문자열을 만들어냄
# s2=s2.replace(',',' ') # 변수이름을 그대로 사용하고 싶으면 재할당하면 가능

# # "Hello" ---> "hello"
# s3="Hello"
# # s3[0]="h" # Error string은 수정 불가능
# s3.lower() # 적용이 안됨 리턴값 출력시에 적용가능하므로
# s4=s3.replace("H","h")

# self 매개변수(클래스 정의할때 꼭 들어감)
# 모든 메소드의 첫번째 매개변수
# 메소드의 정의에는 사용되지만 호출에는 사용되지 않음
# 객체 자신을 참조하여 클래스에 정의된 멤버에 접근할 때 사용
# class person:
#     def say(self): 
#         self.name="사람1" # self.name의 멤버 변수는 사람1
#         print("Hello")
#     def move(self):
#         pass
#     def eat(self, food): # 맨앞, 여러개의 매개변수에도 첫번째 매개변수로 self가 와야함
#         self.sleep()
#         print(f"{self.name}이 {food}을 먹었습니다.")
#     def sleep(self):
#         print(f"{self.name}이 잠을 잤습니다.")

# person1=person()
# person1.say() # 호출시 self 제외
# person1.eat("밥")

# initializer 초기자
# initialize 초기화 # 만든다, 시작한다와 유사한 의미
# 인스턴스가 생성될때 initialize 가 시작된다
# class Person:
#     def __init__(self, name, age, gender, phone): # 지역변수를 외부로 내보내려면 
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.phone=phone
#         print("initialize") # 출력되는 시점에 person 객체가 초기화

#     def say_name(self):
#         print(self.name)

#     def introduce(self):
#         print(f"안녕하세요. 저는 {self.name}입니다.")
#         print(f"나이는 {self.age}살이고, 성별은 {self.gender}입니다.")
#         print(self.name, self.age, self.gender)

# print("before")
# person2=Person("이름",20,"남자","010-1234-5678") # person클래스에 객체가 만들어질떄 initialize가 이루어짐
# print("after")
# person2.say_name()
# 초기값을 입력받을 때 사용

# person 클래스에 introduce 메소드를 추가
# 이름 나이 성별을 print 하는 메소드
# person2.introduce()

# 상속 inheritance
# 클래스(상위클래스)
# class Animal:
#     def __init__(self, name): # name값을 입력받음 특수한 메소드
#         self.name=name # 멤버변수로 저장,할당(self.name이랑 name은 서로 다른 객체이나 값이 똑같음)
#         print(f"{self.name}이 생성되었습니다.")
#     def say(self): 
#         print("")

# class Dog(Animal): # (상위클래스 입력)
#     def say(self):
#         # 매소드 재정의
#         # method overriding(메소드 덮어쓰기)
#         print("멍멍")

# my_dog=Dog("백구") # 상속받아 Animal 객체에서 입력됨
# my_dog.say() # Animal클래스가 아닌 새로 정의한 Dog클래스에서 출력

# class Cat(Animal):
#     def say(self):
#         print("야옹")

# my_cat=Cat("나비")
# my_cat.say()

class Student:
    def __init__(self, name, age, school, grade): # 클래스 정의시 self가 꼭 들어가야한다
        self.name=name
        self.age=age
        self.school=school
        self.grade=grade
    def introduce(self):
        print(f"이름:{self.name}, 나이:{self.age}살, 학교:{self.school}학교, 학년:{self.grade}학년")

stu1=Student("홍길동", 20, "서울대", 1)
stu2=Student("손흥민", 21, "서울대", 2)
stu3=Student("류현진", 22, "서울대", 3)
stu_list=[stu1, stu2, stu3]
for stu in stu_list:
    stu.introduce() # stu객체에 메소드를 쓴다

