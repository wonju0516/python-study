# 스코프 (지역 변수 vs 전역 변수)
# * local scope -> 함수 안에서 만든 변수, 그 함수 안에서만 접근 가능
# * global scope -> 파일 최상단(함수 밖)에서 만든 변수, 어디서든 읽기 가능
# * enclosing scope -> 함수 안에 또 함수가 있을 때, 바깥 함수의 지역 스코프 (안쪽 함수 입장에서 한 단계 바깥)
# * namespace -> "이름(변수명) -> 값"을 연결해주는 장부. global/local이 각각 별도의 장부라 같은 이름이 있어도 안 겹침

my_score = 50  # * global scope


def inside_value_function():
    # * global my_score -> 주석 풀면, 아래 my_score가 지역 변수가 아니라 전역 my_score를 그대로 수정하게 됨
    # ! 그러면 함수 밖에서 찍어도 50이 아니라 80이 나옴 (전역 값 자체가 바뀌므로)
    # global my_score
    my_score = 80  # * local scope
    print(f"my score inside is {my_score}")


inside_value_function()
print(f"my score outside is {my_score}")


# * if/for/while은 함수가 아니라서 새 스코프를 안 만듦 -> 그 안에서 만든 변수도 바깥과 같은 스코프에 그대로 남음
# * 그래서 지금처럼 if 블록 안에서 바꾼 my_score도 진짜 전역 my_score가 90으로 바뀌는 것
did_extra_work = True
if did_extra_work:
    my_score = 90

print(f"my score ouside is {my_score}")


# * nonlocal -> "한 단계 바깥 함수(enclosing scope)의 변수"를 가리키게 해줌 (global처럼, 대상만 다름)
# ! 없으면 b() 안의 x=20은 새 지역 변수를 만들 뿐이라 a()의 x는 그대로 10, print(x)도 10이 나옴
# * nonlocal을 써야 b()가 a()의 x를 진짜로 수정함 -> print(x)가 20이 됨
def a():
    x = 10

    def b():
        nonlocal x
        x = 20

    b()
    print(x)


a()

# * how python search the variable? -> 변수 이름을 찾을 때 확인하는 순서 = LEGB 규칙
# * L(local, 지금 함수) -> E(enclosing, 한 단계 바깥 함수) -> G(global, 전역) -> B(built-in, print 등 내장)
# * 이 순서대로 뒤지다가 가장 먼저 찾은 값을 씀 (안쪽에 같은 이름 있으면 바깥 건 아예 안 봄)

country = ["south korea"]


# * my_score=80은 "=" 대입이라 지역 변수를 새로 만들지만, .append()는 대입이 아니라 메서드 호출
# * country라는 이름을 새로 만드는 게 아니라 country가 가리키는 그 리스트 객체를 직접 수정하는 것
# ! 그래서 지역 변수가 안 만들어지고, LEGB로 전역 country를 찾아서 원본 리스트가 그대로 바뀜
def inside_list_function1():
    country.append("usa")


inside_list_function1()
print(country)


# * globals() -> global 키워드가 아니라, 전역 namespace를 딕셔너리로 보여주는 내장 함수
print(globals())
# ! 이거를 사용하면 현재 글로벌 namespace 안에 있는 변수들이 어떤게 있는지 나옴

# ? 그럼 global scope 는 보통 언제 사용
## * 반복되는 상수가 있음 -> 보통 그것들은 한 곳에다가 지정해놓고 다음에 여러번 사용
## ! 값을 자꾸 바꾸는 용도로는 지양 -> 함수는 인자로 받고 return으로 돌려주는 게 더 안전함
