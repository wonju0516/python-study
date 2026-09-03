# 리스트 & 반복/함수 (loop_function)

## 리스트 기초 & 코딩테스트용 메서드 (`list_data_structure.py`)

| 메서드/문법 | 하는 일 |
|---|---|
| `리스트[i] = 값` | 인덱스로 값 변경 |
| `.append(값)` | 맨 뒤에 추가 |
| `+=` | 리스트끼리 이어붙이기 |
| `.insert(i, 값)` | 원하는 인덱스에 끼워넣기 |
| `[-1]` | 마지막 요소 (음수 인덱스는 뒤에서부터) |
| `.pop()` / `.pop(i)` | 마지막(또는 지정 인덱스) 삭제 + 그 값을 반환 |
| `len(리스트)` | 길이 |
| `값 in 리스트` | 포함 여부 확인 |
| `리스트[시작:끝]` | 슬라이싱, 끝 인덱스는 미포함 |
| `리스트[::-1]` | 뒤집기 |
| `.count(값)` | 그 값의 개수 |
| `.index(값)` | 그 값이 처음 나오는 위치 |
| `.remove(값)` | 값으로 첫 번째 항목만 삭제 (인덱스 아님) |
| `.extend(리스트)` | 다른 리스트를 뒤에 통째로 붙임 (`+=`와 동일) |
| `.sort()` / `.sort(reverse=True)` | 원본을 오름차순/내림차순 정렬 (반환값 없음) |
| `sorted(리스트)` | 원본은 그대로, 정렬된 새 리스트 반환 |
| `.reverse()` | 원본을 뒤집음 (반환값 없음) |
| `min()` / `max()` / `sum()` | 최솟값 / 최댓값 / 합 |
| `"구분자".join(리스트)` | 문자열 리스트를 하나의 문자열로 합침 |

- `.sort()`/`.reverse()`는 **원본을 직접 바꾸고 반환값이 없음**, `sorted()`는 **원본을 안 건드리고 새 리스트를 반환**함 — 둘을 헷갈리면 원본이 예상과 다르게 바뀌어 있거나, `None`을 리스트인 줄 알고 쓰다가 에러가 남
- `.remove(값)`은 인덱스가 아니라 **값**으로 지우는 것이며, 같은 값이 여러 개면 **가장 앞의 것 하나만** 지움

## 중첩 리스트 (Nested List)

리스트 안에 또 다른 리스트가 요소로 들어있는 것.
```python
alphabets = [["a", "b"], "c"]
print(alphabets[0])     # ['a', 'b'] -> 첫 번째 요소 자체가 리스트
print(alphabets[0][0])  # 'a'        -> 안쪽 리스트의 원소는 인덱스를 두 번 써서 접근
```
`alphabets[["a,b"], "c"]`처럼 대괄호 안에 콤마로 값을 나열하면 **튜플로 인덱싱하는 것**으로 해석되어 `TypeError: list indices must be integers or slices, not tuple`가 남 — 중첩 리스트를 만들 땐 `[[...], ...]`처럼 **대괄호를 겹쳐서** 써야 함.

## for-in vs range() vs enumerate() (`loop.py`)

- `for 값 in 리스트/문자열`: **값 자체**가 필요할 때, 인덱스는 필요 없음
- `for i in range(N)`: **인덱스 번호**가 필요하거나, 값 상관없이 **정해진 횟수**만큼 반복할 때
- `for i, 값 in enumerate(리스트)`: **인덱스와 값이 둘 다** 필요할 때, `range(len(리스트))`보다 깔끔한 방법
- `range(start, stop, step)`: `stop`은 항상 미포함, 인자 1개(`range(N)`)면 `start`가 자동으로 0

## FizzBuzz — 조건 순서 (`fizzbuzz.py`)

조건이 서로 겹칠 수 있으면(예: 15는 3의 배수이면서 5의 배수), **더 좁고 구체적인 조건(동시조건)을 항상 먼저** 검사해야 함. `elif`는 위에서부터 하나 걸리면 그 즉시 멈추기 때문에, 넓은 조건을 먼저 두면 좁은 조건이 걸릴 기회를 가로채 버림.
```python
# ! 틀림: i=15면 "fizz"만 출력되고 "fizzbuzz"까지 도달 못 함
if i % 3 == 0:
    print("fizz")
elif i % 3 == 0 and i % 5 == 0:
    print("fizzbuzz")

# * 맞음: 동시조건(둘 다 만족)을 가장 먼저 체크
if i % 3 == 0 and i % 5 == 0:
    print("fizzbuzz")
elif i % 3 == 0:
    print("fizz")
```

## 랜덤 비밀번호 생성기 (`password_pro.py`)

- `string.ascii_lowercase`/`ascii_uppercase`/`digits`/`punctuation`: 알파벳/숫자/특수문자를 일일이 입력할 필요 없이 미리 제공되는 문자열
- `random.randint(0, len(리스트) - 1)`로 인덱스를 뽑아 `리스트[인덱스]`로 값 꺼내기 — `randint`는 양 끝 **포함**이라 `-1` 없이 `len(리스트)`까지 뽑으면 존재하지 않는 인덱스라 `IndexError`가 남
- `random.choice(리스트)`를 쓰면 인덱스 계산 없이 랜덤 값 하나를 바로 뽑을 수 있어 더 간단함
- `random.shuffle(리스트)`로 완성된 문자 리스트의 순서를 섞음 (원본을 직접 바꿈, 반환값 없음)
- `"".join(리스트)`로 문자 리스트를 하나의 문자열(비밀번호)로 합침
- `[str(i) for i in range(10)]`(리스트 축약): `numbers = []; for i in range(10): numbers.append(str(i))`를 한 줄로 줄인 것
