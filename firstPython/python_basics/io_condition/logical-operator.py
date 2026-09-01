# logical-operator
# * A and B : 두 개 모두의 조건절이 참이어야 true를 리턴
# * X or Y :  X 나 Y가 둘 중에 하나라도 true면 true를 리턴
# * not E : E의 값이 참이면 거짓으로, 거짓이면 참으로

value = 10

# ? isinstance(값, 타입) -> 값이 그 타입이면 True, 아니면 False 반환

if isinstance(value, int) and value > 5:
    print("Correct")
else:
    print("Not Correct")

if not isinstance(value, float):
    print(f"{value} is not float")
