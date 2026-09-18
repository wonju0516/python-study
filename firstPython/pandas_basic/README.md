# pandas_basic

pandas / numpy 공부 기록입니다.

## numpy 배열이란? (`numpy_basic.ipynb`)

**numpy 배열**(`np.array`)은 파이썬 기본 `list`랑 비슷해 보이지만, 내부적으로 다르게 동작하는 별도의 자료구조.

```python
import numpy as np

lst = [1, 2, 3, 4, 5]  # * 그냥 파이썬 기본 리스트
a = np.array(lst)       # * np.array()로 감싸서 리스트 -> numpy 배열로 변환
```

### 왜 리스트 대신 numpy 배열을 쓰는지

| | 파이썬 리스트 | numpy 배열 |
|---|---|---|
| 타입 | 섞어서 담을 수 있음 (`[1, "two", 3.0]`) | 모든 원소가 같은 타입으로 통일됨 |
| `+` 연산 | 이어붙이기 (`[1,2,3] + [10]` → `[1,2,3,10]`) | 각 원소마다 계산 (`arr + 10` → 각 원소에 10을 더함) |
| 반복 연산 | 반복문/comprehension 필요 (`[x*2 for x in lst]`) | 반복문 없이 한 번에 (`arr * 2`) — **벡터화 연산** |
| 다차원 구조 | 리스트 안에 리스트로 억지로 흉내 | `shape` 기반의 진짜 다차원 구조를 기본 지원 |
| 속도/메모리 | 원소마다 흩어진 파이썬 객체 | 메모리에 연속된 블록으로 저장 → 훨씬 빠르고 가벼움 |

**정리**: 숫자 여러 개를 담는 그릇이라는 점은 같지만, numpy 배열은 **수학 연산에 최적화된 자료구조**라서 데이터 분석/과학 계산에서는 리스트 대신 거의 항상 numpy 배열을 씀.

### 배열 만드는 여러 방법

```python
a = np.array([1, 2, 3, 4, 5])      # * 리스트를 그대로 배열로 변환

b = [[1, 2, 3], [4, 5, 6]]          # ! 이것도 그냥 파이썬 리스트(중첩) -> 아직 numpy 아님
np.array(b)                          # ! b = np.array(b)로 재대입 안 하면 b 자체는 안 바뀜, 변환 결과만 화면에 보여줌

np.zeros((2, 3))   # * 지정한 shape 크기만큼 전부 0으로 채운 새 배열 생성
np.ones((2, 2))    # * 지정한 shape 크기만큼 전부 1로 채운 새 배열 생성
np.empty((2, 3))   # * shape 크기만큼 배열은 만들지만 값을 초기화하지 않음 (메모리에 있던 값 그대로) -> zeros/ones보다 빠르지만 값 예측 불가
```

- `np.empty(2, 3)`처럼 괄호 없이 쓰면 두 번째 인자(3)가 shape이 아니라 dtype(자료형) 인자로 잘못 해석돼서 에러남 (`Cannot interpret '3' as a data type`) → shape은 반드시 `(2, 3)`처럼 튜플로 감싸서 넣어야 함

### 배열 모양 바꾸기 / 순서열 만들기

| 함수 | 뜻 |
|---|---|
| `np.arange(start, stop, step)` | `range()`의 numpy 버전, `stop` 직전까지 |
| `np.linspace(start, stop, num)` | "간격"이 아니라 "몇 개로 균등하게 나눌지" 지정 |
| `np.eye(n)` | 단위행렬(identity matrix) — 대각선만 1, 나머지 0 |
| `np.reshape(arr, shape)` | 원소 개수는 유지한 채 shape만 변경 |

```python
np.arange(0, 20, 2)      # * [0 2 4 ... 18]
np.linspace(0, 5, 10)    # * 0~5 사이를 10개로 균등 분할
np.eye(4)                 # * 4x4 단위행렬
np.reshape(arr, (3, 4))   # * arr을 3행 4열로 (원소 12개는 그대로)
```

## 뷰(view) vs 복사(copy)

