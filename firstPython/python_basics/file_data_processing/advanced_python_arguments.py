# Arguments with Default Values: 함수 정의할 때 파라미터에 기본값을 미리 넣어두는 것 (mode="w")
from pathlib import Path

# * .parent는 속성(property)이라 괄호 없이 씀. 괄호 붙이면(.parent()) "이미 나온 값을 함수처럼 호출"하는 게 돼서 에러남
BASE_DIR = Path(__file__).parent


# * mode="w": 호출할 때 mode를 안 넘기면 자동으로 "w"가 적용됨 (기본값)
def write_str_to_file(file, content, mode="w"):
    # * with open(파일, mode=모드) as f: 파일을 열고, 블록 끝나면 자동으로 f.close() 해줌
    with open(file, mode=mode) as f:
        f.write(content)


# * mode="a"를 직접 넘겨서 기본값("w") 대신 append 모드로 덮어씀
write_str_to_file(file=BASE_DIR / "sample.txt", content="Hello world!!!!!", mode="a")


# * *args vs **kwargs 한 줄 요약: *는 튜플로 받음(이름 없는 값들), **는 딕셔너리로 받음(이름=값 쌍들)

# * Unlimited Positional Arguments: *args는 인자를 몇 개 넘기든 다 받아서 하나의 튜플로 묶어줌
def unlimited_func(*args):
    print(args[2])  # * args는 튜플이라 인덱스로 접근 가능. args[2] = 세 번째로 넘긴 값


unlimited_func(1, 2, 3)  # * args = (1, 2, 3)


# * *args의 진짜 쓸모: 인자 개수가 몇 개든 상관없이 처리하는 함수를 만들 수 있음
def sum_all(*arg_list):
    total = 0
    for n in arg_list:  # * 튜플이라 for문으로 순회 가능
        total += n
    return total


print(sum_all(1, 2, 3))
# * sum_all(1, 2)도, sum_all(1,2,3,4,5)도 다 됨 (파라미터 개수 고정 안 함)

print("---------------")


# * **kwargs (Keyword Arguments): "이름=값" 형태로 넘긴 인자들을 전부 딕셔너리로 묶어서 받음 (*args의 딕셔너리 버전)
def calc(**kwargs):
    print(kwargs)  # * {"n1": 1, "ne": 3, "func": "add"}


calc(n1=1, ne=3, func="add")

print("---------------")


# * 일반 파라미터(func)와 **kwargs를 같이 쓸 수도 있음: func는 이름 그대로 받고, 나머지 이름=값들은 kwargs에 다 모임
def calc(func, **kwargs):
    for k, v in kwargs.items():  # * 딕셔너리라 .items()로 key, value 순회 가능
        print(k)
        print(v)
    if func == "add":
        return kwargs["n1"] + kwargs["n2"]  # * kwargs["키"]로 값 꺼내기


print(calc(n1=1, n2=3, func="add"))
