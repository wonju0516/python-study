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
    first = 0
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