numpy 슬라이싱은 파이썬 리스트와 다르게 **복사본이 아니라 뷰(view)** — 원본이랑 같은 메모리를 공유함. 그래서 뷰를 통해 값을 바꾸면 원본도 같이 바뀜.

```python
a = np.array([1, 2, 3, 4, 5])
a1 = a[:1]          # * 뷰 -> a랑 메모리 공유 (복사 아님)
a1[0] = 10
print(a)             # * [10 2 3 4 5] -> a도 같이 바뀜

b = a.copy()         # * 복사본 -> 메모리를 따로 분리
b[0] = 11
print(a)             # * [10 2 3 4 5] -> a는 그대로 (b만 바뀜)
```

## 브로드캐스팅 (Broadcasting)

### 0. 먼저 `shape`이 뭔지부터

`shape`은 **"이 배열이 몇 차원이고, 각 차원에 숫자가 몇 개 있는지"**를 튜플로 보여줌. **튜플 안에 숫자가 몇 개 있는지 = 몇 차원인지**를 뜻함.

```python
b = np.array([10, 20, 30])
print(b.shape)  # (3,)  <- 숫자가 1개 -> 1차원 -> 그냥 "원소 3개짜리 한 줄"
```
```
b = [10, 20, 30]   <- 표(행렬)가 아니라 그냥 일렬로 늘어선 데이터 3개
```
1차원 배열은 "1행" "1열" 같은 게 아니라, **애초에 행/열 개념 자체가 없음.** 그냥 "숫자가 3개 있다"는 뜻일 뿐.

```python
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a.shape)  # (4, 3)  <- 숫자가 2개 -> 2차원 -> 이제서야 (행, 열)로 읽음 -> 4행 3열
```
```
[1, 2, 3]     <- 1행
[4, 5, 6]     <- 2행
[7, 8, 9]     <- 3행
[10,11,12]    <- 4행
```
**행/열이라는 말은 2차원(숫자가 2개인 shape)부터** 쓸 수 있는 말이고, `(4, 3)`에서 **앞자리(4) = 행 개수, 뒷자리(3) = 열 개수**.

### 1. 왜 "뒤에서부터" 비교하는지

`b`(1차원, 그냥 3개짜리 줄)를 `a`(2차원 표)에 더하고 싶을 때, numpy는 `b` 한 줄을 **`a`의 모든 행 위에 겹쳐서 반복**하는 방식으로 계산함:

```
a = [1, 2, 3]      b = [10, 20, 30]  <- 이 한 줄이
    [4, 5, 6]                          a의 모든 행에 반복해서 깔림
    [7, 8, 9]
    [10,11,12]
```

이게 되려면 `b`의 원소 개수(3)가 `a`의 **열 개수**(=한 행에 몇 칸 있는지, 3)랑 똑같아야 딱 겹쳐짐. 그래서 `a`의 **맨 뒤 숫자(열 개수)**랑 `b`의 숫자를 비교하는 것 — 이게 "뒤에서부터 비교한다"는 말의 진짜 의미. `a`의 앞자리(행 개수, 4)는 `b` 한 줄이 몇 번이고 그대로 반복되기만 하면 되니까 비교할 필요가 없음(자동으로 다 맞음).

### 한 줄 정의

**크기(shape)가 다른 배열끼리 연산할 때, numpy가 작은 쪽을 자동으로 "늘려서" 크기를 맞춰주는 것.**

```python
a = np.array([1, 2, 3])  # * 3개짜리
print(a + 10)             # * [11 12 13]
```

`10`은 숫자 하나인데, `a`는 3개짜리라서 원래대로면 크기가 안 맞아 에러나야 함. 근데 numpy가 `10`을 `[10, 10, 10]`인 것처럼 취급해서 계산해줌 — 이게 브로드캐스팅.

```
a  =  1   2   3
10 = 10  10  10   <- numpy가 속여서(?) 늘림
결과=  11  12  13
```

### 판단 규칙 — "맨 뒤 자리부터" 비교

두 배열의 shape을 **뒤에서부터(끝자리부터)** 한 자리씩 비교해서, 각 자리가 다음 중 하나면 통과:
- 두 숫자가 **같다**
- 둘 중 하나가 **1**이다
- 한쪽에 그 자리가 **아예 없다** (짧은 쪽은 그 자리가 자동으로 1인 것처럼 취급됨)

