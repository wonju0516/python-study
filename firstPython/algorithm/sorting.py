# sorting data
# * bubble sort
# ! 숫자 리스트를 순회하면서 각 숫자를 다음 숫자와 비교하고, 순서가 올바르지 않으면 둘의 위치를 바꾸는 정렬 알고리즘
# ! 버블 정렬은 첫번재 단계가 끝나면 가장 큰 숫자가 리스트의 마지막으로 이동함
def bubble_sort(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):  # ? range(n) -> 0부터 n-1까지
        no_swaps = True  # * 이번 패스에서 스왑이 한 번도 안 일어났는지 추적하는 플래그
        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False  # ! 스왑이 일어났으니 아직 정렬 안 끝났다는 표시
        if no_swaps:
            return a_list  # ! 스왑이 없었다 = 이미 정렬 완료 = 남은 패스 다 건너뛰기

    return a_list


# * insertion sort
# ! 리스트를 "정렬된 구간(앞쪽)"과 "아직 정렬 안 된 구간(뒤쪽)"으로 나눠서 생각한다.
# ! 정렬 안 된 구간에서 카드를 한 장씩 뽑아, 이미 정렬된 구간의 알맞은 위치에 끼워 넣는 정렬 알고리즘
# ! 리스트 두 번째 요소에서 시작하고 첫번째 요소와 비교히면서 정렬하는거임
def insertion_sort(a_list):
    for i in range(
        1, len(a_list)
    ):  # * for 루프는 리스트의 두번째 요소인 인덱스 1에서 시작
        value = a_list[i]  # * 현재값은 value라는 변수에 저장
        while (
            i > 0 and a_list[i - 1] > value
        ):  # * i가 0보다 크고 이전 요소가 다음 요소보다 크면 루프를 반복
            # ? 조건이 처음부터 거짓이면(a_list[i-1] <= value) 루프가 아예 안 돌고, i도 안 줄어듦
            # ? → 결국 a_list[i] = value는 원래 자리에 그대로 다시 저장하는 셈 (자기 위치가 이미 맞았다는 뜻)
            a_list[i] = a_list[
                i - 1
            ]  # * 정렬된 왼쪽의 어디에 숫자를 삽입할지를 결정해야 하기 때문에 i를 하나씩 줄임
            # * 그러면서 위치를 결정하게 됨
            i = i - 1
        a_list[i] = value  # ! 여기서 나온 i는 0이거나 a_list[i]가 value보다 작은 아이
    return a_list


# * merge sort
# ! 원소 1개 남을 때까지 절반씩 계속 쪼갠다 (원소 1개 = 이미 정렬된 것으로 취급, 재귀 종료 조건)
# ! 왼쪽을 완전히 다 합칠 때까지 끝낸 다음에야 오른쪽을 시작한다 (번갈아 하는 게 아님)
# ! 마지막에 정렬 끝난 왼쪽 결과 + 오른쪽 결과를 합친다(merge)
# ? merge: 두 조각의 맨 앞끼리 비교해서 더 작은 걸 꺼내고, 그 조각만 한 칸 전진 — 반복
# ? 한쪽이 먼저 다 떨어지면, 남은 쪽은 이미 정렬돼 있으니 그대로 뒤에 붙이면 끝


def merge_sort(a_list):
    # ! 리스트를 서브 리스트로 분할 하는 부분
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        # ! 리스트를 병합하는 부분
        left_ind = 0  # * left_half의 인덱스를 저장
        right_ind = 0  # * right_half의 인덱스를 저장
        alist_ind = 0  # * a_list의 인덱스를 저장

        # ! left_half의 첫번째 요소와 right_half의 첫번째 요소를 비교해 더 작은 숫자를 a_list 첫번째로 넣기
        # ! 그러고 각각 인덱스값을 1씩 올려서 다음 차례 계산
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1
            alist_ind += 1
        # ? 이 반복문이 멈추는 순간 -> 왼쪽이든 오른쪽이든 한쪽이라도 다 써버리면 멈추게 됨

        # ! 이때 이 두 개의 반복문은 한쪽만 남았을 때 처리하는 방식
        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1

        while right_ind < len(right_half):
            a_list[alist_ind] = right_half[right_ind]
            right_ind += 1
            alist_ind += 1


# * 파이썬의 정렬 알고리즘
# * 파이썬에는 sorted와 sort, 두 가지의 정렬 함수가 있다. -> 병합 정렬과 삽입 정렬을 조합한 하이브리드 정렬 알고리즘도 사용 (Timsort)

# ! sorted는 파이썬이 데이터를 서로 비교할 수만 있다면 어떤 데이터든 정렬할 수 있음
a_list = [1, 8, 10, 33, 4, 103]
print(sorted(a_list))

# ? 이런식으로 알파벳 순으로 정렬하거나 정수를 오름차순으로 정렬 -? 일단은 default는 오름차순
b_list = ["Guido van Rossum", "James Gosling", "Bredan Eich", "Yukihiro Matsumoto"]
print(sorted(b_list))

# ? sorted 함수는 옵션으로 reverse를 매개변수로 받음
# ? 내림차순으로 정렬하고 싶다면? -> reverse = True 매개변수를 전달하며 ㄴ됨
print(sorted(a_list, reverse=True))

# ? key라는 매개변수도 잇음 -> 각 요소에서 이 key 함수를 호출해 그 결과를 기준으로 정렬함
# * ex -> key에 len 함수를 전달하면 문자열의 길이를 기준으로 정렬
c_list = ["onehundered", "one", "three", "five", "seventy"]
print(sorted(c_list, key=len))

# ! sorted -> 새로운 리스트를 반환, 여러 곳에서 사용가능 (리스트, 튜플, 문자열, 세트, 딕셔너리)
# ! sort -> 리스트에만 사용가능, 원래 리스트를 수정함 (반환 자체를 안함), 매개변수 넣는건 동일함!
d_list = [5, 1, 290, 56, 98]
d_list.sort()
print(d_list)
