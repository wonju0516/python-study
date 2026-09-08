# 파일 & 데이터 처리 (file_data_processing)

## 파일 읽기/쓰기 기초 (`files.py`)

- **`open(파일명, 모드)`**: 파일을 열어서 파일 객체를 반환. 모드 종류
  - `"r"`: read, 읽기 전용 (파일이 없으면 에러)
  - `"a"`: append, 파일 끝에 내용을 덧붙임 (기존 내용은 안 지워짐)
  - `"w"`: write, 덮어쓰기 (기존 내용이 사라짐)
- **`.read()`**: 파일 내용 전체를 문자열로 읽어옴
- **`.write(문자열)`**: 파일에 문자열을 쓰고, **쓴 글자 수(int)를 반환**함
- **`.close()`**: 파일을 닫아서 자원을 반납. 꼭 호출해야 함 — 안 하면 파일이 계속 열린 상태로 남아 자원을 낭비함

## 메모리 관리와 `with`문

- 옛날 언어(C 등)는 메모리를 개발자가 직접 해제해야 했음 — 안 비우면 누수(leak), 너무 일찍 비우면 에러
- 요즘 언어는 GC(Garbage Collector)가 안 쓰는 메모리를 알아서 정리해줌
- **`with open(...) as 변수:`**: 이 블록이 끝나면(에러가 나도!) 파이썬이 자동으로 `.close()`를 실행해줌 — 그래서 `with`를 쓰면 `close()`를 직접 안 적어도 됨

## 실행 위치(작업 디렉토리)와 경로 문제

- `open("파일명")`처럼 파일명만 쓰면, 파이썬은 그걸 **현재 작업 디렉토리(cwd) 기준 상대경로**로 찾음
- VS Code ▶ 버튼으로 실행하면 보통 그 파일이 있는 폴더에서 실행되지만, 터미널에서 다른 위치(예: 프로젝트 루트)에 있는 상태로 실행하면 `FileNotFoundError`가 날 수 있음
- **정석 해결법**: `pathlib.Path`로 "이 파일 기준 경로"를 고정해두면 실행 위치와 상관없이 항상 같은 파일을 찾음
  ```python
  from pathlib import Path

  BASE_DIR = Path(__file__).parent      # 이 파일이 있는 폴더 경로
  readme_path = BASE_DIR / "README.txt" # Path끼리 "/"로 이어붙이면 경로가 합쳐짐 (나눗셈 아님)

  open(readme_path, "r")
  ```
  - `__file__`: "지금 이 파이썬 파일 자신의 경로"가 자동으로 담기는 특수 변수
  - `.parent`: 그 경로에서 파일 이름은 빼고 폴더 경로까지만 잘라냄

## CSV 파일 다루기 (`sample.csv`)

- **`csv` 모듈**: 표준 라이브러리. `csv.reader(파일객체)`로 한 줄씩 리스트(`row`)로 읽어옴 — `row[0]`이 첫 번째 컬럼
- 첫 줄은 보통 헤더(컬럼명)라서, `if row[0] != "country":`처럼 헤더 줄을 걸러내고 처리하는 경우가 많음

## pandas로 CSV 읽기 (`sample.csv`)

- **`pd.read_csv(경로)`**: CSV 파일을 통째로 읽어서 **DataFrame**(표 형태 자료구조)으로 반환
- `데이터프레임["컬럼명"]`: 그 컬럼 하나만 시리즈(Series) 형태로 뽑아냄
- `csv` 모듈은 한 줄씩 직접 다뤄야 하는 반면, pandas는 표 전체를 한 번에 다루고 필터링/집계 같은 데이터 분석 작업에 훨씬 유리함

## DataFrame과 Series (`data_pandas.py`)

