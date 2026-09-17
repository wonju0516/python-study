# dev_tools

파이썬 개발 도구 학습 기록입니다. (pylint, unittest, timeit, pdb, 정규표현식, virtualenv, f-string, pypi, uv 등)

## pylint

- 코드 스타일/버그 가능성을 정적으로 검사해주는 린터 (실행 없이 코드만 보고 분석)
- 실행 위치 주의: 상대 경로로 지정하므로, 파일이 있는 폴더에서 실행하거나 `pylint 경로/파일명.py`처럼 전체 경로를 줘야 함
  - 엉뚱한 위치에서 실행하면 `No module named 파일명.py (fatal)` 에러 발생 (파일을 못 찾아서 모듈 이름으로 잘못 해석함)

```python
a = 1
b = 2
print(a)
print(B)  # * 정의 안 된 변수 사용 -> E0602
```

```
pylint.py:4:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
pylint.py:5:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
pylint.py:7:6: E0602: Undefined variable 'B' (undefined-variable)

Your code has been rated at 0.00/10
```

- `C0103 (invalid-name)`: 변수명이 명명 규칙(camelCase, UPPER_CASE 등)에 안 맞음
- `E0602 (undefined-variable)`: 정의하지 않은 변수를 사용함
- 점수(`Your code has been rated at X/10`)로 코드 품질을 대략적으로 가늠할 수 있음

## unittest (`unittest_py.py`, `calc.py`)

- 함수/메서드 하나하나가 의도대로 동작하는지 자동으로 검증하는 것
- `calc.py`: 테스트 **대상**이 되는 실제 코드
- `unittest_py.py`: 그 `calc.py`를 **검증하는** 테스트 코드

```python
class TestCalc(unittest.TestCase):  # * TestCase를 상속해야 테스트 클래스로 인식됨
    def test_add(self):  # * 메서드 이름이 test로 시작해야 자동으로 테스트로 인식/실행됨
        result = calc.add(1, 2)
        self.assertEqual(result, 3)  # * assertEqual(실제값, 기대값) -> 다르면 테스트 실패 처리


if __name__ == "__main__":  # ! 이 파일을 직접 실행했을 때만 참 (import해서 쓸 땐 실행 안 됨)
    unittest.main()  # * test로 시작하는 메서드들을 전부 찾아서 자동 실행
```

- 메서드 이름을 `test_`가 아니라 `teest_`처럼 오타 내면, unittest가 이름으로 테스트를 찾기 때문에 그 메서드는 조용히 무시되고 실행조차 안 됨
- 실행: `python3 -m unittest unittest_py.py` 또는 `unittest.main()`이 있으면 `python3 unittest_py.py`로 직접 실행 가능

### `echo $?`

- 리눅스에서 **바로 직전 명령어의 종료 코드(exit code)**를 보여주는 명령어
- `0`이면 성공, `0`이 아니면 실패
- unittest를 실행하면 테스트가 전부 통과했을 때 종료 코드 `0`, 하나라도 실패하면 `0`이 아닌 값을 반환함
- 사람이 로그를 눈으로 읽지 않고도, 스크립트/CI(자동 배포 파이프라인)에서 "테스트 통과 여부"를 자동으로 판단할 때 사용

```bash
python3 -m unittest unittest_py.py
echo $?  # * 방금 실행한 테스트가 통과(0)했는지 실패(0 아님)했는지 확인
```

## timeit (`timeit_py.py`)

- `time.time()`: 코드 실행 전후 시각을 찍어서 그 차이로 걸린 시간을 잼. 간단하지만 한 번만 재는 거라 오차가 있을 수 있음
- `timeit`: 같은 코드를 지정한 횟수만큼 반복 실행해서 훨씬 정확하게 측정함

```python
stmt = """
gen_num1(1000)
"""  # * stmt(statement) -> 실제로 시간을 측정할 대상 코드 (반복 실행될 부분)
setup = """
def gen_num1(num):
    return [str(i) for i in range(num)]
"""  # * setup -> stmt 실행 전에 한 번 준비용으로 실행됨. timeit은 바깥(전역) 스코프에 접근 못 해서, stmt에서 쓸 함수를 여기서 직접 정의해줘야 함
# ! stmt/setup 둘 다 문자열(""" """)로 작성 -> 실제 코드가 아니라 "실행할 코드 텍스트"를 넘기는 것

t = timeit.timeit(stmt=stmt, setup=setup, number=100)  # * number=100 -> stmt를 100번 반복 실행한 총 소요 시간을 반환 (평균 아님)
print(t)
```