**모든 자리가 다 통과해야** 성공. 한 자리라도 실패하면 그 즉시 에러.

### 실제 예시로 비교

| a shape | b shape | 맨 뒤 자리 비교 | 결과 |
|---|---|---|---|
| `(4, 3)` | `(3,)` | `3` vs `3` → 같음 | ✅ 성공 |
| `(4, 3)` | `(4,)` | `3` vs `4` → 다르고 1도 아님 | ❌ 실패 |
| `(4, 1)` | `(3,)` | `1` vs `3` → 1이 있음 | ✅ 성공 (양쪽 다 늘어나서 결과는 `(4,3)`) |

```python
# * (4,3) vs (3,) -> 성공 (b가 각 행에 복제되어 더해짐)
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])  # shape (4,3)
b = np.array([100, 200, 300])                          # shape (3,)
a + b  # OK

# * (4,3) vs (4,) -> 실패
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])  # shape (4,3)
b = np.array([100, 200, 300, 400])                     # shape (4,)
a + b  # ValueError: operands could not be broadcast together with shapes (4,3) (4,)

# * (4,1) vs (3,) -> 성공, 양쪽 다 늘어남 -> 결과 (4,3)
a = np.array([[1],[2],[3],[4]])  # shape (4,1)
b = np.array([10, 20, 30])        # shape (3,)
a + b
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]
#  [14 24 34]]
```

### 헷갈리기 쉬운 포인트

**"숫자가 어딘가에 같은 게 있냐"가 아니라, "맨 뒤 자리끼리 비교했을 때 뭐냐"만 본다.**

- `(4, 3)` vs `(4,)`가 실패하는 이유: `b`의 `4`가 **맨 뒤 자리**에 있어서 `a`의 맨 뒤(`3`)랑 직접 비교됨 → 3과 4는 같지도 않고 1도 아님 → 실패
- `(4, 1)` vs `(3,)`가 성공하는 이유: `b`의 `3`이 **맨 뒤 자리**에 있어서 `a`의 맨 뒤(`1`)랑 비교됨 → `a` 쪽이 1이라 성공. `a`의 `4`는 `b`한테 대응하는 자리가 아예 없어서 비교 대상조차 아님 (그냥 1로 취급되고 넘어감)

즉 `4`라는 숫자가 두 shape 어딘가에 같이 등장하는지는 전혀 상관없고, **오직 "맨 뒤 자리"에 뭐가 있는지**만 비교합니다.

## 조건으로 배열 필터링 (Boolean Indexing)

배열에 조건을 걸면 각 원소마다 검사한 **True/False로 이루어진 배열**이 나오고, 그 배열로 원하는 원소만 뽑아낼 수 있음.

```python
arr = np.array([0,1,2,3,4,5,6,7,8,9])
condition = arr > 5         # * [False ... True True True True]
filtered = arr[condition]   # * True인 자리만 뽑힘 -> [6 7 8 9]
```

## 자주 쓰는 numpy 함수

`arr = np.array([1, 2, 3, 4])` 기준

### 수학 함수 — 배열의 각 원소마다 적용

| 함수 | 뜻 |
|---|---|
| `np.sin(arr)` | 각 원소를 사인(삼각함수) 계산 |
| `np.cos(arr)` | 각 원소를 코사인 계산 |
| `np.log(arr)` | 각 원소를 자연로그(밑 e) 계산 |
| `np.exp(arr)` | 각 원소를 e(자연상수)의 거듭제곱으로 계산 (`e^x`) |

- 파이썬 기본 `math.sin()`은 숫자 하나만 되지만, `np.sin()`은 배열 전체에 반복문 없이 한 번에 적용됨 (**벡터화 연산** — 반복문보다 훨씬 빠름)
- `np.log`와 `np.exp`는 서로 역함수 관계

### 집계 함수 — 배열 전체를 하나의 값으로 요약

