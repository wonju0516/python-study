# graph
# * 그래프에는 방향 그래프, 무방향 그래프, 완전 그래프 등이 있음

# * 인접 리스트 구현
## * 인접 리스트는 정렬되지 않은 리스트의 집합 -> 리스트가 점 하나의 연결 상태를 나타냄

# * 딕셔너리로 표현: 키 = 노드, 값 = 그 노드와 연결된 노드들의 리스트
graph = {
    10: [20, 30],
    20: [10],
    30: [10],
}
print(graph)
print(graph[10])  # * 10과 연결된 노드들만 바로 조회

# * 그래프 만들기
## * 파이썬에서 인접 리스트를 만드는 코드


# ! 그래프에 있는 점 하나를 표현하는 클래스
class Vertex:
    def __init__(self, key):
        self.key = key  # * 점의 키 -> 자기 자신의 이름표
        self.connections = {}  # * 점에 인접한 점들을 저장할 딕셔너리 -> 노드마다 완전히 별개(각자 자기 것만 가짐)

    # * 점을 매개변수로 받고, 호출한 점을 리스트에 추가해 두 점이 연결됨을 나타내고 가중치를 매개변수를 추가로 받을 수 있음
    def add_adj(self, vertex, weight=0):
        self.connections[vertex] = weight

    # * 이 노드 자신에게 인접한 노드들(key)을 가져옴 (딕셔너리에 키값이 그거임)
    def get_connections(self):
        return self.connections.keys()

    # * 인접한 노드의 가중치(value)를 가져옴
    def get_weight(self, vertex):
        return self.connections[vertex]


class Graph:
    def __init__(self):
        self.vertex_dict = {}  # * 각 그래프의 점을 저장할 인스턴스 변수

    # * 매개변수로 받은 키를 사용해 Vertex 인스턴스를 만듬
    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex

    # * key(이름)로 그 Vertex 객체를 찾아서 반환 -> 없으면 None
    def get_vertex(self, key):
        if key in self.vertex_dict:  # * 등록된 이름인지 먼저 확인
            return self.vertex_dict[key]  # * 있으면 그 Vertex 객체(value)를 반환
        return None  # * 없으면 None 반환

    # * f와 t를 연결(에지 생성). 둘 다 없으면 자동으로 Vertex부터 만들어줌
    def add_edge(self, f, t, weight=0):
        if f not in self.vertex_dict:
            self.add_vertex(f)  # * f가 없으면 새로 만들어 등록
        if t not in self.vertex_dict:
            self.add_vertex(t)  # * t가 없으면 새로 만들어 등록
        self.vertex_dict[f].add_adj(self.vertex_dict[t], weight)
        # * f의 Vertex 객체를 찾아서, t의 Vertex 객체와 가중치로 연결하라고 시킴
        # ! f의 connections에만 t가 추가됨(한쪽 방향) -> 무방향으로 쓰려면 반대로도 한 번 더 호출해야 함


# * 데이크스트라 알고리즘
## * 점과 점 사이의 가장 짧은 경로를 찾을 때 사용 -> 이 알고리즘에 핵심은 우선순위 큐 (너비 우선 탐색)

# ! 파이썬으로 데이크스트라 알고리즘을 구현한 알고리즘
## * 시작점에서 출발한 가장 짧은 경로를 포함하는 딕셔너리를 반환
## * 최소힙
import heapq


def dijkstra(graph, starting_vertex):
    # * graph의 key(노드 이름)들을 하나씩 꺼내(vertex) -> {그 이름: 무한대} 항목을 하나씩 쌓음
    # * float("infinity"): "무한대"를 나타내는 숫자값 -> 뭐랑 비교해도 항상 더 큼 (아직 거리를 모른다는 뜻으로 씀)
    # ! 시작점만 0으로 하고 나머지는 무한대로 한다
    distances = {vertex: float("infinity") for vertex in graph}
    distances[starting_vertex] = (
        0  # * 시작점만 0으로 덮어씀 (자기 자신까지 거리는 0이니까)
    )
    pq = [
        (0, starting_vertex)
    ]  # * 우선순위 큐로 사용할 리스트 만듬(시작점과, 시작점거리(0))

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue  # ! while문으로 다시 올라가기!!

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# * 매개변수인 인접리스트
graph = {"A": {"B": 2, "C": 6}, "B": {"D": 5}, "C": {"D": 8}, "D": {}}

dijkstra(graph, "A")
print(dijkstra(graph, "A"))
