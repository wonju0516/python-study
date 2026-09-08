from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).parent  # ! 이 파일이 있는 경로

# * DataFrame: 2차원 표, 크기 변경 가능, 컬럼마다 다른 타입 가능
data = pd.read_csv(BASE_DIR / "sample.csv")
print(data)
print(type(data))
print(data.to_dict())  # * 딕셔너리로 변환

# * Series: DataFrame의 컬럼 하나 (1차원, 같은 컬럼은 같은 타입)
print(type(data["country"]))
print(data["country"].to_list())  # * 리스트로 변환

# * sum(리스트): 파이썬 내장 함수 / 시리즈.sum(): pandas 자체 메소드 (pandas에선 이게 표준)
print(sum(data["population"].to_list()))
print(data["population"].sum())
print(data["population"].max())

# * data["population"] 대신 data.population 으로도 접근 가능
# ! 컬럼명에 공백/특수문자 있으면 이 방식은 안 됨
print(data.population)

# * 조건에 맞는 행만 필터링 (불리언 인덱싱)
print(data[data.country == "United States"])
print(data[data.population == data.population.max()])

# * 자주 쓰는 함수들
print(data.head(3))  # * 위에서 3개만
print(data.shape)  # * (행, 열) 개수
print(data.columns)  # * 컬럼명 목록
print(data.sort_values("population"))  # * 정렬
print(data["continent"].value_counts())  # * 값별 개수
print(data.describe())  # * 통계 요약 (숫자 컬럼: 평균/표준편차 등)
print(data.describe(include="object"))
# * 범주형(문자열) 컬럼: count/unique/top/freq로 다르게 나옴

# * 딕셔너리로 DataFrame 직접 만들기 (key=컬럼명, value=값 리스트)
grade = {"student": ["A", "B", "C"], "scores": [90, 80, 85]}
data = pd.DataFrame(grade)
print(data)
data.to_csv(BASE_DIR / "grade.csv", index=False)
