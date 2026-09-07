# hash table
# * 연관 배열
## * 키로 값을 찾을 수 있다 -> 개념적 ADT일 뿐, 내부를 어떻게 구현하는지는 정해져 있지 않음

# * 딕셔너리 (dict)
## * 파이썬이 이 연관배열 ADT를 해시 테이블 방식으로 구현한 결과물

# * 해시 테이블
## * 고유한 키를 사용해 키-값 쌍을 저장하는 선형 자료구조 (키는 고유해야 함 -> 해시 테이블에 중복된 키는 저장 X)

# ! 연관 배열은 추상 타입 -> 해시 테이블은 연관 배열을 구현한 자료구조 -> 파이썬은 해시 테이블을 사용해 딕셔너리 구현

a_dict = {}
# * {} = dict, {key: value}면 dict / {값}만 있으면 set / [] = list(순서O, 변경O) / () = tuple(순서O, 변경X)
a_dict[1776] = "Independence year"
print(a_dict)

# * 86을 저장할 때: 86 % 7 (해시 함수) -> 2 (해시값) -> 배열의 2번 인덱스에 저장. (배열 - 해시 테이블 데이터를 저장할 배열임)

# ! 만약에 해시함수를 넣었을때 해시값이 같은 경우 -> 충돌 발생!!


# ? 문자열 속의 문자 수 세기
def count(a_string):
    a_dict = {}
    for char in a_string:
        if char in a_dict:  # * char가 a_dict 키값에 있다면 그 value를 1 더하기
            a_dict[char] += 1
        else:
            a_dict[char] = 1  # * 없으면 새로 1로 만들기
    print(a_dict)


count("hello")

# ? 두 수의 합 -> 정렬되지 않은 리스트에서 두 숫자의 합이 특정한 수가 되는 두 숫자의 인덱스를 찾는 문제
## ? 리스트에는 특정한 수가 되는 숫자의 쌍이 단 하나만 존재하며, 같은 숫자를 두번 쓸 수 없다고 가정합니다


# * 리스트를 순회하면서 더할 수 있는 모든 경우의 쌍을 더해 그 합이 5가 되는지를 확인하는 방법 -> O(n**2)
def two_sum_brute(the_list, target):
    for i in range(len(the_list)):
        for j in range(i + 1, len(the_list)):
            # * i+1부터: 앞쪽(0~i)은 이전 i들이 돌 때 이미 비교했고, i 자신과 더하는 것도 막기 위함
            if the_list[i] + the_list[j] == target:
                return [the_list[i], the_list[j]]


# * 딕셔너리를 사용하면?
def two_sum(a_list, target):
    a_dict = {}  # * {숫자: 인덱스} -> 숫자를 키로 둬야 in으로 O(1) 조회 가능
    for index, n in enumerate(a_list):
        rem = target - n  # * n과 짝지어 target을 만들려면 필요한 상대 숫자
        if rem in a_dict:  # * 그 상대(rem)를 이전에 이미 본 적 있으면(키로 존재하면)
            return index, a_dict[rem]  # * 지금 인덱스 + 그 상대가 저장된 인덱스 반환
        else:
            a_dict[n] = index  # * 아직 짝 못 찾음 -> 나(n)를 나중을 위해 저장해둠


# ? 주어진 문자열에서 중복되는 단어를 모두 제거해 보세요.
# ? 예를 들어 주어진 문자열이 I am a self-taught programmer looking for a job as a programmer.
# ? I am a self-taught programmer looking for a job as a. 이렇게 반환해야함
