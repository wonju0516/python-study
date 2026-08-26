# search_algorithm
# * 선형 탐색 알고리즘
def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
        # ! else가 없어도 잘 동작함
    return False


a_list = [1, 8, 32, 91, 5, 15, 9, 100, 3]
print(linear_search(a_list, 1003))

# ! 실제로 프로그래밍 할 때는 선형 탐색을 직접 작성 X -> 파이썬에 내장된 in 키워드 사용!!
# * in 키워드: "값 in 리스트" 형태로 써서, 리스트 안에 그 값이 있으면 True, 없으면 False를 반환한다.
# * 즉 위에서 직접 만든 linear_search 함수가 하던 일을
# * 파이썬이 이미 in 키워드로 기본 제공해준다 (내부적으로 선형 탐색과 같은 동작을 함).
unsorted_list = [1, 45, 4, 32, 3]
print(100 in unsorted_list)

# ! 문자열에서도 사용 가능 -> 특정 글자를 찾기 위해 선형 탐색을 사용할 수 있음
letter = "a"
print(letter in "apple")


# ? 데이터가 정렬되어 있다면 모든 요소를 검사하는 선형 탐색보다 이진 탐색을 사용할 수 있음
# * 이진 탐색 (Binary Search)
def binary_search(a_list, n):
    first = 0  # * 인덱스
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
        return False


# ? else: 이런식으로 작성되어 있는 그냥 elif n < a_list[mid]: -> 이런식으로 작성해도 댐!!

# ! 이진 탐색도 파이썬에 내장 모듈을 통해 구현할 수 있음
# ! bisect 모듈에 들어 있는 bisect_left -> 정렬된 리스트에 대상이 없는 경우 존재했다면 있었을 인덱스를 반환한다, 았으면 그 인덱스 반환함
from bisect import bisect_left

sorted_fruits = ["apple", "banana", "orange", "plum"]
# ! bisect_left만 실행하면 결과값이 함수 실행 후 사라져버려서 화면엔 아무것도 안 뜬다.
# ! 화면에 결과를 보려면 반드시 print()로 감싸야 한다.
print(bisect_left(sorted_fruits, "fruit"))

# ! bisect_left는 찾으려는 요소가 리스트에 있는지 확인하기 위해서 그 인덱스가 먼저 있는지 체크하는 코드로 작성해야 함


def binary_search1(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index < len(an_iterable) and an_iterable[index] == target:
        return True
    return False
