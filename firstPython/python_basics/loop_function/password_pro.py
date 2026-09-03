import random
import string

# * 직접 다 적은 버전 (혹시 몰라서 남겨둠, 실제로는 아래처럼 안 씀)
# lower_alphabets = [
#     "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
# ]

# * string 모듈로 짧게 쓰는 버전 (실무/코테에서 실제로 쓰는 방식) -> string을 import 하고 나서 하기
# ! list()로 감싸야 할 때: 나중에 원소를 바꾸거나(mutable) 리스트 전용 메서드(remove, append 등)가 필요할 때
# ? list()로 안 감싸도 될 때: random.choice(), in, for 순회처럼 문자열 그대로도 되는 작업만 할 때
lower_alphabets = list(string.ascii_lowercase)  # * 그러고 리스트로 감싸기!!

upper_alphabets = list(string.ascii_uppercase)

# * 소문자를 하나씩 꺼내서 .upper()로 대문자로 바꿔 담는 방식 -> string.ascii_uppercase 쓰는 것과 결과 동일
# upper_alphabets = []

# for alphabet in lower_alphabets:
#     upper_alphabets.append(alphabet.upper())


alphabets = lower_alphabets + upper_alphabets
# * 리스트 축약(list comprehension) -> for i in range(10)을 돌면서 str(i)를 하나씩 리스트에 담은 것
# ? 풀어쓰면: numbers = []; for i in range(10): numbers.append(str(i))
numbers = [str(i) for i in range(10)]  # * range(0,10)이랑 동일
symbols = ["!", "#", "$", "&", "(", ")", "*", "+"]

# * 비밀번호에 각각 몇 개씩 넣을지 개수 지정 (총 9+3+2 = 14자리)
num_of_alphabets = 9
num_of_numbers = 3
num_of_symbols = 2

strong_password = []

# * 알파벳 리스트에서 랜덤 인덱스로 num_of_alphabets개만큼 뽑아서 채움
for i in range(num_of_alphabets):
    strong_password.append(alphabets[random.randint(0, len(alphabets) - 1)])

# * 숫자 리스트에서 랜덤 인덱스로 num_of_numbers개만큼 뽑아서 채움
for i in range(num_of_numbers):
    strong_password.append(numbers[random.randint(0, len(numbers) - 1)])

# * 특수문자 리스트에서 랜덤 인덱스로 num_of_symbols개만큼 뽑아서 채움
for i in range(num_of_symbols):
    strong_password.append(symbols[random.randint(0, len(symbols) - 1)])

print(strong_password)

random.shuffle(strong_password)  # * 리스트 위치를 각각 셔플함

print(strong_password)

# * 리스트를 한 줄(하나의 문자열)로 만들려면 -> "".join(리스트) 사용

print("".join(strong_password))