- 결과값이 `6.389617919921875e-05`처럼 나오는 건 에러가 아니라 **과학적 표기법**(`6.39 × 10⁻⁵` = `0.0000639`). 값이 작아지면 파이썬이 자동으로 이렇게 표시함
  - 소수점 고정 표기로 보고 싶으면 `f"{t:.6f}"`처럼 포맷팅
- 실무/코테에서 쓰임새가 다름
  - **코딩테스트**: 시간제한 안에 도는지 대충 빠르게 확인하면 되므로 `time`을 많이 씀
  - **실무 성능 비교/벤치마크**: "방법 A vs 방법 B 중 뭐가 더 빠른가"처럼 정확한 평균이 필요할 때 `timeit`(또는 `cProfile` 등 프로파일러)을 씀

## pdb

- **Python DeBugger** — 코드를 실행하다가 원하는 지점에서 멈추고, 그 순간의 변수 값/실행 흐름을 직접 대화형으로 확인할 수 있게 해주는 표준 라이브러리 디버거
- `print()`를 여기저기 넣어보는 것과 달리, 코드를 수정하지 않고도 실행을 멈춘 그 자리에서 원하는 걸 바로 찍어볼 수 있음

```python
import pdb

a = [1, 2, 3]
b = 2


def calc(x, y):
    pdb.set_trace()  # * 이 줄에 도달하면 실행이 멈추고 대화형 디버거 모드로 전환됨
    return x + y


calc(a, b)
```

- `pdb.set_trace()`: 이 줄이 실행되는 순간 프로그램이 멈추고, 터미널이 pdb 명령어를 입력받는 모드로 바뀜 (그 시점의 지역 변수 `x`, `y` 등을 바로 조회 가능)

### 자주 쓰는 명령어

| 명령어 | 기능 |
|---|---|
| `n` (next) | 다음 줄로 이동 (함수 호출은 안 들어가고 통째로 실행) |
| `s` (step) | 다음 줄로 이동하되, 함수 호출이면 그 **안으로** 들어감 |
| `c` (continue) | 다음 브레이크포인트까지(또는 끝까지) 계속 실행 |
| `l` (list) | 현재 위치 주변 코드 보여줌 |
| `p 변수명` (print) | 변수 값 출력 |
| `pp 변수명` (pretty print) | 변수 값을 보기 좋게(들여쓰기 등) 출력 (리스트/딕셔너리 등에 유용) |
| `w` (where) | 현재 호출 스택(어디서 여기까지 왔는지) 보여줌 |
| `q` (quit) | 디버거 종료 |

## 정규표현식 (regex.py)

- **regex** = regular expression(정규표현식)의 줄임말. 문자열 안에서 특정 패턴(규칙)을 가진 부분을 찾거나, 맞는지 검사하거나, 치환할 때 쓰는 문법
- 기본적으로 **대소문자를 구분**함 (`"abc"` 패턴은 `"ABC"`와 매칭 안 됨) → 구분 없이 찾고 싶으면 `re.IGNORECASE` 플래그 필요

```python
import re

matched = re.search("number", txt)  # * 처음 매칭되는 곳 하나만 찾음 (Match 객체 또는 None)
print(matched.span())  # * (9, 15) -> 매칭된 구간의 (시작, 끝) 인덱스

re.findall("number", txt)   # * 매칭되는 걸 전부 문자열 리스트로 반환
re.finditer("number", txt)  # * 매칭되는 걸 전부 Match 객체로 하나씩 순회 (위치 정보 필요할 때)
```

### 특수 시퀀스 (문자 하나를 어떤 종류로 볼지)

| 기호 | 의미 |
|---|---|
| `\d` | digit — 숫자 하나 (`0`~`9`) |
| `\D` | `\d`의 반대 — 숫자가 아닌 문자 하나 |
| `\w` | word character — 문자/숫자/언더스코어(`_`) 하나 (identifier에 쓰일 수 있는 문자) |
| `\W` | `\w`의 반대 — 문자/숫자/`_`가 아닌 문자 하나 |
| `\s` | whitespace — 공백/탭/줄바꿈 하나 |
| `\S` | `\s`의 반대 — 공백이 아닌 문자 하나 |
| `.` | 줄바꿈 제외 아무 문자 하나 |

- 대문자 버전(`\D` `\W` `\S`)은 소문자 버전의 **반대(부정)** 의미

### Quantifiers (앞 패턴이 몇 번 반복되는지)

