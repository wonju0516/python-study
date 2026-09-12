# Data Types
# * int, float, str, bool
# * casting, dynamic typing
# * int(3.5)

# * 변수명: 타입 = 값  -> 타입 힌트(annotation). "이 변수는 이 타입이어야 한다"는 표시일 뿐
# * 파이썬이 강제하는 게 아니라서, 다른 타입 값을 넣어도 에러는 안 남 (사람/IDE용 참고 정보)
age: int = 0
name: str = "Hello"
height: float = 6.0
is_student: bool = True
print(name)


# * def 함수(파라미터: 타입) -> 반환타입:  ->는 "이 함수가 반환할 값의 타입"을 표시하는 문법
def enter_school(is_student: bool) -> bool:
    if is_student:
        return True
    else:
        return False


# * 함수 호출할 때 괄호 "("까지만 쳐도, VS Code(Pylance)가 자동으로 파라미터 이름/타입 힌트를
enter_school(is_student)
