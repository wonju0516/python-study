# python-study

알고리즘 / 자료구조 / 파이썬 기초 문법 공부 기록용 저장소입니다.

각 폴더의 세부 개념 정리는 폴더 안 README.md를 참고하세요.

## 폴더 구조

```
firstPython/
├── algorithm/              # → algorithm/README.md
│   ├── algorithm1.py       # 반복문 기초 (for, range)
│   ├── math.py             # 비트 연산자, 피즈버즈, 최대공약수
│   ├── recursion.py        # 재귀 기초 (팩토리얼)
│   ├── search_Algorithm.py # 탐색 알고리즘
│   ├── sorting.py          # 정렬 알고리즘
│   └── string_algorithm.py # 문자열 알고리즘 (애너그램, 팰린드롬, 시저 암호)
├── datastructure/           # → datastructure/README.md
│   ├── array_practice.py   # 배열(리스트), 0 옮기기, zip, set, 교집합, 짝수/홀수 분리
│   ├── linked_list.py      # 연결 리스트: Node/LinkedList 클래스, append/search/remove/reverse/사이클 탐지
│   └── stack_file.py       # 스택: 배열/연결리스트 구현, 문자열 뒤집기, MinStack/MaxStack, 괄호 짝 검사
└── python_basics/
    ├── playground.ipynb    # 라이브러리 설치/실행 테스트용 노트북
    ├── loop_function/      # → python_basics/loop_function/README.md
    │   ├── list_data_structure.py  # 리스트 기초, 코딩테스트용 메서드, 중첩 리스트
    │   ├── loop.py                 # for-in vs range() vs enumerate()
    │   ├── fizzbuzz.py             # FizzBuzz, 겹치는 조건 순서
    │   ├── password_pro.py         # random 모듈로 랜덤 비밀번호 생성기
    │   ├── while_loop.py           # while vs for, while True + break
    │   ├── string_reverse.py       # 문자열 뒤집기 4가지 방법, 이터레이터
    │   ├── robot_game.py           # 함수 기초
    │   ├── function_with_param.py  # 타입 힌트, 키워드 인자, 함수 반환값
    │   ├── going_dutch.py          # 더치페이 계산, float() 나눗셈
    │   ├── hangman.py              # 행맨 게임, 시도 횟수 설계 선택
    │   ├── prime_number.py         # 소수 판별 함수 두 버전 비교
    │   ├── dictionaries.py         # 딕셔너리 기초 (items, keys, values, in)
    │   └── grading_program.py      # 언제 함수로 뽑아야 하는지
    └── io_condition/       # → python_basics/io_condition/README.md (섹션 3: 입출력, 조건절)
        ├── print.py
        ├── input.py
        ├── f-string.py
        ├── primitive_data_type.py
        ├── mathmatical_operation.py
        ├── conditional-expression.py
        ├── logical-operator.py
        ├── Randomization.py
        ├── mok_module.py
        └── coin.py
```

## 폴더별 정리

- [algorithm/](firstPython/algorithm/README.md) — 재귀, 탐색, 정렬, 문자열, 비트 연산, 수학 알고리즘
- [datastructure/](firstPython/datastructure/README.md) — 배열(리스트)/연결 리스트/스택 개념, set을 활용한 중복/교집합 찾기, 연결 리스트 삽입·삭제·뒤집기·사이클 탐지, 스택 push/pop O(1) 원리, MinStack/MaxStack, 괄호 짝 검사
- [python_basics/loop_function/](firstPython/python_basics/loop_function/README.md) — 리스트/딕셔너리 기초, for-in/range/enumerate, FizzBuzz, while/이터레이터, 함수(타입힌트·키워드인자·반환값·언제 뽑아야 하는지), 소수 판별, 랜덤 비밀번호 생성기, 행맨
- [python_basics/io_condition/](firstPython/python_basics/io_condition/README.md) — print/input, 문자열 포맷팅, 기본 데이터 타입, 사칙연산, 조건문, 논리 연산자, random 모듈, 커스텀 모듈