| 기호 | 의미 |
|---|---|
| `*` | 앞 패턴이 0번 이상 반복 |
| `+` | 앞 패턴이 1번 이상 반복 |
| `?` | 앞 패턴이 0번 또는 1번(있어도 되고 없어도 됨) |
| `{n}` | 앞 패턴이 정확히 n번 반복 |
| `{n,}` | 앞 패턴이 n번 이상 반복 (위 제한 없음) |
| `{n,m}` | 앞 패턴이 n번 이상 m번 이하 반복 |

- 예: `\d+`는 "연속된 숫자 하나 이상" → `"123-1234-1234"`에서 숫자 덩어리만 뽑아낼 때 사용

### 그 외 (위치/구조)

| 기호 | 의미 |
|---|---|
| `^` | 문자열의 시작 |
| `$` | 문자열의 끝 |
| `[]` | 대괄호 안의 문자 중 하나 (예: `[abc]` = a 또는 b 또는 c) |
| `[^]` | 대괄호 맨 앞에 `^`가 오면 반대 의미 — 안의 문자들이 **아닌** 것 하나 (예: `[^!.?]` = `!` `.` `?`가 아닌 문자) |
| `\|` | OR — 왼쪽 또는 오른쪽 패턴 중 매칭 (예: `cat\|dog`, 그룹 안에 쓰면 `(cat\|sat\|hat)`) |
| `()` | 그룹 — 패턴을 하나로 묶어서 반복/추출 단위로 사용 |

- **주의**: `^`는 위치에 따라 의미가 다름 — 패턴 맨 앞(`^\d`)이면 "문자열의 시작", 대괄호 맨 앞(`[^...]`)이면 "부정(반대)"
- `.`도 마찬가지로 대괄호 밖에서는 "아무 문자 하나", 대괄호 안에서는 그냥 **마침표 글자 자체**를 의미함 (특수문자들은 `[]` 안에서 원래 의미를 잃고 리터럴 문자가 되는 경우가 많음)

### `re.compile()`과 그룹(`()`)으로 부분 추출하기

```python
pattern = re.compile(r"(\d{3})-(\d{4})-(\d{4})")  # * 패턴을 미리 컴파일해서 재사용 가능하게 만듦
output = re.search(pattern, txt)
print(output.group(1))  # * 첫 번째 그룹(괄호)에 매칭된 부분만 추출 -> 인덱스는 1부터 시작 (0은 전체 매칭)
```

- `re.compile(패턴)`: 패턴을 미리 만들어두고 여러 번 재사용할 때 씀 (문자열 대신 `re.search(pattern, txt)`처럼 그대로 넘겨도 됨)
- `()`로 감싼 부분은 "그룹"이 되어 `.group(n)`으로 각각 따로 꺼낼 수 있음 — `.group(0)`(또는 `.group()`)은 전체 매칭, `.group(1)`부터 괄호 순서대로 매칭됨

## virtualenv

- 프로젝트마다 **독립된 패키지 설치 공간**을 만들어주는 도구. 프로젝트 A/B가 서로 다른 버전의 패키지가 필요할 때, 전역 환경 하나에 다 깔면 충돌이 날 수 있어서 이걸로 분리함

```bash
python3 -m venv test_venv       # * 현재 python3로 test_venv 폴더에 가상환경 생성
source test_venv/bin/activate   # * 가상환경 활성화 -> 터미널의 python/pip가 이 안의 것으로 바뀜
which python                    # * 가상환경 안 python의 실제 경로 확인 (.../test_venv/bin/python)
```

- **VSCode에 연결하기**: `Cmd+Shift+P` → `Python: Select Interpreter` → `Enter interpreter path`에 위 `which python` 경로를 넣으면, **이 워크스페이스(프로젝트)에 한해서만** 그 가상환경을 기본 인터프리터로 사용함 (코드 자동완성/에러 체크/실행/터미널 전부 적용, 다른 프로젝트엔 영향 없음)
- **`venv` vs `virtualenv` vs `uv`**: `venv`는 표준 라이브러리라 설치 없이 바로 사용 가능 (개인 학습/대부분의 프로젝트엔 이걸로 충분). `virtualenv`는 pip로 따로 설치해야 하는 서드파티 패키지로, `venv`보다 빠르고 옵션이 많음 (레거시 프로젝트에서 종종 사용). `uv`는 Rust로 만들어져 훨씬 빠르고 패키지 설치+가상환경 관리를 한 번에 처리하는 최신 도구 (최근 새 프로젝트에서 많이 채택)

### 현업에서 보통 하는 방식

