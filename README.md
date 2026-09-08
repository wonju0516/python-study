# python-study

알고리즘 / 자료구조 / 파이썬 기초 문법 공부 기록용 저장소입니다.

각 폴더의 세부 개념 정리는 폴더 안 README.md를 참고하세요.

## 폴더 구조

각 폴더 안의 파일 하나하나가 뭘 다루는지는 그 폴더의 README.md에 정리돼 있습니다 (파일이 늘어날 때마다 여기까지 다 갱신하지 않기 위해, 여기서는 폴더 단위까지만 보여줍니다).

```
firstPython/
├── algorithm/              # → algorithm/README.md
├── datastructure/          # → datastructure/README.md
└── python_basics/
    ├── playground.ipynb    # 라이브러리 설치/실행 테스트용 노트북
    ├── loop_function/          # → python_basics/loop_function/README.md
    ├── io_condition/           # → python_basics/io_condition/README.md
    ├── python_internals/       # → python_basics/python_internals/README.md
    ├── oop/                    # → python_basics/oop/README.md
    └── file_data_processing/   # → python_basics/file_data_processing/README.md
```

## 폴더별 정리

- [algorithm/](firstPython/algorithm/README.md) — 재귀, 탐색, 정렬, 문자열, 비트 연산, 수학 알고리즘
- [datastructure/](firstPython/datastructure/README.md) — 배열(리스트)/연결 리스트/스택/큐/해시 테이블/이진 트리 개념, set을 활용한 중복/교집합 찾기, 연결 리스트 삽입·삭제·뒤집기·사이클 탐지, 스택 push/pop O(1) 원리, MinStack/MaxStack, 괄호 짝 검사, 큐 FIFO와 스택 2개로 큐 구현, 해시 충돌과 두 수의 합, BST와 O(log n), BFS/DFS와 트리 순회, 트리 뒤집기
- [python_basics/loop_function/](firstPython/python_basics/loop_function/README.md) — 리스트/딕셔너리 기초, for-in/range/enumerate, FizzBuzz, while/이터레이터, 함수(타입힌트·키워드인자·반환값·언제 뽑아야 하는지), 소수 판별, 랜덤 비밀번호 생성기, 행맨, 다단계 중첩과 오버라이트
- [python_basics/io_condition/](firstPython/python_basics/io_condition/README.md) — print/input, 문자열 포맷팅, 기본 데이터 타입, 사칙연산, 조건문, 논리 연산자, random 모듈, 커스텀 모듈
- [python_basics/python_internals/](firstPython/python_basics/python_internals/README.md) — 얕은 복사/깊은 복사와 compound object, 스코프(LEGB, global/nonlocal), 코드를 줄이는 better solution 모음
- [python_basics/oop/](firstPython/python_basics/oop/README.md) — 클래스/객체/메소드 기초, turtle 라이브러리, naming convention, 생성자(__init__), 외부 패키지(PrettyTable) 활용, list/dict/set/tuple 내장 자료형 비교, 고차함수와 데코레이터, 상속·오버라이딩·super()·메소드 탐색 순서
- [python_basics/file_data_processing/](firstPython/python_basics/file_data_processing/README.md) — 파일 열기/닫기, with문과 메모리 관리, 모드(r/w/a), 실행 위치에 따른 상대경로 문제와 pathlib 해결법, csv 모듈, pandas.read_csv, 가상환경과 pyenv 차이
