# * 부모 클래스
class Car:
    def __init__(self):
        self.wheel_count = 4
        self.door_count = 2

    def start(self):
        print("started...")

    def drive(self):
        print("driving...")


# * class 자식클래스(부모클래스): 이렇게 쓰면 상속됨
class ElectricCar(Car):
    def __init__(self):
        # ! super().__init__() 안 부르면 부모의 __init__이 실행 안 됨
        super().__init__()

    # * 오버라이딩: 부모에 있는 start()를 자식이 같은 이름으로 재정의
    def start(self):
        # * ec.start() 호출 시 탐색순서: 객체(ec) -> 객체의 클래스(ElectricCar) -> 부모클래스(Car)
        # * ElectricCar에서 바로 찾아지니 거기서 멈춤. Car까지 안 감.
        # * super().start() 있으면: 그 안에서 명시적으로 Car.start() 호출 -> started... + No sound... 둘 다 출력
        # * super().start() 없으면: Car.start() 호출 자체가 없으니 No sound...만 출력
        super().start()
        print("No sound...")


class CombustionEngineCar(Car):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print("vrooooom...")


ec = ElectricCar()
ec.start()  # * ElectricCar가 오버라이딩했으니 이 버전 실행됨
ec.drive()  # * drive()는 오버라이딩 안 했으니 부모(Car) 것 그대로 실행됨

print("----------------")

cec1 = CombustionEngineCar()
cec1.start()
cec1.drive()
# * id(): 객체 고유 식별값. 다른 인스턴스면 값 같아도 id는 다름
print(id(cec1))

cec2 = CombustionEngineCar()
print(id(cec2))  # * cec1과 별개 인스턴스라 id 다르게 나옴
