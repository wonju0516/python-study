# * collections 모듈
# * list/dict/tuple/set만으로 부족한 상황을 위한 특화된 컬렉션 타입 모음 (deque, Counter, defaultdict 등)

# * Counter: 리스트/문자열 안의 각 원소가 몇 번 등장하는지 자동으로 세어주는 딕셔너리 (내부적으로 dict를 상속)
from collections import Counter

lst = [1, 2, 3, 2, 2, 2, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 3]
c = Counter(lst)
print(c)  # * Counter({2: 7, 1: 5, 3: 5}) -> {값: 등장횟수} 형태. 삽입 순서가 아니라 등장 횟수 내림차순으로 보여줌
print(list(c))  # * list()로 감싸면 값(key)들만 뽑힘 -> [1, 2, 3]

c = Counter("Hello")
print(c)  # * 문자열도 한 글자씩 세어줌. 'H'와 'h'는 다른 문자로 취급(대소문자 구분)

sentences = "hello hello hello a wonderful world"
c = Counter(sentences.split())  # * split()으로 먼저 단어 리스트로 쪼갠 뒤 Counter에 넣음 -> 단어별 등장 횟수
print(c)

# * most_common(): 등장 횟수가 많은 순서대로 (원소, 횟수) 튜플 리스트를 반환
print(c.most_common())
print(list(c))

# * defaultdict: 없는 key에 접근해도 KeyError 없이 "기본값 생성 함수"로 자동 채워주는 딕셔너리
# ! 일반 dict는 없는 key에 접근하면 KeyError 발생 (예: d["b"] -> 에러)
from collections import defaultdict

d = {"a": 10}

# * defaultdict(lambda: 0): 없는 key에 접근하는 순간, 그 key에 lambda 결과값(0)을 자동으로 채워 넣음
dd = defaultdict(lambda: 0)
dd["here"] = 10

print(dd["here"])  # 10 -> 직접 넣은 값

dd["there"]  # * 아직 없는 key를 그냥 "읽기"만 해도, 그 순간 자동으로 dd["there"] = 0 이 생성됨
print(dd["there"])  # 0 -> 방금 자동 생성된 기본값

# * namedtuple: 인덱스뿐 아니라 이름으로도 접근 가능한 튜플 -> "필드 이름 있는 작은 클래스" 같은 느낌
from collections import namedtuple

t = (10, 20, 30)
print(t[1])  # * 일반 튜플은 인덱스로만 접근 가능해서, 뭐가 뭔지(나이인지 몸무게인지) 이름만 봐선 알 수 없음

# * namedtuple("타입이름", [필드명, ...]): 이 필드들을 가진 새로운 튜플 "타입"을 만들어줌
Dog = namedtuple("Dog", ["age", "breed", "name"])
print(Dog)  # * <class '__main__.Dog'> -> Dog는 값이 아니라 새로 정의된 클래스(타입) 자체

sammy = Dog(age=5, breed="Husky", name="Sammy")  # * 이 타입으로 실제 인스턴스(튜플) 생성
print(sammy)  # Dog(age=5, breed='Husky', name='Sammy')
print(sammy.age)  # * 이름으로 접근 가능 -> 5
print(sammy[0])  # * 여전히 튜플이라 인덱스로도 접근 가능 -> 5 (age와 동일한 값)


# * deque(더블 엔디드 큐, "덱"이라 읽음): 양쪽 끝(앞/뒤) 모두에서 추가/삭제가 O(1)로 빠른 자료구조
# * 일반 list는 맨 뒤 추가/삭제는 O(1)이지만, 맨 앞 추가/삭제는 나머지 값이 다 밀려서 O(n) -> 앞쪽도 자주 건드릴 때 deque가 유리
from collections import deque

dq = deque([1, 2, 3])
print(dq)  # deque([1, 2, 3])

dq.append(4)  # * 뒤에 추가
dq.appendleft(0)  # * 앞에 추가
print(dq)  # deque([0, 1, 2, 3, 4])

dq.pop()  # * 뒤에서 제거
dq.popleft()  # * 앞에서 제거
print(dq)  # deque([1, 2, 3])

# * maxlen 지정 시, 꽉 찬 상태에서 새 값이 들어오면 반대쪽 값이 자동으로 밀려나감 (원형 큐처럼 동작)
dq_fixed = deque([1, 2, 3], maxlen=3)
dq_fixed.append(4)
print(dq_fixed)  # deque([2, 3, 4], maxlen=3) -> 맨 앞 1이 자동으로 빠짐