| 함수 | 뜻 | 결과(`[1,2,3,4]` 기준) |
|---|---|---|
| `np.sum(arr)` | 전체 합 | `10` |
| `np.prod(arr)` | 전체 곱 | `24` |
| `np.min(arr)` | 최솟값 | `1` |
| `np.max(arr)` | 최댓값 | `4` |
| `np.mean(arr)` | 평균 | `2.5` |
| `np.median(arr)` | 중앙값 | `2.5` |
| `np.std(arr)` | 표준편차 (데이터가 평균에서 얼마나 퍼져있는지) | `1.118...` |
| `np.var(arr)` | 분산 (표준편차의 제곱) | `1.25` |

### 누적 함수 — 중간 과정을 배열로 남김

| 함수 | 뜻 | 결과(`[1,2,3,4]` 기준) |
|---|---|---|
| `np.cumsum(arr)` | 누적 합 (cumulative sum) | `[1, 3, 6, 10]` |
| `np.cumprod(arr)` | 누적 곱 (cumulative product) | `[1, 2, 6, 24]` |

- `sum`/`prod`는 결과가 **숫자 하나**(최종 결과만), `cumsum`/`cumprod`는 결과가 **배열**(단계별 중간 결과를 다 남김)
- 예: `cumsum`의 `[1, 3, 6, 10]`은 "1까지 합", "1+2까지 합", "1+2+3까지 합", "1+2+3+4까지 합"을 순서대로 보여줌
- 활용 예: "시간에 따른 누적 매출/누적 방문자 수" 계산할 때 자주 씀

### 배열 메서드로 쓰는 집계 (`arr.max()`처럼 직접 호출)

| 메서드 | 뜻 |
|---|---|
| `arr.max()` | 최댓값 |
| `arr.min()` | 최솟값 |
| `arr.argmax()` | 최댓값 **자체가 아니라**, 최댓값이 있는 위치(인덱스) |
| `arr.argmin()` | 최솟값이 있는 위치(인덱스) |
| `arr.dtype` | 배열 원소들의 자료형 확인 |

### `axis`로 방향 지정하기

2차원 배열(`shape = (행, 열)`)에서 `axis`는 "어느 방향을 따라 계산해서 압축할지"를 가리킴. 계산에 쓰인 축은 결과에서 사라짐.

```python
arr = np.array([[1,2,3],[4,5,6]])   # shape (2, 3)

np.prod(arr, axis=1)  # * 행 방향 -> 행끼리 계산 -> [1*2*3, 4*5*6] = [6, 120]
np.prod(arr, axis=0)  # * 열 방향 -> 열끼리 계산 -> [1*4, 2*5, 3*6] = [4, 10, 18]
```

- `axis=0` → **세로(열) 한 줄끼리** 계산 (`1,4` / `2,5` / `3,6`)
- `axis=1` → **가로(행) 한 줄끼리** 계산 (`1,2,3` / `4,5,6`)

## pandas DataFrame / Series (`pandas_intro.ipynb`)

### DataFrame vs Series

| | Series | DataFrame |
|---|---|---|
| 차원 | 1차원 | 2차원 (행 x 열) |
| 구조 | 인덱스(index) + 값(values)로 이루어진 하나의 열 | 여러 Series(열)들이 모인 표 |
| 인덱스 | `index`만 있음 | `index`(행) + `columns`(열 이름) 둘 다 있음 |
| dtype | 전체가 **하나의 dtype**으로 통일 | **열마다 서로 다른 dtype** 가능 |

```python
df["컬럼명"]        # * DataFrame에서 열 하나만 뽑으면 결과 타입은 Series
type(df["컬럼명"])   # <class 'pandas.core.series.Series'>
```

**핵심**: DataFrame의 열(column) 하나하나가 사실 Series. 그래서 열 하나만 뽑으면 자동으로 Series 타입이 됨.

### 열(column) 추가 vs 인덱스(index) — 헷갈리기 쉬운 포인트

- **인덱스(index)** = 행(row)에 붙는 이름표 (기본값은 `0, 1, 2, 3, ...`)
- **열(column)** = `Name`, `Age`처럼 세로줄 하나하나의 이름
- `df['새이름'] = [값들]`은 **열을 추가/수정**하는 문법이지, 인덱스랑은 무관함 (인덱스를 바꾸려면 `df.index = [...]`나 `df.set_index(...)`를 따로 써야 함)

