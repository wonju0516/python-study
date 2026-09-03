# linked list
# * 배열과 마찬가지로 앞이나 뒤에 요소를 추가하고 탐색하며, 삭제할 수 있음
# ! 링크드 리스트의 요소에는 인덱스가 없음 -> 연속적인 메모리 블록에 저장 X (비연속적 메모리에 저장 가능)
# ! 링크드의 리스트의 노드는 데이터를 보관하는 필드, 다음 노드의 위치를 나타내는 포인터로 이루어져있다
# ! 첫번째 노드 -> 헤드, 마지막 노드 -> 테일

# * 링크드 리스트는 삽입할 때 다른 데이터를 미뤄낼 필요가 없다
# * 포인터 2개만 수정하면 됨

# * 링크드 리스트의 종류
# ? 단일 링크드 리스트
## * 각 노드에 다음 요소를 가르키는 포인터만 있는 링크드 리스트를 말함

# ? 이중 링크드 리스트
## * 각 노드에 다음 요소를 가르키는 포인터와 이전 요소를 가리키는 포인터가 모두 있는 링크드 리스트를 말함

# ? 환형 링크드 리스트 (Circular linked list)
## * 마지막 노드에 첫 번째 노드를 가리키는 포인터가 있어 마지막 요소에서 처음으로 돌아올 수 있음

# * 링크드 리스트의 시간 복잡도
# ! O(n) -> 접근, 탐색 || O(1) -> 삽입, 삭제


class Node:  # * 클래스는 값과 그 값을 다루는 함수(메서드)까지 같이 묶을 수 있는 것
    def __init__(self, data, next=None):  # * 이 클래스에 있는 함수
        # ! __init__(self) -> 클래스의 객체를 만들 때 필요한 초기 데이터를 설정하고 속성을 부여하기 위해 사용
        # ! -> 직접 호출할 필요 없이, 객체 생성 시점(Node(...))에 파이썬이 알아서 자동으로 실행해줌
        # ! self -> 지금 만들어지는 그 객체 자기 자신을 가리키는 참조
        self.data = data  # ? 이 노드가 담고 있는 실제 값
        self.next = (
            next  # ? 다음 노드를 가리키는 포인터 (기본값 None -> 아직 다음 노드 없음)
        )


