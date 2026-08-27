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

        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1

        while right_ind < len(right_half):
            a_list[alist_ind] = right_half[right_ind]
            right_ind += 1
            alist_ind += 1
