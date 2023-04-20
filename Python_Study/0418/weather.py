weather = "맑음" # weather 변수에 값 할당
print("비가 오나요?", weather == "비") # 전제문장(질문, 대답) weather의 값이 비와 같다. 비교연산자를 사용한 비교연산식이므로 True나 False 값이 나옴
if weather == "비" : # weather의 값이 "비"와 같으면 조건식이 True이므로 안쪽 코드 블록 실행
    print("우산을 가져간다.")
elif weather == "맑음" : # if에서 False가 나와야 조건을 확인하려고 elif로 내려옴
    print("날씨가 좋다")
else : # if나 elif의 조건식이 모두 False이면 실행
    print("우산을 가져가지 않는다.")

print(1+1) # 1+1이라는 연산식이 수행이 되어 결과가 2가 되어 2가 출력되었음