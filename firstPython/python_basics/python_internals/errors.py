# 에러/예외 다루기

is_correct = True


def func():
    if is_correct == True:
        return True
    else:
        return False


# * better solution -> is_correct가 이미 True/False인 불리언이라 비교/분기 없이 그 값 자체를 바로 반환하면 됨
## ! `== True`로 비교하는 것 자체가 불필요한 코드 (이미 불리언인 값을 굳이 다시 True와 비교)
def func1():
    return is_correct


total = 0
num_lst = [1, 2, 3, 4, 5]
for n in num_lst:
    total += n

# * better solution -> sum()은 내장 함수, 직접 반복문 짤 필요 없이 한 줄로 합계 구함 (실수할 여지도 적음)
total = sum(num_lst)
print(total)

import math

# * 최솟값이나 최댓값 찾기
num_lst = [1, 2, 3, 4, 5]
minimum = math.inf  # * 양의 무한대 -> 어떤 숫자든 이거보다 작으니 최솟값 찾는 초기값으로 안전함 (음수만 있어도 문제없음)
for n in num_lst:
    if n < minimum:
        minimum = n

# * better solution -> min()/max() 내장 함수, math.inf로 초기값 잡는 것보다 간단하고 오타/실수 위험 없음
minimum = min(num_lst)
maximum = max(num_lst)
print(minimum)

# * 평균 구하기
total = 0
for n in num_lst:
    total += n
avg = total / len(num_lst)

# * better solution -> numpy의 mean()이 최적화되어 있어 대용량 데이터에서 직접 짠 반복문보다 빠르고 간결함
import numpy as np

avg = np.mean(num_lst)
print(avg)

# * sort vs sorted
l1 = [4, 2, 3, 7, 5]
print(l1.sort())  # ! sort는 원본을 직접 정렬하고 반환값이 없음(None) -> 그래서 이 print는 None이 찍힘
l2 = [6, 4, 2, 8, 3]
l2 = sorted(l2)  # * sorted는 원본은 그대로 두고, 정렬된 "새 리스트"를 반환함
print(l2)