```python
df['Experience'] = [2, 5, 8, 10, 12]  # * 없는 열 이름이면 새 열 추가, 리스트 길이는 행 개수랑 같아야 함
```

### 조건으로 행 필터링 (Boolean Indexing)

```python
older_than_30 = df[df['Age'] > 30]  # * Age가 30 초과인 행만 남김
```

### `groupby` — 그룹별로 묶어서 집계

```python
df.groupby('City').mean(numeric_only=True)
```

- `numeric_only=True` 필요 → `Name`처럼 문자열 열이 섞여 있으면 평균 계산 시 `TypeError`남 (숫자 열만 계산하도록 명시해야 함)
- 그룹 기준을 **2개 이상** 쓰려면 **리스트로 묶어야** 함 — 콤마로 나열하면 에러

```python
df.groupby('City', 'Age')          # ! ValueError
df.groupby(['City', 'Age']).mean(numeric_only=True)  # * OK -> City+Age 조합별로 그룹핑
```

## pandas Series (`series.ipynb`)

### Series란

공식 정의: **"one dimensional labeled array"** — 1차원이면서 각 값마다 라벨(인덱스)이 붙은 배열.

- numpy 배열은 위치가 그냥 `0, 1, 2...`로 자동 매겨지고 라벨이 없음
- Series는 그 위치에 원하는 이름(라벨)을 직접 붙일 수 있음 (`index` 파라미터)

```python
data = [10, 20, 30, 40, 50]
pd.Series(data)                                   # * 인덱스 안 주면 기본값 0,1,2... 자동 부여

pd.Series(data, index=['A','B','C','D','E'])       # * 인덱스(라벨) 직접 지정
```

### 딕셔너리로 Series 만들기

```python
city_population_data = {"tokyo": 37000000, "seoul": 9700000, "beijing": 21000000}
pd.Series(city_population_data)  # * key -> 인덱스, value -> 값
```

### Series끼리 연산 — index alignment

Series끼리 연산하면 **같은 인덱스끼리 자동으로 짝지어서** 계산됨. 한쪽에만 있는 인덱스는 상대쪽 값이 없어서 결과가 `NaN`.

```python
s1 = pd.Series({"a": 1, "b": 2})
s2 = pd.Series({"a": 10, "b": 5, "c": 5})

s1 + s2
# a    11.0
# b     7.0
# c     NaN   <- s1에는 'c'가 없어서 NaN
```

### 자주 쓰는 메서드 — Series 전용 아님

`head`/`tail`/`describe`/`sum`/`value_counts`는 Series와 DataFrame이 공통 부모 클래스(`NDFrame`)를 상속받기 때문에 **둘 다에서 사용 가능**. Series에서 먼저 배우는 경우가 많아 "Series 함수"처럼 느껴질 수 있지만 실제로는 공통 메서드.

| 메서드 | Series일 때 | DataFrame일 때 |
|---|---|---|
| `head(n)` / `tail(n)` | 앞/뒤 n개 값 | 앞/뒤 n개 **행 전체** |
| `describe()` | 그 열 하나의 통계 요약 | **모든 숫자 열 각각**에 대한 통계 요약 |
| `sum()` | 전체 값의 합 하나 | **열마다** 합을 따로 계산 |
| `value_counts()` | 값별 등장 횟수 | **행 전체 조합**별 등장 횟수 |

```python
df.describe()                 # * 기본값 -> 숫자 열만 요약
df.describe(include=object)   # * 문자열(object) 열만 요약 -> count/unique/top/freq
df.describe(include='all')    # * 숫자 + 문자열 열 전부 같이 요약 (안 맞는 칸은 NaN)
```

## `df.loc` / `df.iloc` (`dataframe_1.ipynb`)

### loc vs iloc

| | `loc` | `iloc` |
|---|---|---|
| 기준 | 라벨(이름) | 정수 위치 (0부터) |
| 예시 | `df.loc['a']` | `df.iloc[0]` |

### `[행, 열]` 구조 — 대괄호 안에 뭐가 몇 개 있는지가 핵심

