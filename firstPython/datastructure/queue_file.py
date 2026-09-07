# queue
# * FIFO -> 선입선출 : 가장 먼저 추가한 요소부터 제거하는 자료구조
## * 인큐 -> 요소를 큐에 추가 -> O(1)
## * 디큐 -> 요소를 큐에서 제거하는 것 -> O(1)
## * 큐에 있는 요소에 접근하거나 탐색하는 작업 -> O(n)

# ! 큐는 스택과 마찬가지로 저장할 수 있는 요소에 제한이 있을 수도 있고, 없을 수도 있다
## * 제한적 큐 -> (배열을 사용해 만들기)
## * 무제한 큐 -> (링크드 리스트를 사용해 만들기)


# ? 링크드 리스트를 사용해 Queue 클래스 만들기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.front = None  # * 앞 뒤 요소 저장
        self.rear = None
        self._size = 0  # * 큐 크기를 저장할 변수

    def enqueue(
        self, item
    ):  # * 맨 뒤에 요소를 추가하는 메서드 -> item : 큐에 저장할 데이터를 매개변수로 받음
        self._size += 1
        node = Node(item)  # * 새 노드를 만들어서 요소를 저장
        if (
            self.rear is None
        ):  # * 큐가 비어있다면? -> 지금 만든 요소를 맨 앞, 뒤 에다가 둡니다
            self.front = node
            self.rear = node
        else:
            self.rear.next = node  # * 기존 마지막 노드(rear)가 새 노드를 가리키게 연결
            self.rear = (
                node  # ! rear 이름표를 새 노드로 옮김 -> 새 노드가 새로운 마지막이 됨
            )

    def dequeue(self):  # * 큐의 맨 앞에서 요소를 꺼내는 메소드
        if self.front is None:  # * 큐가 비어있을 때 디큐 시도하면 예외를 일으키는 코드
            raise IndexError("pop from empty queue")
        self._size -= 1
        temp = self.front  # * 맨 앞에 있는 노드를 임시 변수에 저장
        self.front = self.front.next  # ! front 이름표를 다음 노드로 옮김
        if self.front is None:  # * 마지막 노드까지 뺐다면
            self.rear = None  # ! rear도 같이 None으로 맞춤 (안 그러면 front는 비었는데 rear만 예전 노드를 가리키게 됨)
        return temp.data

    def size(self):
        return self._size


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.size())
for i in range(3):
    print(queue.dequeue())


# * 파이썬에 내장된 큐 클래스
from queue import Queue

q = Queue()
q.put("a")  # * put = enqueue (뒤에 추가)
q.put("b")
q.put("c")
print(q.qsize())
for i in range(3):  # ! i는 그냥 "3번 반복" 카운터일 뿐, 꺼내는 값이랑 무관
    print(q.get())  # * get = dequeue (앞에서 꺼내기, put한 순서대로 나옴 -> FIFO)


# * 두 개의 스택을 사용해 큐 만들기
class Queue:
    def __init__(self):
        self.s1 = []  # * 큐 역할 (매번 front가 top에 오도록 재정렬해서 유지)
        self.s2 = []  # * s1을 뒤집는 용도의 임시 스택

    def enqueue(self, item):
        while len(self.s1) != 0:  # * s1을 통째로 s2로 옮겨서 순서를 뒤집음
            self.s2.append(self.s1.pop())
        self.s1.append(item)  # * 비워진 s1 맨 아래에 새 값을 넣음
        while len(self.s2) != 0:  # * s2를 다시 s1으로 옮겨서 원래 순서로 복구
            self.s1.append(self.s2.pop())
        # ! 결과: s1의 top(맨 위)이 항상 "가장 먼저 들어온 값(front)"이 됨

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Cannot pop from empty queue")
        return self.s1.pop()  # * s1의 top = front라서 pop()이 곧 큐의 dequeue가 됨


# ? 두 개의 스택을 사용해 큐를 구현하되, 인큐 동작이 O(1)을 따르도록 만들어보세요


class Queue1:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Cannot pop from empty queue")
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        temp = self.s2.pop()
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
        return temp
