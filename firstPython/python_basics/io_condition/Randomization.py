# Randomization
# * random module
import random

print(random.randint(1, 100))  # * 정수 리턴

import mok_module  # * 모듈 만들어보기

print(mok_module.MY_LOCATION)

random_float = random.random()  # * 이거는 정수가 아니라 0-1 사이의 값을 리턴
print(random_float)

# ? how to generate 0 - 10?
print(int(random_float * 10))

# * randrange(a, b) -> range(a, b)처럼 b는 제외하고 랜덤 정수 (randint(1,10)은 10 포함, randrange(1,10)은 10 제외)
print(random.randrange(1, 10))

# * uniform(a, b) -> a부터 b 사이의 랜덤 실수(float)
print(random.uniform(1.0, 5.0))

fruits = ["apple", "banana", "cherry", "grape"]

# * choice(리스트) -> 리스트에서 원소 하나만 랜덤으로 뽑기
print(random.choice(fruits))

# * sample(리스트, n) -> 리스트에서 중복 없이 n개 랜덤으로 뽑기 (로또 번호 뽑기 같은 상황에 사용)
print(random.sample(fruits, 2))

# * shuffle(리스트) -> 리스트 순서를 그 자리에서 랜덤으로 섞음 (반환값 없음, 원본이 바로 바뀜)
random.shuffle(fruits)
print(fruits)