1. 프로젝트 루트에서 폴더 이름을 관례상 **`.venv`**로 고정해서 생성 (이 이름이어야 VSCode가 자동으로 감지해서 "이거 쓸래?"라고 물어봐 줌)
   ```bash
   python3 -m venv .venv
   ```
2. 터미널(iTerm이든 VSCode 내장이든 상관없음)에서 활성화 후 필요한 패키지 설치
   ```bash
   source .venv/bin/activate
   pip install pandas requests
   ```
3. 설치 상태를 기록해서 공유 가능하게 저장
   ```bash
   pip freeze > requirements.txt
   ```
4. `.gitignore`에 `.venv/`를 추가 → 가상환경 폴더 자체는 커밋하지 않고, `requirements.txt`만 커밋 (다른 사람은 이 파일로 똑같은 환경을 재현)
5. VSCode로 프로젝트를 열면 `.venv`를 자동 감지해서 인터프리터로 쓸지 물어봄 → 수락하면 그 뒤로 계속 그걸로 인식

### 원하는 버전 지정해서 만들기

가상환경 버전은 생성 시점에 쓰인 `python3`의 버전 그대로 고정되므로, 특정 버전으로 만들고 싶으면 그 버전의 python 경로를 직접 지정해서 실행해야 함:
```bash
~/.pyenv/versions/3.11.0/bin/python3 -m venv .venv  # * 3.11.0 버전으로 생성 (먼저 pyenv install 3.11.0 필요)
```

## f-string (`f-string-trick.py`)

### `=` 디버깅 트릭

```python
a = 10
b = 20
print(f"{a=}, {b=}")  # * a=10, b=20 -> "변수명=값" 형태로 자동으로 찍어주는 디버깅용 트릭
```

### 숫자 포맷팅

`{값:형식}`에서 `:` 뒤에 오는 게 **포맷 지정자**. 마지막 글자(타입 지정자)가 핵심이고, 앞의 옵션들은 그 타입에 대한 추가 설정.

```python
num = 100

print(f"num: {num:.2f}")    # * num: 100.00   -> .2 = 소수점 2자리, f(fixed-point) = 소수점 고정 표기 타입 지정자
print(f"hex: {num:#0x}")    # * hex: 0x64     -> x = 16진수 타입 지정자, # = 0x 접두어 자동으로 붙이는 플래그
print(f"binary: {num:b}")   # * binary: 1100100  -> b = 2진수 타입 지정자
print(f"octal: {num:o}")    # * octal: 144    -> o = 8진수 타입 지정자
print(f"scientific: {num:e}")  # * scientific: 1.000000e+02  -> e = 과학적 표기법(지수), 기본 소수점 6자리
print(f"Number:{num:09}")   # * Number:000000100  -> 0 = 빈 자리를 0으로 채움, 9 = 전체 자릿수(폭) 9자리로 맞춤
```

- `0x`/`0b`/`0o`는 f-string 문법이 아니라 "이 숫자는 16/2/8진수다"를 사람이 알아보게 붙이는 **범용 접두어 관례**. `#` 플래그가 이걸 자동으로 붙여주는 것
- `0` 플래그는 **뒤에 전체 자릿수(폭)가 숫자로 같이 와야만** 실제로 작동함 (`#0x`처럼 폭 없이 쓰면 사실상 `#x`랑 결과가 같음, `#06x`처럼 써야 진짜 0 채우기가 됨)

### datetime 포맷팅

```python
import datetime

today = datetime.datetime.now(tz=datetime.timezone.utc)  # * tz 인자에 UTC를 명시적으로 지정

print(f"current : {today}")                        # * 기본 형식 그대로 출력
print(f"current : {today:%m/%d/%Y %H:%M:%S}")       # * 09/16/2026 10:53:28 -> datetime 객체도 : 뒤에 형식 지정자 사용 가능
```

- `datetime.datetime.utcnow()`는 Python 3.12부터 deprecated됨 (naive datetime을 반환해서 timezone 정보가 없음) → `datetime.now(tz=timezone.utc)`를 대신 사용

### `@dataclass`

- `__init__`, `__repr__`, `__eq__` 등을 자동으로 만들어주는 데코레이터 (직접 작성하지 않아도 됨)

```python
from dataclasses import dataclass

@dataclass
class Car:
    brand: str  # * 타입 힌트가 곧 필드 선언 -> 이 두 줄만으로 생성자 인자가 됨
    model: str

    def __str__(self) -> str:  # * __repr__과 별개로, 사람이 보기 좋은 출력 형태를 직접 커스터마이징
        return f"{self.brand} has {self.model}"

model3 = Car("Tesla", "Model 3")  # * __init__ 없이도 바로 생성 가능
print(f"{model3}")  # * Tesla has Model 3
```