- **DataFrame**: pandas의 핵심 자료구조. 2차원 표(행/열) 형태이고, 각 행/열에 이름(라벨)이 붙어있음. 크기를 자유롭게 바꿀 수 있고, 컬럼마다 다른 자료형을 가질 수 있음
- **Series**: DataFrame의 컬럼 하나에 해당하는 자료구조 (`df["컬럼명"]`의 결과 타입). 1차원 배열이고 각 값에 인덱스가 붙음, 같은 컬럼 안 값들은 전부 같은 타입
- **`sum(리스트)` vs `시리즈.sum()`**: `list`/`tuple`은 자기만의 `sum()` 메소드가 없어서 파이썬 내장 함수 `sum()`을 써야 함. pandas의 `Series`는 자체 `.sum()` 메소드를 갖고 있어서 `데이터.메소드()` 형태가 표준
- **`df.컬럼명`**: `df["컬럼명"]`과 동일하게 컬럼에 접근하는 방법. 단, 컬럼명에 공백/특수문자가 있거나 DataFrame의 기존 메소드 이름과 겹치면 이 방식은 안 됨 → 그럴 땐 `df["컬럼명"]`만 가능
- **불리언 인덱싱**: `df[df.컬럼 == 값]`처럼 조건을 넣으면, 그 조건이 True인 행만 걸러서 새 DataFrame을 반환함 (`df.컬럼 == 값` 자체는 행마다 True/False로 이루어진 Series)
- **자주 쓰는 메소드**: `.head(n)`(위에서 n개), `.shape`((행,열) 개수), `.columns`(컬럼명 목록), `.sort_values("컬럼")`(정렬), `.value_counts()`(값별 개수), `.describe()`(통계 요약)
- **`describe()`는 숫자/범주형에 따라 다르게 나옴**: 숫자 컬럼은 평균·표준편차·사분위수, 문자열(범주형) 컬럼은 `count`/`unique`/`top`/`freq`로 나옴. `df.describe(include="object")`를 쓰면 문자열 컬럼들을 한 번에 볼 수 있음

## DataFrame 순회하기 (`iterate_pandas_dataframe.py`)

- **`딕셔너리.items()`**: `(key, value)` 쌍으로 순회. `.items()` 없이 `for x in 딕셔너리`만 하면 key만 나옴
- **`DataFrame.items()`는 딕셔너리랑 다름**: "행"이 아니라 **"컬럼"** 을 하나씩 돎 — `key`는 컬럼명, `value`는 그 컬럼 전체(Series). 컬럼 개수만큼만 반복됨
- **`DataFrame.iterrows()`**: 진짜 "행" 단위로 순회. 반복마다 `(인덱스, 그 행의 Series)`를 돌려줌 — 행 개수만큼 반복됨, 한 행 안의 여러 컬럼 값을 동시에 쓰고 싶을 때 씀
- **`row["컬럼명"]` vs `row.컬럼명`**: 둘 다 되지만, 실무에서는 대괄호 방식을 더 권장함 (컬럼명에 공백/특수문자가 있어도 항상 안전하게 동작하기 때문)

## List/Dictionary Comprehension (`list_comprehension.py`, `dictionary_comprehension.py`)

- **list comprehension(리스트 축약)**: `[표현식 for 변수 in 반복가능한것]` — 반복문으로 새 리스트를 만드는 코드를 한 줄로 줄이는 문법. 표현식은 "결과 리스트에 실제로 넣고 싶은 값"
- **조건 붙이기**: `[표현식 for 변수 in 반복가능한것 if 조건]` — 조건은 원본 값 기준으로 먼저 판단되고, 통과한 것만 표현식이 적용됨 (변환 후 값으로 비교하는 게 아님)
- **문자열도 순회 가능**: 문자열은 iterable이라 `[ch for ch in 문자열]`처럼 한 글자씩 리스트로 만들 수 있음
- **dictionary comprehension**: `{key표현식: value표현식 for (key, value) in 딕셔너리.items() if 조건}` — 원리는 list comprehension과 같고, 대괄호 대신 중괄호에 `key: value` 쌍을 넣는 것만 다름
