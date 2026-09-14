def get_num1(num):
    return [str(i) for i in range(num)]


print(get_num1(10))


def get_num2(num):
    return list(map(str, range(num)))


print(get_num2(10))


# * 시간 체크 (import time)

import time

## * before
start = time.time()
## * run
get_num1(1000)
## * after
end = time.time()
diff = end - start
print(diff)


## * before
start = time.time()
## * run
get_num2(1000)  # ! -> 이 친구가 더 빠름
## * after
end = time.time()
diff = end - start
print(diff)

# * 시간 체크 (import timeit)
## ! time.time()과 다르게, timeit은 지정한 횟수만큼 반복 실행해서 평균을 내주므로 측정이 더 정확함
import timeit

stmt = """
gen_num1(1000)
"""  # * stmt(statement) -> 실제로 시간을 측정할 대상 코드 (반복 실행될 부분)
setup = """
def gen_num1(num):
    return [str(i) for i in range(num)]
"""  # * setup -> stmt 실행 전에 한 번(설정용으로) 실행됨. timeit은 바깥(전역) 변수/함수에 접근 못 해서, stmt에서 쓸 함수를 여기서 직접 정의해줘야 함
# ! stmt/setup 둘 다 문자열(""" """)로 작성 -> 실제 코드가 아니라 "실행할 코드 텍스트"를 넘기는 것

t = timeit.timeit(
    stmt=stmt, setup=setup, number=100
)  # * number=100 -> stmt를 100번 반복 실행한 총 소요 시간을 반환
print(t)
