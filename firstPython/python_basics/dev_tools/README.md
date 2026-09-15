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
- **버전은 자동으로 안 맞춰짐**: 가상환경의 파이썬 버전은 `python3 -m venv`를 실행할 때 **그 시점에 쓰인 `python3`의 버전 그대로 고정**됨
  - 다른 버전으로 만들고 싶으면 그 버전의 python 경로를 직접 지정해서 실행해야 함
    ```bash
    ~/.pyenv/versions/3.11.0/bin/python3 -m venv test_venv  # * 3.11.0 버전으로 가상환경 생성 (먼저 pyenv install 3.11.0 필요)
    ```
- **`venv` vs `virtualenv` vs `uv`**: `venv`는 표준 라이브러리라 설치 없이 바로 사용 가능 (개인 학습/대부분의 프로젝트엔 이걸로 충분). `virtualenv`는 pip로 따로 설치해야 하는 서드파티 패키지로, `venv`보다 빠르고 옵션이 많음 (레거시 프로젝트에서 종종 사용). `uv`는 Rust로 만들어져 훨씬 빠르고 패키지 설치+가상환경 관리를 한 번에 처리하는 최신 도구 (최근 새 프로젝트에서 많이 채택)

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
