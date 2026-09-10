# * map(함수, 리스트): 리스트의 각 원소에 함수를 하나씩 적용해서 새로운 결과를 만들어줌


def square(num):
    return num**2


print(square(3))

number_list = [1, 2, 3, 4, 5]
# ! map()은 결과를 바로 리스트로 안 주고 map 객체(제너레이터 비슷한 것)를 돌려줌 -> print해도 값이 안 보임
print(map(square, number_list))

# * map 객체는 for문으로 하나씩 꺼내 쓸 수 있음
for i in map(square, number_list):
    print(i)

# or..

# * list()로 감싸면 map 객체를 한 번에 리스트로 변환해서 값 확인 가능
print(list(map(square, number_list)))

# ? 인자가 여러 개 필요한 함수는 어떻게 map에 넣을까?


def sum(a, b):
    return a + b


lst1 = [2, 4, 6, 8]
lst2 = [1, 3, 5, 7, 9]
# * map(함수, 리스트1, 리스트2): 같은 순서끼리 짝지어서 함수에 두 개씩 넘겨줌
print(list(map(sum, lst1, lst2)))


# * filter(함수, 리스트): 함수 결과가 True인 원소만 걸러서 남김 (함수는 True/False를 반환해야 함)
def is_even(num):
    return num % 2 == 0


print(is_even(3))

number_list = [1, 2, 3, 4, 5]
# * filter도 map처럼 filter 객체를 돌려주기 때문에 list()로 감싸야 값이 보임
print(list(filter(is_even, number_list)))
