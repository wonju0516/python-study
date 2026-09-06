# 얕은 복사 (shallow copy) vs 깊은 복사 (deep copy)

# * Assignment Operator(=)
## * 리스트에 `=`로 대입하는 건 복사가 아님 -> 두 변수가 메모리상 같은 리스트 하나를 가리키게 될 뿐
colors = ["red", "blue", "green"]
b = colors  # * 복사가 아니라 b도 colors와 같은 리스트를 가리킴 (같은 이름표 2개)
b.append(
    "white"
)  # ! b를 바꿨을 뿐인데, b와 colors가 가리키는 리스트가 같아서 colors도 같이 바뀜
print(b)
print(colors)

# * shallow copy
## * 얕은 복사(shallow copy)는 새로운 바깥 리스트(껍데기)만 새로 만들고,
## * 그 안에 들어있는 요소(안쪽 리스트/딕셔너리 등)는 원본이랑 같은 걸 그대로 참조함
## ! 그래서 안쪽 요소를 수정하면 원본도 같이 바뀜 -> 완전히 분리하려면 deepcopy() 필요

# * compound object -> 다른 객체에 대한 참조(포인터)를 담고 있는 객체 (리스트, 딕셔너리 등. 숫자/문자열은 해당 안 됨)
## * 리스트 원소로 리스트/딕셔너리 등 compound object를 담고 있을 때만 얕은 복사 문제가 생김

a = [[1, 2], [2, 4]]
b = a[:]
b.append([3, 6])
# * 바깥 리스트(b) 자체에 새 원소 추가 -> a는 영향 없음 (a는 새 껍데기가 아니라 원본 그대로)

print(b)
print(a)

b[0].append(3)  # ! b[0]은 a[0]과 같은 객체를 참조 -> 그 객체를 수정하니 a도 같이 바뀜
print(b)
print(a)

# * deep copy
## * 깊은 복사는 바깥 리스트뿐 아니라, 안의 원소들도 재귀적으로 전부 새 복사본을 만들어서 넣음
## * 그래서 원본과 완전히 분리됨 -> 안쪽을 수정해도 서로 영향 없음

import copy

a1 = [[1, 2], [3, 4]]
b1 = copy.deepcopy(a1)
b1[0].append(5)
print(b1)
print(a1)


# * simple list -> compound가 아님
## * 원소가 숫자처럼 단순 값(atomic)이면 공유할 "안쪽 객체" 자체가 없음
## * 그래서 a[:](얕은 복사)만으로도 완전히 독립적인 복사가 됨 (b를 바꿔도 a는 그대로)
## ! 이건 b = a(assignment)와는 다른 얘기 -> 그건 원소 상관없이 애초에 같은 객체라 무조건 서로 영향을 줌
a = [1, 2, 3, 4]
b = a[:]
b.append(5)
print(a)
print(b)
