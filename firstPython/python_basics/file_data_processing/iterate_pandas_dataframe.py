# iterate pandas dataframe: DataFrame을 반복문으로 순회하는 여러 방법

score_dict = {"student": ["Tom", "Lisa", " Sarah"], "score": [80, 90, 95]}

# * 딕셔너리.items()로 key만 뽑아 순회 (value는 안 써서 관례적으로 _로 표시, 버림 변수)
[print(col) for (col, _) in score_dict.items()]

import pandas as pd

score_df = pd.DataFrame(score_dict)
print(score_df)

# ! DataFrame.items()는 딕셔너리 items()랑 다름: "행"이 아니라 "컬럼"을 하나씩 돎
# ! key=컬럼명, value=그 컬럼 전체(Series) -> 여기선 student 컬럼, score 컬럼이 각각 한 번씩만 나옴
for key, value in score_df.items():
    print(key)
    print(value)

# * iterrows(): 진짜 "행" 단위로 순회. 반복마다 (인덱스, 그 행의 Series)를 돌려줌
# * row["student"]처럼 대괄호로 접근하는 게 표준 (row.student도 되지만, 컬럼명에 공백/특수문자 있으면 안 되므로 대괄호가 더 안전해서 실무에서 더 많이 씀)
for i, row in score_df.iterrows():
    print(f"{row['student']} : {row['score']}")