class LinkedList:  # * 그 노드들을 서로 연결해서 관리하는 전체 리스트에 대한 설계도
    def __init__(self):
        self.head = None

    # ? 새로운 노드를 추가 할 때 사용하는 함수
    def append(self, data):
        if not self.head:  # * self.head가 None(=리스트가 비어있음)일 때만 실행됨
            self.head = Node(data)  # * 새로운 노드를 헤드로 만들고 리턴
            return
        current = self.head  # * current 변수에 리스트의 헤드를 넣음
        while (
            current.next
        ):  # * current.next가 None이 아닌 동안 계속 반복 -> 리스트 마지막까지 이동
            current = current.next
        current.next = Node(
            data
        )  # * current가 리스트 마지막 요소로 이동했으니 그 next에 넣기

    # ? 노드를 쉽게 출력하는 함수 -> 그냥 이거 없이 출력하면 객체 자체를 출력함
    def __str__(self):  # * 객체를 사람이 읽기 좋은 문자열로 표현하기 위해 사용하는 함수
        # ! 직접 호출할 필요 없이, print(객체) / str(객체) 시점에 파이썬이 알아서 자동으로 실행해줌
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return "end"

    # ? 링크드 리스트의 탐색 함수
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            else:
                current = current.next
        return False

    def remove(self, target):
        if (
            self.head.data == target
        ):  # ? 제거할 노드가 헤드라면? -> self.head는 Node "객체" 자체라서 .data로 꺼낸 실제 값끼리 비교해야 함
            self.head = self.head.next  # ? 헤드를 다음 노드를 할당하고 종료하면 됨
            return
        current = (
            self.head
        )  # ? 그렇지 않으면.. 현재 노드와 이전 노드를 각각 저장해서 구해야함
        previous = None
        while current:  # * 링크드 리스트 순환중
            if current.data == target:  # ? 순환중에 데이터를 찾으면?
                previous.next = (
                    current.next
                )  # * 없앨 데이터의 다음을 이전 데이터의 다음으로 저장
                return  # ! 찾았으면 바로 끝내야 함 (없으면 중복값일 때 여러 개 지워지는 버그 생김)
            previous = (
                current  # ? 못 찾았으니 한 칸 이동: previous를 지금 current 위치로
            )
            current = current.next  # ? current를 그다음 노드로

    # ? 링크드 리스트 뒤집기
    def reverse_list(self):
        current = self.head  # * 현재 노드를 head부터 시작
        previous = None  # * 이전 노드
        while current:
            next = current.next  # * 다음 노드를 미리 next라는 변수에 저장
            current.next = previous  # * current.next를 이전 노드로 방향을 바꿈
            previous = current  # * previous가 current가 됨
            current = next  # * 그리고 미리 저장한 다음 노드값을 current로 옮김 -> 이게 그냥 다음으로 이동한거
        self.head = (
            previous  # * 이 반복문이 끝나면 head는 맨 마지막에 있던 노드가 새로운 head
        )
        # ! current가 아닌 이유 - current가 저 반복문에서 빠져 나온거면 None임!

    # * 링크드 리스트의 사이클 찾기
    ## ! 마지막 요소가 다음 변수의 값이 None이 아니라 리스트의 어떤 요소를 가르키는지를 확인하라는 뜻
    ## ? 토끼와 거북이 알고리즘 -> slow, fast를 두고 fast변수가 만약 slow를 따라잡으면 사이클이 있단 뜻
    def detect_cycle(self):
        slow = self.head  # * 한 칸씩 이동
        fast = self.head  # * 두 칸씩 이동
        while True:
            try:  # * 아래 코드 실행하다 에러나면 except로 넘어감
                slow = slow.next
                fast = fast.next.next
                if (
                    slow is fast
                ):  # ? is는 완전히 같은 객체인지(값 말고), ==는 값이 같은지 -> 같은 노드에서 만난 건지 확인해야 하니 is가 맞음
                    return True
            except (
                AttributeError
            ):  # ! None.next 시도하다 에러 = 끝(None)까지 갔다 = 사이클 없음
                return False


a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")
print(a_list)

# ! deque -> 내부는 연결 리스트라 양쪽 끝 추가/삭제 O(1)로 빠름(리스트는 앞쪽이 O(n))
# ! 근데 이미 __str__ 있어서 print(d)만 해도 내용 잘 보임(우리가 만든 LinkedList와 다른 점)
from collections import deque

d = deque()
d.append("Harry")
d.append("Potter")

for (
    item
) in d:  # ? print(d) 대신 굳이 for문 쓴 이유: 값을 한 줄씩 따로 출력하려고 (없어도 됨)
    print(item)

print(d)  # ? 이렇게 해도 출력은 됨

# * 링크드 리스트의 탐색
## ? append 메서드를 조금 수정하면 링크드 리스트에서 요소를 탐색할 수 있음

# def search(self, target):
#     current = self.head
#     while current.next:
#         if current.data == target:
#             return True
#         else:
#             current = current.next
#     return False

import random

a_list1 = LinkedList()

for i in range(20):  # * 0~19 -> 20개의 숫자
    j = random.randint(1, 30)  # * 1부터 30까지 (끝숫자들 포함) 그 중 랜덤 숫자
    a_list1.append(j)
    print(j, end=" ")

print(a_list1.search(10))

# * 링크드 리스트에서 노드 삭제하기 -> 기술 면접에서 자주 나옴

