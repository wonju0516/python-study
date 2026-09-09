# catching exception: try-except로 에러를 잡아서 프로그램이 죽지 않게 처리하는 방법 정리
from pathlib import Path

BASE_DIR = Path(__file__).parent


# * custom error(사용자 정의 에러): Exception을 상속받아 나만의 에러 타입을 직접 만들 수 있음
# * 왜 만드냐: "숫자가 범위를 벗어남" 같은, 파이썬 기본 에러엔 없는 상황을 내 코드 의미에 맞게 표현하려고
class GradeOutOfBoundError(Exception):
    def __init__(self, grade, message):
        print(grade)
        print(message)
        # do something here


try:
    grade = int(input("Type your score from 0 to 100: "))
    if grade < 0 or grade > 100:
        # * raise: 조건에 맞으면 강제로 에러를 발생시킴. 여기선 방금 만든 커스텀 에러를 던짐
        raise GradeOutOfBoundError(
            grade=grade, message="Grade should be between 0 to 100"
        )

# * except 아래에 에러 타입을 적으면, 그 타입의 에러가 발생했을 때 기본 에러 화면(트레이스백) 대신
# * 여기 적힌 코드가 대신 실행됨 (지금은 pass라서 아무것도 안 하고 조용히 넘어감)
except GradeOutOfBoundError:
    pass


# * FileNotFound: 파일이 없을 때 나는 에러
# with open(BASE_DIR / "sample1.txt") as f:
#     f.read()

try:
    with open(BASE_DIR / "sample1.txt") as f:
        f.read()
except FileNotFoundError:
    print("FileNotFoundError occurs")


# * KeyError: 딕셔너리에 없는 key로 접근할 때 나는 에러
try:
    dict = {"k": "v"}
    print(dict["no"])
except KeyError as error_message:
    print("KeyError occurs")
    print(error_message)


# * IndexError: 리스트 범위를 벗어난 인덱스로 접근할 때 나는 에러
try:
    country_list = ["USA", "South Korea", "Japan"]
    pick_country = country_list[3]
except IndexError:
    print("IndexError occurs")

# * TypeError: 타입이 안 맞는 연산을 할 때 나는 에러 (동적/강한 타이핑 개념이랑 연결됨)
try:
    print(1 + "a")
    dict = {"k": "v"}
    print(dict["no"])
except TypeError:
    print("TypeError occurs")
else:
    print("this got triggered due to no error found")
finally:
    print("always running this")

# ? try - 에러가 날 수도 있는 코드를 넣는 곳
# ? except - try 안에서 에러가 나면 여기서 잡아서 처리
# ? else - try 안에서 에러가 하나도 안 났을 때만 실행
# ? finally - 에러가 나든 안 나든 무조건 마지막에 실행
# ? try 블록 안에서 에러가 나면, 그 지점에서 즉시 멈추고 except로 넘어감 (그 아래 남은 코드는 실행 안 됨)