```python
df.loc['a']          # * 값 1개 -> 행(row) 기준
df.loc['a', 'x']      # * 콤마로 나누면 [행, 열] -> 값 하나 콕 집기
df.loc[['a','b'], ['x','y']]  # * 행/열 여러 개를 리스트로 -> 부분 표(서브셋)
```

**핵심 규칙**: 대괄호 안에 값이 **1개**면 무조건 **행** 기준. **열까지 지정하려면 반드시 콤마로 나눠서** `df.loc[행, 열]` / `df.iloc[행, 열]` 형태로 써야 함.

### 슬라이싱(`:`) — loc와 iloc가 다르게 동작

```python
df.loc['a':'c']    # * 라벨 기준 슬라이싱 -> 끝 라벨('c')도 "포함"됨
df.iloc[0:2]        # * 위치 기준 슬라이싱 -> 끝 위치(2)는 "미포함" (파이썬 리스트 슬라이싱과 동일)
df.iloc[::2]         # * step 슬라이싱 -> 처음부터 끝까지 2칸씩 건너뛰기
```

- `loc` 슬라이싱은 일반 파이썬 슬라이싱과 다르게 **끝 라벨도 결과에 포함**됨 (헷갈리기 쉬운 포인트)
- `iloc` 슬라이싱은 파이썬 리스트/numpy와 똑같이 **끝 위치는 미포함**

### 행과 열을 동시에 슬라이싱하기

```python
df.iloc[:, 0:2]        # * 행 자리에 :(전체) -> 열만 슬라이싱
df.iloc[0:2, 1:3]       # * 행도 열도 둘 다 슬라이싱 -> [행 범위, 열 범위]
```

## DataFrame 합치기: concat vs merge vs join (`dataframe_2.ipynb`)

### 가로 합치기 vs 세로 합치기 — 셋의 가장 큰 차이

| | 방향 | 기준 |
|---|---|---|
| `concat` (기본값, `axis=0`) | **세로** (행이 늘어남) | 없음 — 그냥 이어붙이기 |
| `concat(axis=1)` | **가로** (열이 늘어남) | 없음 — 위치 순서대로 나란히 |
| `merge` | **가로** (열이 늘어남) | 공통 **열(column)** 값이 같은 행끼리 |
| `join` | **가로** (열이 늘어남) | **인덱스(index)** 값이 같은 행끼리 |

### 셋 다 실제로 실행해서 비교

```python
df1 = pd.DataFrame({'Name':['Alice','Bob'], 'Age':[25,30]})
df2 = pd.DataFrame({'Name':['Charlie','David'], 'Age':[35,40]})

pd.concat([df1, df2], ignore_index=True)
#       Name  Age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35
# 3    David   40
```

```python
a = pd.DataFrame({'ID':[1,2,3], 'Name':['Alice','Bob','Charlie']})
b = pd.DataFrame({'ID':[1,2,3], 'Age':[25,30,35]})

pd.merge(a, b, on='ID')   # * ID라는 "열" 값이 같은 행끼리 짝지어서 합침 (SQL JOIN과 동일한 개념)
#    ID     Name  Age
# 0   1    Alice   25
# 1   2      Bob   30
# 2   3  Charlie   35
```

```python
a2 = a.set_index('ID')
b2 = b.set_index('ID')

a2.join(b2)   # * merge랑 하는 일은 비슷하지만 기준이 "열"이 아니라 "인덱스"
#        Name  Age
# ID
# 1     Alice   25
# 2       Bob   30
# 3   Charlie   35
```

### 한 줄 정리

- **`concat`**: 짝짓는 기준 자체가 없음 — 그냥 이어붙이기 (세로가 기본, `axis=1`이면 가로)
- **`merge`**: 특정 **열 값**이 같은 행끼리 짝지어서 가로로 합침 (제일 유연, SQL `JOIN`과 동일)
- **`join`**: `merge`의 특수한 경우 — 기준이 열이 아니라 **인덱스**

## `axis` 완전 정리 (`dataframe_3.ipynb`)

### 집계 함수(`sum`/`mean`/`apply` 등) — "어느 방향으로 훑는지"

