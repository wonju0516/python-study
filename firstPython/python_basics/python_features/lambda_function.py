# lambda 표현식

# * 람다(lambda): 이름 없이 한 줄로 만드는 간단한 함수
# * 문법 ->  lambda 인자: 표현식  -> return 없이 그 표현식의 결과가 바로 반환값이 됨


def square(num):
    return num**2


print(square(3))

# * 위 square 함수랑 완전히 같은 동작을 하는 람다 버전
# * square 이름을 재사용해서 변수에 람다 함수를 담음 -> 이제 square()는 def가 아니라 이 람다를 가리킴
square = lambda num: num**2
print(square(3))

# ? 그러면 왜 굳이 lambda를 씀?
# * map()/filter()처럼 "함수를 인자로 넘겨야" 하는 상황에서,
# * 그 함수가 한 줄짜리 간단한 계산이면 def로 이름 붙여 따로 정의하기 귀찮음
# * -> 그 자리에서 바로 즉석으로 만들어서 넘기는 용도

number_list = [1, 2, 3, 4, 5]
# * def로 따로 함수를 안 만들고, map() 안에서 바로 lambda로 처리
print(list(map(lambda num: num**2, number_list)))

# * filter도 마찬가지 -> is_even 같은 이름 붙일 필요 없이 그 자리에서 바로 조건 작성
print(list(filter(lambda num: num % 2 == 0, number_list)))
