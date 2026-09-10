# * 제너레이터(generator)
# * 리스트처럼 for문으로 순회 가능하지만, 값을 미리 다 만들어 메모리에 저장하지 않고 필요할 때마다 하나씩 계산해서 넘겨주는 함수 ("lazy iterator")
# ? 리스트: 결과를 전부 미리 만들어서 메모리에 쌓아둠 vs 제너레이터: 요청받을 때마다 그때그때 하나씩만 계산 -> 데이터가 크거나 끝이 없는 경우에 메모리 절약됨
# * 이터레이터(iterator): next() 호출할 때마다 값을 하나씩 꺼내주는 객체 (상태를 기억) -> 제너레이터는 이터레이터를 쉽게 만드는 방법 중 하나


# * 일반 함수 방식: n개의 세제곱수를 다 계산해서 리스트에 담고, 한 번에 통째로 return
def get_cubes(n):
    output = []
    for x in range(n):
        output.append(x**3)
    return output


print(get_cubes(5))  # * [0, 1, 8, 27, 64] -> 리스트 전체가 한 번에 메모리에 만들어짐

for x in get_cubes(5):
    print(x)  # * 이미 다 만들어진 리스트를 하나씩 순회하는 것뿐


# * 제너레이터 함수: return 대신 yield를 씀 -> 이 함수를 호출해도 코드가 바로 실행되는 게 아니라 "제너레이터 객체"만 만들어짐
# * yield x**3: "여기서 값을 하나 내보내고, 잠깐 멈춰있다가 다음 요청 오면 이어서 실행"이라는 뜻 (return처럼 함수가 끝나버리는 게 아님)
def get_cubes2(n):
    for x in range(n):
        yield x**3


# * 리스트가 아니라 <generator object ...> 출력됨 -> 아직 계산 하나도 안 한 상태 (lazy)
print(get_cubes2(19))

for x in get_cubes2(5):
    print(x)  # * for문이 내부적으로 next()를 계속 호출해줘서 값이 하나씩 뽑혀나옴

cubes = get_cubes2(5)
# * 역시 generator object 자체가 찍힘 (아직 안이 비어있는 게 아니라, 아직 "실행을 안 한" 상태)
print(cubes)

# * next(객체): 이터레이터/제너레이터한테 "다음 값 하나만 계산해서 줘"라고 요청하는 함수
# * 호출할 때마다 yield 지점까지 실행 -> 값 하나 반환 -> 거기서 멈춤 -> 다음 next() 오면 멈춘 데서 이어서 실행
print(next(cubes))  # 0
print(next(cubes))  # 1
print(next(cubes))  # 8
print(next(cubes))  # 27
print(next(cubes))  # 64

s = "Joon"
# ! str은 iterable(순회 가능)이지 iterator는 아님 -> next()는 iterator한테만 쓸 수 있어서 TypeError: 'str' object is not an iterator 발생
# print(next(s))

# * iter(객체): iterable을 iterator로 변환 -> 이렇게 변환해야 next()로 하나씩 꺼낼 수 있음
# * list, tuple, dict, set도 전부 iterable이지 iterator가 아니라서 next()를 바로 쓰려면 똑같이 iter()로 먼저 변환해야 함
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