```
axis=0 (↓ 세로로 훑음)        axis=1 (→ 가로로 훑음)
   Math  Physics                  Math  Physics
    ↓      ↓                 Alice → → →
   85     80
    ↓      ↓                 Bob   → → →
   90     85
```

- `axis=0` → 같은 **열** 안에서 위→아래로 계산 → 결과는 **열 단위**(`Math`, `Physics`, ...)로 나옴
- `axis=1` → 같은 **행** 안에서 왼→오른쪽으로 계산 → 결과는 **행 단위**(`Alice`, `Bob`, ...)로 나옴

```python
df.sum(axis=0)     # * 열마다 합계 (Math 합, Physics 합, ...)
df.sum(axis=1)     # * 행마다 합계 (Alice 총합, Bob 총합, ...)
df.apply(lambda row: row.mean(), axis=1)   # * 행 단위로 함수 적용 (학생별 평균)
```

`mean`/`max`/`min`/`std`/`count`/`apply` 전부 이 규칙을 따름 — **예외 없음.**

### 삭제 함수(`drop`/`dropna`) — "무엇을 지울지"

집계 함수와 `axis`의 **의미 자체가 다름.** 방향이 아니라 "지울 대상이 행 이름표냐 열 이름표냐"를 가리킴.

```python
df.drop('Alice', axis=0)   # * axis=0 -> '행' 이름을 지움 (Alice 행 삭제)
df.drop('Math', axis=1)     # * axis=1 -> '열' 이름을 지움 (Math 열 삭제)
```

| | 집계 함수 (`sum`, `apply`, ...) | 삭제 함수 (`drop`, `dropna`, ...) |
|---|---|---|
| `axis`의 의미 | 어느 방향으로 훑으며 계산할지 | 지울 대상이 행인지 열인지 |
| `axis=0` | 결과가 **열 단위**로 나옴 | **행**을 지움 |
| `axis=1` | 결과가 **행 단위**로 나옴 | **열**을 지움 |

**헷갈리지 않는 법**: `axis=0`/`axis=1`이라는 이름은 항상 "행 축(index)"/"열 축(columns)"을 가리키는 게 맞지만, 그 축을 **"계산 방향"으로 쓰는지 "삭제 대상"으로 쓰는지는 함수마다 다름.**

## 결측치(NaN) 처리 (`dataframe_3.ipynb`)

### 결측치 확인/제거/채우기

| 함수 | 뜻 |
|---|---|
| `isna()` | 값이 NaN인 자리마다 True/False 표시 |
| `dropna()` | NaN이 하나라도 있는 **행**을 통째로 삭제 (기본값) |
| `dropna(thresh=n)` | 정상 값(NaN 아닌 값)이 **최소 n개는 있어야** 그 행을 유지 |
| `dropna(axis=1)` | NaN이 있는 **열**을 삭제 |
| `fillna(값)` | NaN 자리를 지정한 값으로 채우기 |
| `fillna(df.mean())` | NaN을 그 열의 평균값으로 채우기 |
| `ffill()` | NaN을 바로 위(이전) 값으로 채우기 (forward fill) |
| `bfill()` | NaN을 바로 아래(다음) 값으로 채우기 (backward fill) |

```python
df.dropna(thresh=2)   # * 정상값이 2개 이상이면 유지, 1개 이하면 삭제 (>= 조건, 경계값은 유지)
```

- ⚠️ `fillna(method='ffill')`처럼 `method=` 파라미터로 쓰는 방식은 최신 pandas(3.x)에서 **삭제됨** → `df.ffill()`/`df.bfill()`을 직접 호출해야 함
- `mean()`/`sum()` 등 집계 함수는 기본적으로 **NaN을 합계·개수 둘 다에서 제외**하고 계산함 (`skipna=True`가 기본값)

### 값 확인 함수

| 함수 | 뜻 |
|---|---|
| `unique()` | 중복 제거한 값 목록 (NaN도 값으로 포함) |
| `nunique()` | 중복 없는 값이 몇 개인지 개수만 (NaN은 기본적으로 제외) |
| `value_counts()` | 값마다 몇 번씩 등장했는지 개수 세기 |

## `apply` + `lambda` (`dataframe_3.ipynb`)