# def remove(self, target):
#     if self.head.data == target: # ? 제거할 노드가 헤드라면? -> self.head는 Node "객체" 자체라서 .data로 꺼낸 실제 값끼리 비교해야 함
#         self.head = self.head.next # ? 헤드를 다음 노드를 할당하고 종료하면 됨
#         return
#     current = self.head # ? 그렇지 않으면.. 현재 노드와 이전 노드를 각각 저장해서 구해야함
#     previous = None
#     while current: # * 링크드 리스트 순환중
#         if current.data == target: # ? 순환중에 데이터를 찾으면?
#             previous.next = current.next # * 없앨 데이터의 다음을 이전 데이터의 다음으로 저장
#             return # ! 연결을 끊었으면 여기서 끝내야 함 (없으면 불필요하게 계속 순회함)
#         previous = current
#         current = current.next

a_list.remove("Wednesday")
print(a_list)

# * 링크드 리스트 뒤집기
# def reverse_list(self):
#     current = self.head # * 현재 노드를 head부터 시작
#     previous = None # * 이전 노드
#     while current:
#         next = current.next # * 다음 노드를 미리 next라는 변수에 저장
#         current.next = previous # * current.next를 이전 노드로 방향을 바꿈
#         previous = current # * previous가 current가 됨
#         current = next  # * 그리고 미리 저장한 다음 노드값을 current로 옮김 -> 이게 그냥 다음으로 이동한거
#     self.head = previous # * 이 반복문이 끝나면 head는 맨 마지막에 있던 노드가 새로운 head
#     # ! current가 아닌 이유 - current가 저 반복문에서 빠져 나온거면 None임!

# * 링크드 리스트의 사이클 찾기
## ! 마지막 요소가 다음 변수의 값이 None이 아니라 리스트의 어떤 요소를 가르키는지를 확인하라는 뜻
## ? 토끼와 거북이 알고리즘 -> slow, fast를 두고 fast변수가 만약 slow를 따라잡으면 사이클이 있단 뜻
# def detect_cycle(self):
#     slow = self.head # * 한 칸씩 이동
#     fast = self.head # * 두 칸씩 이동
#     while True:
#         try: # * 아래 코드 실행하다 에러나면 except로 넘어감
#             slow = slow.next
#             fast = fast.next.next
#             if slow is fast: # ? is는 완전히 같은 객체인지(값 말고), ==는 값이 같은지 -> 같은 노드에서 만난 건지 확인해야 하니 is가 맞음
#                 return True
#         except AttributeError: # ! None.next 시도하다 에러 = 끝(None)까지 갔다 = 사이클 없음
#             return False


# ? 1부터 100까지의 숫자로 링크드 리스트를 만들고 그 리스트의 노드를 모두 출력해보시오
class Node1:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linkedlist1:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node1(data)
            return
        current = self.head
        while current.next:  # * 이게 끝까지 이동해야 나올 수 있음
            current = current.next
        current.next = Node1(data)

    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        return ""  # ! __str__은 반드시 문자열을 반환해야 함 -> 빈 문자열이라도 넣어야 함 (None 반환하면 에러)

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except AttributeError:
                return False


num_list = Linkedlist1()
for i in range(1, 101):
    num_list.append(i)
print(num_list)

# ? 하나는 사이클이 있고 하나는 없는 두개의 링크드 리스트를 만들어 보세요. 두 리스트에는 모두 사이클을 찾는 detect_cycle이 있어야 함
# ? 그리고 각 리스트에서 detect_cycle을 출력해보시오.

# * 사이클 없는 리스트 -> append()로 정상적으로 만들면 마지막 노드의 next가 자동으로 None
no_cycle_list = Linkedlist1()
no_cycle_list.append("A")
no_cycle_list.append("B")
no_cycle_list.append("C")
print(no_cycle_list.detect_cycle())  # False

# * 사이클 있는 리스트 -> 정상적으로 만든 다음, 마지막 노드의 next를 head로 강제 연결
cycle_list = Linkedlist1()
cycle_list.append("A")
cycle_list.append("B")
cycle_list.append("C")

current = cycle_list.head
while current.next:  # * current.next가 None이 아닌 동안 -> 마지막 노드까지 이동
    current = current.next
current.next = (
    cycle_list.head
)  # ! 마지막 노드("C")의 next를 head("A")로 다시 연결 -> 사이클 발생

print(cycle_list.detect_cycle())  # True
