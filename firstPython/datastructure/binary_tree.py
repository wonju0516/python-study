# binary tree

# ? 루트 노트 -> 트리의 맨 위에 있는 노드
# ? 자식 노드 -> 그 아래로 연결된 링크드 노드
# ? 부모 노드 -> 하나 이상의 자식 노드를 가짐
# ? 형제 노드 -> 같은 부모 노드를 공유
# ? 리프 노드 -> 자식 노드가 없는 노드
# ? 브랜치 노드 -> 자식 노드가 있는 노드

# * binary tree
## * 각각의 노드가 최대 2개의 자식 노드만 가질 수 있는 트리 자료구조

# * binary search tree
## * 각각의 노드가 최대 2개의 자식 노드만 가질 수 있는 트리 자료구조
## * 왼쪽 자식은 항상 나보다 작고, 오른쪽 자식은 항상 나보다 큼
## ! 동일한 값에 대한 발생 횟수를 추적하기 위해 트리의 노드 객체에 카운드 필드를 추가하여 이 제한을 우회하고 중복값을 처리할 수 있음
## * 탐색이 O(log n)인 이유 -> 비교할 때마다 안 볼 절반을 통째로 버림(트리가 균형 잡혀있을 때만, 한쪽으로 치우치면 최악 O(n))

# ! 이진 트리에는 백트래킹이 많이 쓰인다
# * 백트래킹 -> 선택지를 하나씩 시도, 답이 아니면 되돌아가서 다른 선택 시도 (가지치기)
## * 트리 DFS(재귀로 자식 내려갔다 부모로 돌아오는 것) 구조랑 똑같아서 트리에서 백트래킹이 자주 쓰임


class BinaryTree:
    def __init__(self, value):
        self.key = value  # * 노드 데이터 저장하기
        self.left_child = None  # * 노드의 왼쪽 자식을 추적
        self.right_child = None  # * 노드의 오른쪽 자식을 주척

    def insert_left(self, value):
        # ! insert_left를 여러 번 부르면, 매번 "나중에 넣은 게 self 바로 밑 자리"를 차지함 (맨 끝/맨 아래로 추가되는 게 아님)
        # ! 예: insert_left(5) 후 insert_left(2) -> 1-2-5 순서 (2가 1 바로 밑, 5는 그 밑으로 밀림)
        if self.left_child == None:  # * 왼쪽 자리가 비어있으면
            self.left_child = BinaryTree(
                value
            )  # * 새 노드 만들어서 바로 그 자리에 붙임
        else:  # * 왼쪽에 이미 노드(+그 서브트리)가 있으면
            bin_tree = BinaryTree(
                value
            )  # * 지금 넣으려는 value -> self와 원래 left_child "사이"에 끼워질 새 노드
            bin_tree.left_child = self.left_child  # * 원래 있던 왼쪽 서브트리를 새 노드의 왼쪽으로 옮겨 붙임 (안 그러면 사라짐)
            self.left_child = bin_tree  # * 이제서야 self가 원래 노드 대신 bin_tree(새 노드)를 가리키게 됨 -> 진짜로 트리에 연결됨

    # ! 참고: 일반 이진 트리는 보통 이렇게 안 짜고, 트리 모양을 이미 알고 있는 상태에서 아래처럼 직접 조립함
    # ? root = BinaryTree(1)
    # ? root.left_child = BinaryTree(2)
    # ? root.right_child = BinaryTree(3)
    # ? root.left_child.left_child = BinaryTree(4)
    # ! (BST가 아니라서 "어디에 넣어야 하는지" 규칙이 없음 -> insert_left/right처럼 밀어내는 메서드가 필수는 아님)

    def insert_right(self, value):
        if self.right_child == None:  # * 오른쪽 자리가 비어있으면
            self.right_child = BinaryTree(
                value
            )  # * 새 노드 만들어서 바로 그 자리에 붙임
        else:  # * 오른쪽에 이미 노드(+그 서브트리)가 있으면
            bin_tree = BinaryTree(value)  # * value를 담을 새 노드부터 만듦
            bin_tree.right_child = (
                self.right_child
            )  # * 원래 있던 오른쪽 서브트리를 새 노드의 오른쪽으로 옮겨 붙임
            self.right_child = bin_tree  # * 새 노드를 내 오른쪽 자리에 끼워넣음

    def breadth_first_search(self, n):  # * 우리가 찾고자 하는 데이터 n
        current = [self]  # * 현재 탐색중인 레벨의 노드들을 저장
        next = []  # * 다음 레벨의 노드들을 저장
        while current:
            for node in current:
                if node.key == n:
                    return node
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return False

    # * 이진 트리 뒤집기
    ## ? 이진 노드를 뒤집기 위해서는 모든 노드를 방문하면서 각 노드의 자식을 추적해야 한다
    ## ! BFS 를 활용해 왼쪽과 오른쪽 자식을 각각 추적해 뒤집는 것이다
    def invert(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
            current = next
            next = []


tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.left_child.insert_right(6)
tree.insert_right(5)

# * "root -> 왼쪽 -> 오른쪽" 규칙을 각 노드마다 재귀로 반복 적용 (왼쪽 끝까지 파고들다가 막히면 오른쪽으로)


def preorder(tree):
    if tree:
        print(tree.key)  # * 1. 나 자신 먼저
        preorder(tree.left_child)  # * 2. 왼쪽 서브트리에서 "root -> 왼 -> 오" 다시 반복
        preorder(
            tree.right_child
        )  # * 3. 오른쪽 서브트리에서 "root -> 왼 -> 오" 다시 반복


def postorder(
    tree,
):  # * "왼쪽 -> 오른쪽 -> root" 규칙 (preorder랑 순서만 다르고 재귀 구조는 동일)
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)


def inorder(
    tree,
):  # * "왼쪽 -> root -> 오른쪽" 규칙 (BST면 이 순서로 뽑으면 오름차순 정렬됨)
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)

    ## ! DFS를 활용해 이진 트리를 뒤집어 보세요


def invert_dfs(node):
    if node:
        temp = node.left_child
        node.left_child = node.right_child
        node.right_child = temp
        invert_dfs(node.left_child)
        invert_dfs(node.right_child)