### `lambda` — 이름 없는 한 줄 함수

```python
def my_func(row):        # * 이름 있는 보통 함수
    return row.mean()

f = lambda row: row.mean()  # * 위와 똑같은 일을 하는 이름 없는 함수 (한 줄로 압축)
```

`lambda 매개변수: 반환할 표현식` 구조 — `def`/`return`/함수 이름을 다 생략한 것뿐, 동작은 완전히 같음.

### `apply(함수, axis)` — 내장 함수로 안 되는 계산을 직접 만들어 적용

```python
df.apply(lambda row: row.mean(), axis=1)   # * 행 단위로 적용 (학생별 평균)
df.apply(lambda col: col.mean(), axis=0)   # * 열 단위로 적용 (과목별 평균)
```

- `row`/`col`은 그냥 붙인 이름 — `apply`가 각 행(또는 열)을 Series로 만들어서 그 이름에 넘겨주는 것뿐, 이름 자체는 아무거나 써도 됨
- `axis=1`/`axis=0` 규칙은 `sum`/`mean` 같은 집계 함수랑 **완전히 동일** (위 "axis 완전 정리" 참고)

## `pivot_table` (`dataframe_3.ipynb`)

엑셀 피벗 테이블과 같은 개념 — 데이터를 표 형태로 재구성해서 요약.

```python
df.pivot_table(
    values='Sales',    # * 채울 값
    index='Region',     # * 결과의 행 기준
    columns='Product',  # * 결과의 열 기준
    aggfunc='sum')       # * Region+Product 조합마다 Sales를 합산해서 채움
```

## 파일/DB 입출력 (`dataframe_input_output.ipynb`)

### csv / json / excel

| 함수 | 뜻 |
|---|---|
| `pd.read_csv(경로)` | csv 파일 → DataFrame |
| `df.to_csv(경로, index=False)` | DataFrame → csv 파일, `index=False`면 인덱스 열은 저장 안 함 |
| `pd.read_json(경로)` | json 파일 → DataFrame |
| `json.load(f)` | json 파일 → 파이썬 딕셔너리 (아직 DataFrame 아님) |
| `pd.read_excel(경로, sheet_name=...)` | 엑셀 파일 → DataFrame |
| `df.to_excel(경로, sheet_name=...)` | DataFrame → 엑셀 파일 |

- `to_csv`/`to_excel`에서 `index=False`를 안 주면(기본값 `True`) **인덱스 열도 같이 저장됨** — 보통 필요 없어서 `False`로 많이 씀
- 딕셔너리 값들이 스칼라(리스트 아님)일 때 `pd.DataFrame(data)`만 하면 에러남 → `pd.DataFrame(data, index=[0])`처럼 행이 1개짜리라는 걸 명시해야 함

### DB 연결 (`sqlalchemy`)

```python
connection_string = f'mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = sa.create_engine(connection_string)      # * "연결 통로"만 준비, 아직 실제 접속 안 함
data = pd.read_sql_query(sql_query, engine)        # * 여기서 진짜 접속 + 쿼리 실행
```

- `create_engine()`은 `db_name`이 틀려도 **에러 없이 성공**함 (실제 접속 안 하니까) — 진짜 접속은 `read_sql_query()` 시점에 일어남
- 접속하려는 DB가 실제로 존재해야 함 — 로컬에 MySQL 서버가 없으면 Docker로 띄워서 테스트 (`docker-compose.yml` + `docker compose up -d`)

### 웹페이지 표 읽기 (`read_html`)

```python
import requests
from io import StringIO

headers = {'User-Agent': 'Mozilla/5.0'}   # * 기본값은 'python-requests/버전'이라 봇으로 차단당하기 쉬움
response = requests.get(url, headers=headers)
tables = pd.read_html(StringIO(response.text))   # * 문자열은 StringIO로 감싸야 "파일"로 인식됨
```

- `pd.read_html(url)`을 그대로 쓰면 위키피디아 같은 사이트에서 봇 요청으로 인식해서 `403 Forbidden`이 날 수 있음
- `requests` + `User-Agent` 헤더로 직접 받아온 HTML을 넘기는 방식이 실무에서도 흔한 우회법
