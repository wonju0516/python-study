# * 이진 힙(Binary Heap): 개념/heapq 모듈 정리는 README 참고

from heapq import heapify, heappop, heappush

# * heapify: 리스트를 최소 힙으로 in-place 재배열 (반환값 없음)
a_list = ["R", "C", "T", "H", "E", "D", "L"]
heapify(a_list)
print(a_list)

# * heappop: 루트(최솟값)를 꺼내면서 자동으로 재정렬까지 함
# * 재정렬 방식: 루트를 꺼내고 -> 맨 끝 값을 루트로 올린 뒤 -> 자식과 비교하며 내려보냄
a_list = ["R", "C", "T", "H", "E", "D", "L"]
heapify(a_list)
heappop(a_list)  # ! 꺼낸 값을 반환함
print(a_list)

# * while로 힙 전체를 꺼내면 오름차순으로 나옴
a_list = ["D", "E", "L", "H", "R", "T"]
heapify(a_list)
while len(a_list) > 0:
    print(heappop(a_list))

# * heappush: 값 삽입 후 자동 재정렬 -> 반환값 없음
a_list = ["D", "E", "L", "H", "R", "T"]
heapify(a_list)
heappush(a_list, "Z")
print(a_list)


# * 최소 비용으로 로프 연결하기 (그리디 + 힙, 문제 설명은 README 참고)
def find_min_cost(ropes):
    heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        sum = heappop(ropes) + heappop(ropes)  # * 최솟값 2개를 꺼내서 합침
        heappush(
            ropes, sum
        )  # * 합친 값도 "새 로프"로 다시 넣어야 다음 라운드에 또 합칠 후보가 됨
        cost += sum
    return cost


# * 이진 트리를 매개변수로 받아 최소 힙이면 True를, 그렇지 않으면 False를 반환하는 함수를 만들어보세요
# from heapq import heapify
def is_mean_heap(tree):
    heap = tree.copy()  # * copy를 통해 원본은 그대로 두고 복사본만 만들어서 그걸 변형함
    heapify(heap)  # * heapify를 하면 원본 자체가 재배열되므로 복사본으로 해야함
    return tree == heap


# ================================================================
# ? 여기부터는 심화/참고용: 힙을 라이브러리 없이 직접 구현해보는 연습
# ? (heapq 사용법과는 별개 내용 -> 지금 당장 몰라도 무방, 나중에 필요할 때 참고)
# ================================================================


# * 배열 기반 최대 힙 직접 구현 (heapq는 최소 힙 전용이라 문자열엔 -1 트릭이 안 통함)
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    # * heapify up: 새 값을 넣고 부모보다 크면 계속 위로 올려보냄
    def insert(self, key):
        self.heap.append(key)  # * 일단 맨 끝에 추가
        i = len(self.heap) - 1  # * 방금 넣은 값의 인덱스
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:  # * 부모보다 크면
            self.heap[i], self.heap[self.parent(i)] = (  # * 나와 부모 자리 swap
                self.heap[self.parent(i)],
                self.heap[i],
            )
            i = self.parent(i)  # * 옮겨간 자리로 인덱스 갱신 -> 다시 그 위 부모와 비교

    # * heapify down: 루트를 꺼내고, 맨 끝 값을 루트로 내린 뒤 자식과 비교하며 아래로 내려보냄
    def extract_max(self):
        if not self.heap:
            return None
        max_value = self.heap[0]  # * 반환할 값(루트=최댓값)을 따로 챙겨둠
        last = self.heap.pop()  # * 맨 끝 값을 꺼냄 (리스트에서도 제거됨)
        if self.heap:  # * 남은 값이 있을 때만 재정렬 필요
            self.heap[0] = last  # * 맨 끝 값을 루트 자리로 임시 이동
            i = 0
            while True:
                left, right, largest = self.left_child(i), self.right_child(i), i
                if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                    largest = left  # * 왼쪽 자식이 더 크면 갱신
                if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                    largest = right  # * 오른쪽 자식이 (더) 크면 갱신
                if largest == i:  # * 내가 여전히 제일 크면 -> 더 내려갈 필요 없음
                    break
                self.heap[i], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[i],
                )  # * 더 큰 자식과 swap
                i = largest  # * 내려간 자리로 인덱스 갱신 -> 다시 그 아래 자식과 비교
        return max_value  # * 처음에 챙겨뒀던 원래 루트 값 반환


max_heap = MaxHeap()
for ch in ["R", "C", "T", "H", "E", "D", "L"]:
    max_heap.insert(ch)
print(max_heap.heap)
print(max_heap.extract_max())  # * 'T'
