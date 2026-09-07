# custom class
# * naming convention (이름 짓는 규칙)
## * PascalCase (단어별 첫글자 대문자, 예: Car1) : class name
## * camelCase (첫단어 소문자, 이후 첫글자만 대문자, 예: myCar) : object name
## * snake_case (전부 소문자, 언더스코어로 연결, 예: engine_type) : anything else
## ! 참고: 파이썬 공식 스타일(PEP8)은 보통 객체(변수)도 snake_case를 씀


class Car1:
    pass


tesla = Car1()
# * 클래스가 빈 껍데기(pass)라도, 객체를 만든 뒤엔 속성을 즉석에서 자유롭게 추가할 수 있음
tesla.color = "red"  # * 이 순간 tesla 객체에 color라는 속성이 새로 생김
tesla.engine_type = "electric"

print(tesla.color)

print(vars(tesla))  # * vars(객체) -> 객체의 __dict__와 동일, 속성들을 딕셔너리로 보여줌


# * 생성자(constructor) = __init__ -> 객체를 만드는 순간(Car2(...)) 자동으로 실행되는 함수
# * Car1처럼 나중에 속성을 하나씩 즉석 추가하는 대신, 생성자에서 한 번에 속성을 다 정해놓는 방식
class Car2:
    def __init__(self, color, engine_type):
        # * color, engine_type -> __init__이 넘겨받은 매개변수(파라미터), 이 함수 안에서만 쓰는 임시 값
        # * self.color, self.engine_type -> 그 값을 "이 객체(self)의 속성"으로 저장하는 것
        # ! 왼쪽(self.color)은 객체에 영구히 저장되는 값, 오른쪽(color)은 그냥 지금 받은 매개변수일 뿐
        self.color = color
        self.engine_type = engine_type


tesla2 = Car2("green", "electric")
print(tesla2.color)
