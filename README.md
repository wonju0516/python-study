# algo-basics

알고리즘 / 자료구조 기초 공부 기록용 저장소입니다.

## 폴더 구조

```
firstPython/
├── algorithm/
│   ├── algorithm1.py       # 반복문 기초 (for, range)
│   ├── recursion.py        # 재귀 기초 (팩토리얼)
│   ├── search_Algorithm.py # 탐색 알고리즘
│   └── sorting.py          # 정렬 알고리즘
└── dataStructure/
    └── array.py            # 자료구조 (준비 중)
```

## 재귀 (Recursion)

함수가 자기 자신을 다시 호출해서, 문제를 더 작은 문제로 쪼개 해결하는 방식.

- **반복(iterative)**: `while`/`for` 반복문으로 값을 계속 갱신하며 계산
- **재귀(recursive)**: 함수가 자기 자신을 호출, 종료 조건(base case)에 도달하면 멈춤

```python
# 반복
def factorial(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n -= 1
    return the_product

# 재귀
def factorial_2(n):
    if n == 0:
        return 1
    return n * factorial_2(n - 1)
```

## 탐색 알고리즘 (Search)

| 알고리즘 | 개념 | 시간복잡도 |
|---|---|---|
| 선형 탐색 (Linear Search) | 리스트를 처음부터 끝까지 하나씩 순회하며 비교 | O(n) |
| 이진 탐색 (Binary Search) | **정렬된** 리스트를 대상으로, 중간값과 비교해 탐색 범위를 절반씩 좁혀나감 | O(log n) |

이진 탐색은 데이터가 정렬돼 있을 때만 쓸 수 있고, 그 대신 선형 탐색보다 훨씬 빠름.

### 직접 구현 vs 파이썬 내장 기능

| 하고 싶은 것 | 직접 구현 | 파이썬 내장 기능 |
|---|---|---|
| 리스트/문자열에 값이 있는지 확인 | `linear_search()` | `in` 키워드 (`값 in 리스트`) |
| 정렬된 리스트에서 값 찾기 | `binary_search()` | `bisect.bisect_left()` |

`bisect_left`는 값이 있는지 없는지(True/False)가 아니라, "정렬 순서를 유지하려면 몇 번째 인덱스에 넣어야 하는가"를 반환하므로, 있는지 확인하려면 인덱스 범위 체크(`index < len(list)`)와 값 비교(`list[index] == target`)를 추가로 해줘야 함.

## 정렬 알고리즘 (Sort)

| 알고리즘 | 개념 | 시간복잡도 |
|---|---|---|
| 버블 정렬 (Bubble Sort) | 인접한 두 원소를 비교해서 순서가 틀리면 교환, 이를 반복 | O(n²) |
| 삽입 정렬 (Insertion Sort) | 리스트를 정렬된 구간 / 안 된 구간으로 나누고, 안 된 구간에서 하나씩 꺼내 정렬된 구간의 알맞은 위치에 삽입 | O(n²) |
| 병합 정렬 (Merge Sort) | 원소 1개가 남을 때까지 재귀적으로 반씩 쪼갠 뒤, 두 조각을 비교하며 다시 병합(merge) | O(n log n) |

### 직접 구현 vs 파이썬 내장 기능

| 하고 싶은 것 | 직접 구현 | 파이썬 내장 기능 |
|---|---|---|
| 리스트 정렬 | `bubble_sort()`, `insertion_sort()`, `merge_sort()` | `list.sort()` (원본 변경) / `sorted(list)` (새 리스트 반환) |

파이썬 내장 정렬은 **Timsort**(병합 정렬 + 삽입 정렬을 결합한 알고리즘)를 사용하며, 실무에서는 대부분 이 내장 함수를 사용함. 직접 구현은 알고리즘의 동작 원리와 시간복잡도를 이해하기 위한 학습 목적.