## dataclass 심화 (`dataclass_py.py`)

### frozen / order

```python
@dataclass(frozen=True, order=True)
class Car:
    id: int
    color: str = ""
    brand: str = ""
```

- **`frozen`**: 한번 만들면 값을 못 바꾸게 고정(불변). `car1.color = "Red"`처럼 수정하려 하면 에러남
- **`order`**: `<`, `>` 같은 비교 연산자를 쓸 수 있게 해줌 (필드 순서대로 비교)

### 자동 생성되는 함수들 확인하기

```python
import inspect
pprint(inspect.getmembers(Car, inspect.isfunction))  # * 클래스 안에 있는 함수 목록 출력
```
- `inspect.getmembers(대상, 필터함수)`: 대상의 멤버 중 필터를 통과하는 것만 뽑음
- `inspect.isfunction`: "이게 함수냐?"를 판별하는 필터 → `__init__`, `__eq__`, `__lt__` 등 `@dataclass`가 자동 생성한 메소드들이 쭉 나옴

### 변환 / 복사

```python
print(astuple(car1))          # * 튜플로 변환 -> (1, 'White', 'TESLA')
print(asdict(car1))           # * 딕셔너리로 변환 -> {'id': 1, 'color': 'White', 'brand': 'TESLA'}
print(replace(car1, id=3))    # * 불변 객체는 직접 수정 불가 -> 일부 필드만 바뀐 새 복사본 생성
```

### 중첩 (다른 dataclass를 필드로 담기)

```python
@dataclass
class Inventory:
    cars: list[Car]  # * dataclass 필드에 다른 dataclass 객체들도 담을 수 있음
```

### 상속

```python
@dataclass(frozen=True)  # ! 부모(Car)가 frozen이면 자식도 frozen이어야 함 (안 그러면 TypeError)
class Taxi(Car):
    owner_company: str = ""  # * 부모에 없던 필드를 자식에서 추가
```
- 상속 = 부모 클래스의 필드를 그대로 물려받고, 자식에서 필드를 추가로 붙일 수 있음
- 공통 필드(id/color/brand)는 부모(`Car`)에 두고, 자식만의 특징(`owner_company`)만 추가하는 게 전형적인 상속 사용 예

## pip

- 파이썬 **패키지 설치/관리 도구**

```bash
pip install pandas          # * 패키지 하나 설치
pip freeze                  # * 현재 환경에 설치된 패키지 목록을 버전까지 포함해서 출력 (pandas==3.0.5 형태)
pip install -r requirements.txt  # * requirements.txt에 적힌 패키지들을 한 번에 전부 설치
```

- **`requirements.txt`**: "이 프로젝트를 실행하려면 이 패키지들, 이 버전으로 깔아야 함"을 적어둔 파일 — 다른 사람/다른 컴퓨터에서 내 개발 환경을 그대로 재현할 수 있게 공유하는 용도
- 흐름: 개발하며 패키지 설치 → `pip freeze > requirements.txt`(지금 설치 상태를 파일로 저장) → 다른 사람은 가상환경 만들고 `pip install -r requirements.txt` 한 방으로 동일한 패키지/버전 설치

### requirements.txt 형식

한 줄에 패키지 하나씩, `pip freeze`가 만들어주는 형태 그대로 저장하면 됨:

```
pandas==3.0.5
numpy==2.1.0
requests>=2.31.0
```

- `패키지명==버전`: **정확히 이 버전**만 설치 (가장 흔한 형태, 재현성이 가장 확실함)
- `패키지명>=버전`: 이 버전 **이상**이면 설치 허용 (조금 더 유연하게 쓰고 싶을 때)
- 버전 없이 `패키지명`만 쓰면 그냥 최신 버전 설치 (재현성은 떨어짐)

## uv

### 정의

- 파이썬 프로젝트를 관리하는 **하나의 통합 도구**. 지금까지 각각 따로 썼던 이 세 가지 역할을 전부 대신함:
  - `pip` (패키지 설치)
  - `venv` (가상환경 만들기)
  - `pyenv` (파이썬 버전 관리)
- Rust라는 언어로 만들어져서 속도가 매우 빠름

### 왜 쓰는지 (기존 방식과 비교)

