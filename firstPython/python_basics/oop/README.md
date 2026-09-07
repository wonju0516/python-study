# 객체지향 프로그래밍 (oop)

## 클래스 기초 — Turtle 라이브러리 (`oop_turtle.py`)

- **클래스(class)**: 객체를 찍어내는 설계도. `Turtle`이 클래스
- **객체/인스턴스**: 클래스로 실제로 찍어낸 것. `john = Turtle()` → `john`이 `Turtle`의 인스턴스
- **메소드(method)**: 클래스 안에 정의돼서 특정 객체에 소속된 함수 (`john.forward(5)`, `john.shape("turtle")`). `객체.메소드()` 형태로 호출
- **함수(function)**: 특정 객체에 속하지 않는 독립적인 코드. `time.sleep()`은 메소드처럼 보이지만 사실 `time` 모듈 안의 함수 — `time`은 객체가 아니라 모듈이라 자기만의 상태가 없음
- **`from 모듈 import 이름`**: 모듈 전체가 아니라 그 안의 특정 이름 하나만 콕 집어 가져옴 (접두어 없이 바로 사용 가능). 그 이름이 클래스면, 클래스 안의 메소드들도 전부 같이 딸려옴 (메소드는 모듈이 아니라 클래스에 속한 것)
  - `import 모듈`(모듈 전체)은 여러 걸 폭넓게 쓸 때, `from 모듈 import 이름`은 딱 몇 개만 자주 쓸 때 편함

## 커스텀 클래스 & 생성자 (`custom_class.py`)

- **naming convention**: 클래스 이름은 PascalCase(`Car1`), 나머지(변수 등)는 snake_case가 파이썬(PEP8) 기본 스타일
- **동적 속성 추가**: `class Car1: pass`처럼 빈 클래스라도, 객체를 만든 뒤 `tesla.color = "red"`처럼 즉석에서 속성을 자유롭게 추가할 수 있음 (`vars(객체)`로 그 객체가 가진 속성들을 딕셔너리로 확인 가능)
- **생성자(constructor, `__init__`)**: 객체를 만드는 순간(`Car2(...)`) 자동으로 실행되는 함수. 매번 속성을 하나씩 즉석 추가하는 대신, 생성자에서 한 번에 정해두는 정석적인 방식
  - `__init__(self, color, engine_type)`의 `color`/`engine_type`은 그 함수 안에서만 쓰이는 매개변수(임시 값)
  - `self.color = color`는 "이 객체(`self`)의 `color` 속성에, 방금 받은 매개변수 값을 영구 저장"하는 것 — 왼쪽(`self.color`)과 오른쪽(`color`)은 이름이 같아 보여도 역할이 다름

## 외부 패키지 활용 — PrettyTable (`pypi.py`)

- `pip install prettytable`로 설치하는 외부 라이브러리, 표 형태로 데이터를 보기 좋게 출력해줌
- `table.field_names`로 컬럼 이름 지정, `table.add_row([...])`로 행 추가, `print(table)`로 ASCII 표 형태 출력
