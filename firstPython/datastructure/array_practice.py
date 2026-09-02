# array.py

# * 리스트
# ? 순서가 있는 값을 저장하는 자료구조를 정의하는 추상 데이터 타입

# * 배열
# ? 연속적인 메모리 블록에 인덱스와 함께 요소를 저장하는 자료구조
# ? 보통 동질적이며 정적임 -> 동질적 자료구조? - 정수나 문자열과 같이 한가지의 데이터 타입만 담을 수 있다는 것

# ! 그러나 파이썬의 리스트는 이질 가변 길이 배열임
# ! 가변 길이 배열 - 생성한 뒤에도 크기를 바꿀 수 있음
# ! 이질 배열 - 여러 타입의 데이터를 담을 수 있음

# * 1차원 배열
array = [1, 2, 3]
print(array[0])

# * 다차원 배열 -> 차원의 수만큼의 인덱스를 사용해 각 요소에 접근

multi_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(multi_array[1][2])

# ! 정렬되지 않은 배열 탐색 -> O(n) -> 추가나 삭제 등 어떤 형태로든 배열을 변경하는 작업의 시간복잡도
# ! 정렬된 배열 탐색 -> O(logn)

import array

# * 배열의 일정한 성능이 필요하면 파이썬에 내장된 array 클래스를 이용하는 것이 좋음

arr = array.array(
    "f", (1.0, 1.5, 2.0, 2.5)
)  # ! 한가지의 타입만 담을 수 있는 배열 (문자열은 못담아)
# * array.aray("typecode", (초기값))
# ? typecode -> "i" - 정수, "d" - 배정도 실수(double)
print(arr[1])


# * 0 옮기기
# ? 리스트에 0을 모두 찾아 리스트의 마지막으로 옮기고 나머지 요소는 원래 순서를 유지하라는 문제
def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(
        a_list
    ):  # ? (인덱스, 값)을 한 장씩 순서대로 꺼내주는 함수
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return a_list


# ! 내가 직접 생각한 방법
def move_zeros2(a_list):
    zero_index = 0
    zero_count = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            zero_index += 1
        else:
            zero_count += 1
    for i in range(zero_count):
        a_list[zero_index + i] = 0
    return a_list


a_list = [8, 0, 3, 0, 12]
move_zeros2(a_list)
print(a_list)

# * 리스트의 결합
movie_list = ["interstellar", "inception", "the prestige", "insomnia", "batman begins"]
ratings_list = [1, 10, 10, 8, 6]

# ! 이 둘을 결합해 튜플 리스트로 만들겠다 -> 튜플은 추가 또는 삭제할 수 없는 불변의 자료구조
# ! zip 함수를 이용하면  두 리스트를 결합할 수 있다
print(list(zip(movie_list, ratings_list)))
# ? zip 함수는 하나 이상의 이터러블 데이터를 받아 각 이터러블 데이터의 요소를 순서대로 묶어 놓은 zip 객체 반환
# ? 이 객체를 리스트로 변환

# * 중복 요소 찾기
# ! set를 활용하기! -> 중복을 허용하지 않고, 순서가 없는 값들의 집합임
a_set = set()
a_set.add("Kanye West")  # * .add로 추가하기
a_set.add("Kendall Jenner")
a_set.add("Justin Bieber")
print(a_set)
a_set.add("Kanye West")
print(a_set)  # ! 추가하지 않는다 (중복이라)


# * 세트를 사용해 리스트에 중복이 있는 확인하는 함수
def return_dups(an_interable):
    dups = []  # ? 중복되는 요소를 저장할 리스트
    a_set = set()  # ? 빈 세트

    for item in an_interable:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if (
            l1 == l2
        ):  # * 추가를 했는데 길이가 같은거면 중복이라 추가가 안된거라 빈 리스트에 추가
            dups.append(item)
    return dups


a_list1 = ["Susan Adams", "Kwame Goodall", "Jill Hampton", "Susan Adams"]
dups = return_dups(a_list1)
print(dups)

# * 두 리스트의 교집합 찾기
this_weeks_winners = [2, 43, 48, 62, 64, 28, 3]
most_common_winners = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]


def return_inter(list1, list2):
    list3 = [v for v in list1 if v in list2]
    # * 리스트 축약 문법: [표현식 for 변수 in 반복대상 if 조건]
    # ? for v in list1 -> list1의 원소를 하나씩 꺼내서 v에 담음
    # ? if v in list2 -> 그 v가 list2 안에도 있는지 확인 (조건 통과한 것만 남김)
    # ? [v ...] -> 조건을 통과한 v들만 모아서 새 리스트로 만듦
    # ! 즉 list1을 돌면서, list2에도 들어있는 값만 골라 새 리스트에 담는 것 -> 두 리스트의 교집합
    return list3


print(return_inter(this_weeks_winners, most_common_winners))


# * 이 문제를 세트를 사용해서 풀이가능
# ! set에는 두 개 이상의 세트에 모두 존재하는 요소를 반환하는 교집합 함수 intersection이 있어 사용 가능
set1 = set(this_weeks_winners)
set2 = set(most_common_winners)  # ? 세트로 바꾸기

set1.intersection(
    set2
)  # ? 이를 통해 교집합이 있는지 (중복되는 요소가 있는지 확인할 수 있다)
list(set1.intersection(set2))  # ? list로 교집합을 다시 리스트로 변환함


# ! 함수로 만들기
def return_inter2(list1, list2):
    set1 = set(list1)
    set2 = set(list2)  # ? 세트로 바꾸기
    return list(
        set1.intersection(set2)
    )  # ? 이를 통해 교집합이 있는지 (중복되는 요소가 있는지 확인할 수 있다)
    # * list()로 감싸서 리스트로 반환


new_list = return_inter2(this_weeks_winners, most_common_winners)
print(new_list)

# ? intersection은 두개의 세트만 비교하는 것 X!
# ? s1.intersection(s2,s3,s4) -> 여러개 가능


# * 음이 아닌 정수로 구성되어 있는 배열 an_array에서 짝수만 추출한 배열과 홀수만 추출한 배열을 만들어보세요


# * append(값) / insert(인덱스, 값) -> 리스트 "크기를 늘리면서" 새 값을 넣는 것
# ? append는 맨 뒤에 추가, insert는 원하는 인덱스에 끼워넣기 (그 자리에 있던 값은 뒤로 밀림)
# * 리스트[인덱스] = 값 -> 크기는 그대로 두고, 이미 있는 그 자리 값을 덮어쓰는 것(대입)
# ! 대입은 그 인덱스가 이미 존재할 때만 가능함 -> 빈 리스트에 evens_list[0] = 1 처럼 쓰면
# ! 아직 0번 자리 자체가 없어서 IndexError 발생 (그래서 빈 리스트를 채워나갈 땐 append를 써야 함)
def split_evens_odds(a_list):
    evens_list = []
    odds_list = []
    for i in a_list:
        if i % 2 == 0:
            evens_list.append(i)
        else:
            odds_list.append(i)
    return evens_list, odds_list


an_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(split_evens_odds(an_array))