**기존 방식**: 도구 3개를 따로따로 배우고 따로따로 실행해야 함
```bash
pyenv install 3.12.0              # 1. 파이썬 버전 설치 (pyenv)
python3 -m venv .venv             # 2. 가상환경 생성 (venv)
source .venv/bin/activate         # 3. 가상환경 활성화
pip install pandas                # 4. 패키지 설치 (pip)
pip freeze > requirements.txt     # 5. 버전 기록 (pip)
```

**uv 방식**: 이 전체 과정이 명령어 2~3개로 줄어듦
```bash
uv init                # 1. 프로젝트 생성 -> 가상환경(.venv)까지 알아서 같이 만들어줌
uv add pandas           # 2. 패키지 설치 -> 버전 기록(uv.lock)까지 자동으로 같이 됨
uv run main.py          # 3. 실행 -> 가상환경 활성화 안 해도 알아서 그 환경으로 실행함
```

- **속도**: 같은 작업 기준 `uv` 0.06s vs `poetry` 0.99s vs `pdm` 1.90s vs `pip-sync` 4.63s → 체감될 정도로 빠름
- **재현성(lockfile)**: `uv.lock` 파일에 "정확히 어떤 패키지가 어떤 버전으로 설치됐는지"가 자동 기록됨 → 다른 사람 컴퓨터에서 `uv sync` 한 번이면 나랑 100% 똑같은 환경이 만들어짐 (예전처럼 `requirements.txt` 직접 관리 안 해도 됨)

### 설치 (OS별)

**macOS**
```bash
brew install uv                                    # * Homebrew로 설치 (둘 중 아무거나 하나만 하면 됨)
curl -LsSf https://astral.sh/uv/install.sh | sh    # * curl로 설치 (Rust나 Python 없어도 설치 가능)
```

**Windows**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
- `powershell`: 윈도우 PowerShell 실행
- `-ExecutionPolicy ByPass`: 윈도우는 기본적으로 보안 때문에 스크립트(.ps1) 실행을 막아놓는데, 이번 실행만 그 제한을 건너뜀(bypass)
- `-c "..."`: 뒤에 오는 문자열을 명령어로 실행
- `irm 주소`: Invoke-RestMethod — 그 주소의 설치 스크립트 내용을 다운로드해서 텍스트로 받아옴
- `| iex`: Invoke-Expression — 받아온 텍스트를 파일로 저장하지 않고 바로 실행
- 전체적으로 mac/리눅스의 `curl ... | sh`(다운로드해서 바로 실행)와 동일한 패턴, 윈도우 버전이라고 보면 됨

**pip로 설치 (OS 무관, 파이썬만 있으면 됨)**
```bash
pip install uv
```

### 주요 명령어

| 명령어 | 기능 |
|---|---|
| `uv init` | 새 프로젝트 초기화 — `.venv/` 생성, `pyproject.toml` 생성, `uv.lock` 생성 |
| `uv run main.py` | 프로젝트의 가상환경으로 스크립트 실행 (`.venv/bin/python main.py`의 단축 명령) |
| `uv add <package>` | 패키지 설치 + `pyproject.toml`/`uv.lock` 자동 갱신 |
| `uv remove <package>` | 패키지 제거 + `pyproject.toml`/`uv.lock` 자동 갱신 |
| `uv sync` | 지금 환경을 `uv.lock` 내용과 정확히 일치시킴 (CI나 환경 복원 시 유용) |
| `uv lock` | `pyproject.toml` 기준으로 `uv.lock`을 재생성 (설치는 안 함, 의존성 변경 반영용) |
| `uv lock --upgrade <package>` | 특정 패키지만 최신 호환 버전으로 업그레이드 (나머지는 그대로 유지) |
| `uv tree` | 의존성 트리 보여줌 (뭐가 왜 설치됐는지 파악할 때 유용) |
| `uv python list` | uv가 관리할 수 있는 파이썬 버전 목록 (pyenv와 비슷하지만 더 빠르고 통합돼 있음) |
| `uv python install 3.12.0` | 파이썬 3.12.0을 로컬에 설치 (이후 프로젝트에서 바로 사용 가능) |
| `uv venv --python 3.12.2` | 지정한 버전으로 가상환경 생성 (시스템 기본 버전 무시하고 지정 가능) |
| `source .venv/bin/activate` | 표준 방식으로 가상환경 활성화 (`uv run`/`uv pip`만 쓸 거면 필수는 아님) |
| `uv build` | 배포용 아티팩트 생성 (`.tar.gz` 소스 배포본 + `.whl` 휠 파일) |
| `uv publish` | 빌드한 패키지를 PyPI(또는 다른 인덱스)에 업로드 |

## logging

### 정의

