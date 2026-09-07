"""car2"""


class Car2:
    def __init__(self, color, engine_type):
        # * color, engine_type -> __init__이 넘겨받은 매개변수(파라미터), 이 함수 안에서만 쓰는 임시 값
        # * self.color, self.engine_type -> 그 값을 "이 객체(self)의 속성"으로 저장하는 것
        # ! 왼쪽(self.color)은 객체에 영구히 저장되는 값, 오른쪽(color)은 그냥 지금 받은 매개변수일 뿐
        self.color = color
        self.engine_type = engine_type
        self.speed = 0
        self.is_start = False

    # * 메소드도 만들어보기
    def start_engine(self):
        self.speed = 0
        self.is_start = True

    def speed_up(self, speed):
        self.speed += speed

    def speed_down(self, speed):
        self.speed -= speed
