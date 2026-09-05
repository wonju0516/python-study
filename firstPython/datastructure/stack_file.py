# stack

# * 추상 데이터 타입 (ADT) -> 이런 기능을 제공해야 한다는 개념적인 명세

# * 자료구조 -> ADT를 실제로 메모리에 어떻게 담아서 구현할 것인지에 대한 구체적인 방법

## * push, pop -> O(1)


# ! 스택 만들기
## * 1. Stack 클래스 만들기
### ? 배열을 사용해 내부적으로 데이터를 관리

class Stack1:
    def __init__(self): # * 초기화 -> 이 빈 리스트가 스택의 요소를 관리함
        self.items = []

    def push(self, data):
        # * 스택 규칙: push/pop은 O(1)
        # * 배열은 맨 뒤 append가 O(1)이라 뒤를 top으로 씀
        # * 앞에 넣으면 기존 원소를 전부 밀어야 해서 O(n)
        self.items.append(data)

    def pop(self): # * pop을 사용해 가장 최근이 추가된 요소를 반환 (제거까지)
        return self.items.pop() # ! 리스트 pop()은 제거 + 제거된 값 반환을 동시에 함

    def size(self): # * len을 사용해 스택의 길이를 반환
        return len(self.items)

    def is_empty(self): # * 메서드가 비워있는지 확인
        return len(self.items) == 0 # ? ==0 자체가 이미 True/False라서 if 없이 바로 반환 가능

    def peek(self): # * 스택의 마지막, 가장 최근에 추가된 요소를 반환
        return self.items[-1]

### ? 링크드 리스트를 이용해 Stack 클래스를 만들 수 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack2:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            # * 스택 규칙: push/pop은 O(1)
            # * 이 구현은 head만 들고 있어서, 뒤에 붙이려면 끝까지 순회해야 함 -> O(n)
            # * 그래서 앞에(head) 붙임. 포인터만 바꾸면 O(1)
            node.next = self.head # * 새 노드가 기존 head를 가리키게 연결
            self.head = node # ! head 이름표를 새 노드로 옮김 (head는 하나뿐, 늘어나는 거 아님)

    def pop(self):
        # * 스택에서 지운다 = 노드를 delete하는 게 아니라, head 연결만 끊는 것
        # * head가 더 이상 안 가리키면 그 노드는 스택에서 빠진 거
        # * 함수가 끝나면 아무도 안 가리켜서 Python이 메모리를 수거함
        if self.head is None:
            raise IndexError('pop from empty stack')
        poppednode = self.head # * 지금 top을 잠시 잡아둠 (값 꺼내려고)
        self.head = self.head.next # ! head를 다음으로 옮김 = 스택 줄에서 끊김 = 제거
        return poppednode.data # * 끊긴 노드 안의 값만 반환 (노드 자체를 돌려주는 거 아님)  

stack = Stack2()
stack.push(1)
stack.push(2)
stack.push(3)

for i in range(3):
    print(stack.pop())

### ! 실제로는 파이썬 리스트를 이용해 스택을 만든다 (보통은 이리 사용함)
stack1 = []
print(stack1)
stack1.append('Kayne West')
print(stack1)
stack1.append('Jay-Z')
print(stack1)
stack1.append('Chance the Rapper')
print(stack1)
stack1.pop()
print(stack1)

# * append -> 리스트의 마지막에 요소를 추가하므로 스택의 푸시와 같음
# * poop -> 리스트에서 요소를 제거하며, 지정하지 낳으면 마지막 요소를 제거


# ! 문자열 뒤집기

## * 1
a_string = "a_string"
print(a_string[::-1])
## * [start:stop:step]
### * start: 어디서부터(생략시 처음), stop: 어디까지(생략시 끝, 그 인덱스는 미포함), step: 몇 칸씩 이동(생략시 1)
### * step이 음수(-1)면 방향이 거꾸로 되고 start/stop 기본값도 끝/처음으로 뒤바뀜 -> 그래서 [::-1]이 전체를 뒤집은 결과가 됨

## * 2
print("".join(reversed(a_string)))

## * 3. 스택을 사용하면 마지막에 추가한 요소를 가장 먼저 꺼낼 수 있으므로 쉽게 문자열을 뒤집을 수 있음
def reverse_string(a_string):
    stack = []
    string = ""
    for c in a_string:
        stack.append(c)

    # ! 저 반복문은 stack = list(a_string) 으로 해도 됨
    
    for c in a_string:
        string += stack.pop()
    return string

print(reverse_string(a_string))

# ! 최소 스택
## ? 가장 작은 요소를 반환하는 메서드를 가진 자료구조 (일반 스택 기능에 더해서 가장 작은 값이 뭐야 -> O(1)로 알려주는 스택)

class MinStack:
    def __init__(self):
        self.main = [] # * 메인 스택 (푸시와 팝 동작을 지원)
        self.min = [] # * 최소 스택
        # ! min은 "최솟값만" 걸러 담는 게 아니라, main과 항상 같은 개수(높이)를 유지함
        # ! min[i] = main을 i번째까지 넣었을 때의 최솟값 (그래서 값이 중복돼서 쌓일 수 있음)
        # ! 개수가 어긋나면 pop할 때 main/min이 서로 다른 시점끼리 짝지어져 최솟값이 틀어짐

    def push(self, n):
        if len(self.main) == 0:
            self.min.append(n)
        elif n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])
        self.main.append(n)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return self.min[-1]

min_stack = MinStack()
min_stack.push(10)
min_stack.push(15)
print(min_stack.main)
print(min_stack.min)
print(min_stack.get_min())

min_stack.pop()
print(min_stack.main)
print(min_stack.min)
print(min_stack.get_min())

# * 스택과 괄호
## ? 문자열에 들어있는 괄호의 짝이 맞는지 확인해보세요 -> 여는 괄호가 있으면 닫는 괄호도 있어야한다

pairs = {")": "(", "}": "{", "]": "["} 
# ! key는 "닫는 괄호" -> 170번줄 pairs[c]에서 c(닫는 괄호)로 찾으니까 key 방향을 맞춰야 함 (반대로 하면 KeyError)

def check_parentheses(a_string):
    stack = []
    for c in a_string:
        if c in "({[":
            stack.append(c) # * 여는 괄호 -> 1개 push (한 글자당 한 번씩만 동작)
        elif c in ")}]":
            if len(stack) == 0:
                return False # ! 닫을 상대가 없음 -> 즉시 실패
            if stack.pop() != pairs[c]: # * 방금 뺀 여는 괄호가 이 닫는 괄호의 짝이 아니면
                return False # ! 종류가 안 맞음 -> 실패
    return len(stack) == 0


# * maxstack 구현
class MaxStack:
    def __init__(self):
        self.main = []
        self.max = []

    def push(self, n):
        if len(self.main) == 0:
            self.max.append(n)
        elif n >= self.max[-1]: # ! MinStack의 <=를 그대로 복사해오면 안 됨, Max는 >=여야 함
            self.max.append(n)
        else:
            self.max.append(self.max[-1])
        self.main.append(n)

    def pop(self):
        self.max.pop()
        return self.main.pop()

    def get_max(self):
        return self.max[-1]

max_stack = MaxStack()
max_stack.push(5)
max_stack.push(8)
max_stack.push(2)
print(max_stack.main)
print(max_stack.max)
print(max_stack.get_max())

max_stack.pop()
print(max_stack.main)
print(max_stack.max)
print(max_stack.get_max())

    