- 소프트웨어가 실행되는 동안 **발생한 이벤트(사건)를 기록으로 남기는 것**
- `logging`은 파이썬 **표준 모듈**(별도 설치 불필요) — 로그 메시지를 유연하게 내보낼 수 있는 프레임워크를 제공함
- 기록된 로그는 두 가지 방식으로 쓰임:
  - **파일에 기록**(write the logs to the file) — 나중에 확인할 수 있게 저장
  - **화면에 출력**(print the log) — 지금 바로 확인

### 왜 쓰는지 (purpose)

| 목적 | 설명 |
|---|---|
| **Debugging(디버깅)** | 디버그 메시지를 로그로 남기면, 개발자가 코드의 실행 흐름을 파악하고 문제의 원인을 찾아낼 수 있음 |
| **Diagnostic Logging(진단 로깅)** | 애플리케이션 동작과 관련된 이벤트를 기록함. 에러가 발생했을 때, 이 로그들이 "무슨 일이 있었는지"에 대한 단서를 제공함 |
| **Audit Logging(감사 로깅)** | 주요 이벤트와 변경사항의 기록을 남김. 거래(transaction)를 처리하거나 컴플라이언스(규정 준수)를 위해 활동 기록을 유지해야 하는 시스템에서 특히 유용함 |
| **Performance Monitoring(성능 모니터링)** | 시간이 오래 걸리는 작업과 관련된 이벤트를 로깅해서, 애플리케이션의 성능을 추적하는 데 도움을 줌 |
| **Security(보안)** | 각종 요청/행동의 기록을 유지함으로써, 의심스러운 활동을 식별하는 데 도움을 줌 |

- `print()`로도 비슷하게 할 수 있지 않냐고 생각할 수 있는데, `logging`은 위 목적들(디버깅/진단/감사/성능/보안)을 **레벨별로 구분해서 체계적으로** 남길 수 있다는 게 차이점

### 심각도 레벨 (severity levels)

로그는 심각도(중요도) 순서로 레벨이 나뉘어 있음 — **낮은 순 → 높은 순**:

| 레벨 | 의미 |
|---|---|
| `DEBUG` | 문제를 진단하기 위한 용도, **가장 낮은** 심각도 |
| `INFO` | 평범한(정상적인) 동작 메시지 |
| `WARNING` | 예상치 못한 일이 발생했거나, 가까운 미래에 문제가 생길 수 있다는 징후 (예: 디스크 공간 부족) |
| `ERROR` | 심각한 문제 — 이 문제 때문에 소프트웨어가 특정 기능을 수행하지 못한 상태 |
| `CRITICAL` | **가장 높은** 레벨. 애플리케이션 전체가 멈출 수도 있는 매우 심각한 에러 |

- 레벨을 나누는 이유: 상황에 따라 "지금은 ERROR 이상만 보고 싶다"처럼 **필터링**해서 볼 수 있게 하기 위함 (개발 중엔 DEBUG까지 다 보고, 운영 중엔 WARNING 이상만 보는 식)

### 실무에서는 로깅을 어떻게 쓰는지 (How do we use the logging)

- 실제 서비스는 서버 하나가 아니라 **여러 대의 서버/애플리케이션**에서 동시에 로그가 발생함
- 각 서버에 로그가 따로따로 흩어져 있으면 확인하기 어려우므로, 이 로그들을 **한 곳(중앙 서버/클라우드)으로 모아서** 한 사람이 통합해서 볼 수 있게 만듦
- 이렇게 여러 곳의 로그를 모아주는 대표적인 도구들:
  - **Logstash**: 로그를 수집/가공해서 저장소로 보내주는 도구
  - **Fluentd**: 로그 수집기 (여러 소스의 로그를 통합해서 전달)
  - **Beats**: 가벼운 로그/데이터 수집 에이전트 (각 서버에 설치해서 로그를 실시간으로 전송)
- 즉 개별 애플리케이션은 로그를 남기기만 하고, 이런 도구들이 그 로그들을 한곳으로 모아줘서 사람이 중앙에서 모니터링할 수 있게 되는 구조

### 실습 (`learn_logging.py`)

**root logger (기본 로거)** — `logging.debug(...)`처럼 모듈 이름으로 바로 호출하면 자동으로 쓰이는 로거

```python
import logging

logging.basicConfig(  # * 로깅 전체의 기본 설정을 한 번 지정 (보통 파일 맨 위에서 딱 한 번만 호출)
    level=logging.DEBUG,  # * DEBUG 이상 전부 출력 -> "필터 기준선"
    format="%(asctime)s - %(levelname)s - %(message)s",
    # * %(asctime)s = 시각, %(levelname)s = 레벨 이름, %(message)s = 메시지 내용
    # ! %(이름)s 는 옛날 방식(% 포맷팅) 문법, logging 모듈은 지금도 이 문법을 씀
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is an critical message")
```

