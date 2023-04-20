# dictionary 자료형
# 이름표를 찾아 값을 저장
# (key(이름표)-value(이름표에 붙는 값))
# 쉼표로 구분
# {key:value} 형태
# person={
#     "이름":"이름",
#     "나이":18,
#     "점수":{
#         "영어":80,
#         "국어":90,
#         "수학":100
#     },
#      1:"ㅎㅎ"} 
# # 여러 자료형태 사용 가능
# # 해시맵구조 : 규칙에 따라 엮어놓은 형태
# # key값으로 접근
# # 장점 : 정보를 알아보기 쉬움
# print(person["나이"]) # 인덱스 대신에 key 값으로 접근
# print(person["점수"]["영어"])
# dict_1={1:'a'}
# dict_1['b']=2 # 추가 'b':2 key-value 쌍 추가
# dict_1[1]='C' # 바꿈 1: 'C', 'b': 2
# del dict_1[1] # 삭제 'b': 2
# print(dict_1)

dict_2={1:'a', 2:'b', 3:'c'}

# # keys()
# # 딕셔너리에서 key 값만 리스트 형태로 돌려준다.
dict_keys = dict_2.keys()
print(dict_keys)
# # values()
# # 딕셔너리에서 value 값만 리스트 형태로 돌려준다.
dict_values=dict_2.values()
print(dict_values)
# # items()
# # 딕셔너리에서 key-values 쌍을 튜플로 묶은 값을 리스트 형태로 돌려준다.
dict_items=dict_2.items()
print(dict_items)
# get()
# key에 대응되는 value를 돌려준다.
# key값이 존재하지 않으면 None을 돌려준다.
# dict_2["2"] # 해당 딕셔너리에 key 값이 없으면 error가 난다.
print(dict_2.get("나이", "나이불명")) # 앞의 key값이 None 일때 뒤의 값을 출력
# None : 깡통변수
# 값이 존재하지 않는 변수에 None을 대입하여 이 변수에 아무런 값이 없다는 것을 나타낼 때 사용

# clear()
# 딕셔너리 안의 모든 요소를 삭제한다.
# remove는 키 한 개값 삭제
dict_2.clear()
print(dict_2)