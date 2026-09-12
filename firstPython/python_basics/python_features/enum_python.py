# * Enum(열거형): "정해진 값들 중 하나"만 가질 수 있는 특수한 타입을 만드는 도구
# * 문자열/숫자를 그냥 쓰면 오타가 나도 에러가 안 나지만, Enum은 허용된 멤버만 쓰도록 강제해줌
from enum import Enum


class Car(Enum):  # * Car(Enum) -> Car가 Enum을 상속받음 -> Car는 "열거형" 타입이 됨
    HYUNDAY = 1  # * HYUNDAY는 멤버 이름, 1은 그 멤버에 연결된 값 (값은 꼭 숫자가 아니어도 됨)
    KIA = 2
    TESLA = 3
    FORD = 4


print(Car.HYUNDAY)  # Car.HYUNDAY  -> 그냥 1이 아니라 "Car.HYUNDAY"라는 고유한 멤버 자체가 출력됨
print(Car.HYUNDAY.name)  # "HYUNDAY"  -> 멤버의 이름(문자열)
print(Car.HYUNDAY.value)  # 1          -> 멤버에 연결된 실제 값
print(type(Car.HYUNDAY))  # <enum 'Car'>  -> Car.HYUNDAY의 타입은 Car 클래스 자체
print(list[Car])  # list[Car]  -> 이건 실행 결과가 아니라 "Car를 원소로 갖는 리스트"라는 타입힌트 표현일 뿐

# * list(Car): Enum 클래스를 리스트로 감싸면 정의된 멤버들을 순서대로 다 꺼낼 수 있음
for car in list(Car):
    print(f"{car.name} - {car.value}")