- `filename="example.log"`를 `basicConfig`에 추가하면 콘솔 대신 **파일에** 로그가 기록됨. 단, 상대 경로라서 **스크립트를 실행한 위치(cwd) 기준**으로 파일이 생김 (어디서 실행하냐에 따라 생기는 위치가 달라짐)

**custom logger (직접 만든 로거)** — root logger를 그대로 쓰지 않고, 이름/설정을 직접 지정한 로거

```python
logger = logging.getLogger(__name__)  # * 이름을 직접 지정 -> root logger와 구분됨 (관례상 __name__ 사용)
logger.debug("This is a debug message")  # * logging.debug(...) 대신 logger.debug(...)로 호출
```

- 여러 모듈이 다 root logger만 쓰면 "어디서 찍힌 로그인지" 구분이 안 됨. custom logger는 이름이 있어서 구분 가능하고, 모듈별로 다른 레벨/설정을 줄 수 있음

**Handler로 세밀하게 제어하기** — `getLogger` + `setLevel` + `Formatter` + `Handler` + `addHandler`

```python
my_logger = logging.getLogger("my_custom_logger")
my_logger.setLevel(logging.DEBUG)  # * 이 로거 자체가 처리할 최소 레벨
my_logger.propagate = False  # ! True(기본값)면 이 로거의 로그가 root logger한테도 전달돼서 중복 출력됨

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# * %(name)s -> 로거 이름도 같이 출력 (Formatter는 로그 출력 형식을 정의, basicConfig의 format=과 같은 역할)

file_handler = logging.FileHandler("custom.log")  # * 로그를 "파일에" 기록하는 담당자
file_handler.setLevel(logging.DEBUG)  # * 파일에는 DEBUG 이상 전부 기록
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()  # * 로그를 "콘솔(화면)에" 출력하는 담당자
console_handler.setLevel(logging.WARNING)  # * 콘솔에는 WARNING 이상만 (덜 시끄럽게)
console_handler.setFormatter(formatter)

my_logger.addHandler(file_handler)     # * 로거에 담당자 등록 (여러 개 등록 가능)
my_logger.addHandler(console_handler)

my_logger.debug("...")     # * 파일에만 기록 (콘솔 레벨보다 낮아서 화면엔 안 뜸)
my_logger.warning("...")   # * 파일 + 콘솔 둘 다 출력
```

- **핵심**: 하나의 로거에 핸들러를 여러 개 붙이면, **핸들러마다 다른 레벨/다른 목적지**로 로그를 보낼 수 있음 (파일엔 자세히 다 남기고, 화면엔 중요한 것만 보여주는 실무 패턴)
- `*.log` 파일들은 실습 중 생기는 로그 파일이라 `.gitignore`에 등록해둠

## python-dotenv

- `.env` 파일에 적어둔 값(API 키, DB 비밀번호 같은 민감한 정보)을 파이썬 코드에서 읽어올 수 있게 해주는 패키지
- **왜 쓰는지**: API 키/비밀번호를 코드에 직접 써놓으면 Git에 올라가서 유출될 수 있음 → 별도 파일(`.env`)로 분리해서 관리

```bash
pip install python-dotenv
```

```
# .env 파일
API_KEY=abc123
```

```python
from dotenv import load_dotenv
import os

load_dotenv()  # * .env 파일을 읽어서 환경변수로 등록
api_key = os.getenv("API_KEY")  # * "abc123"
```

- **`override` 옵션**: `load_dotenv(override=True)`
  - 기본값(`override=False`)은 시스템에 이미 같은 이름의 환경변수가 설정돼 있으면 `.env` 값으로 덮어쓰지 않고 기존 값을 유지함
  - `override=True`로 하면 `.env` 파일 값으로 시스템 환경변수를 **강제로 덮어씀**
  - 보통은 기본값이 안전함 (배포 서버의 실제 값이 로컬 테스트용 `.env` 값으로 실수로 덮어써지는 걸 방지) — `override=True`는 무조건 `.env` 내용을 우선시하고 싶을 때만 명시적으로 사용
- `.env` 파일은 `.gitignore`에 추가해서 **절대 Git에 커밋하지 않음**
- 대신 `.env.example` 같은 파일에 "이런 키가 필요하다"는 구조만 남겨서 공유하는 게 관례
