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
