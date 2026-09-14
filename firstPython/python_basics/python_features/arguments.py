# * arguments and keyword arguments 언팩하기
# * 인자(arguments): 함수 호출할 때 넘기는 값들. 몇 개가 들어올지 모를 때 *, ** 로 한꺼번에 긁어모아 받을 수 있음

# * args
# * *args: 개수가 정해지지 않은 일반 값들을 하나의 튜플로 묶어서 받음. args라는 이름은 관례일 뿐, 핵심은 앞의 * 하나
def adding_numbers(*args):
    # * args is just name of variable
    _sum = sum([arg for arg in args])
    return _sum


print(
    adding_numbers(1, 2, 3)
)  # * 함수 안에서 args = (1, 2, 3) 으로 자동 묶임 -> sum = 6

# * kwargs
# * **kwargs: "이름=값" 형태(키워드 인자)로 넘어오는 것들을 하나의 딕셔너리로 묶어서 받음 (별 2개 = 딕셔너리로 묶음)


def concat_str(**kwargs):
    # * for kw in kwargs -> 딕셔너리를 그냥 순회하면 key(이름)만 나옴 (값이 아님)
    return "".join([kw for kw in kwargs])


print(concat_str(str1="a", str2="b", str3="c"))
# * kwargs = {"str1": "a", "str2": "b", "str3": "c"} -> key만 이어붙여서 "str1str2str3" 출력


def concat_str1(**kwargs):
    # * kwargs.values() -> key 말고 값(value)만 꺼내서 순회 -> "a", "b", "c"
    return "".join([kw for kw in kwargs.values()])


print(concat_str1(str1="a", str2="b", str3="c"))  # * 값만 이어붙여서 "abc" 출력

# * 일반 인자 + *args + **kwargs를 같이 쓸 때는 순서가 고정됨: (일반 인자) -> (*args) -> (**kwargs)
# ! 순서를 어기면(예: **kwargs를 *args보다 앞에 두면) SyntaxError 발생

