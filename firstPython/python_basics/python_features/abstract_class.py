# abstract class
# * 추상 클래스 -  직접 사용하지 않고 자식 클래스가 완성해서 써라 (직접 인스턴스를 못만듬)

# * Abstract Base Class
# * ABC: "나는 추상 클래스다"라고 표시해주는 부모 클래스 (이것 자체엔 특별한 기능 없음, 표식 역할)
# * abstractmethod: 이 메서드는 자식이 반드시 직접 구현해야 함을 표시하는 데코레이터
from abc import ABC, abstractmethod


class Car(ABC):  # * class Car(ABC) -> Car가 ABC를 상속받음 -> Car도 추상 클래스가 됨
    def start_engine(self):
        print("start....")

    @abstractmethod
    def turn_off_engine(self):
        raise NotImplementedError  # * 실제로 호출되면 안 되는 메서드라서 에러를 던짐


# c = Car() # ! -> 에러 발생!! 이유: turn_off_engine이 구현 안 된 추상 메서드라서 Car는 미완성 상태 -> 인스턴스화 불가


class Tesla(Car):  # * Tesla가 Car를 상속받음 (Car의 start_engine을 그대로 물려받음)
    def turn_off_engine(
        self,
    ):  # * 추상 메서드를 실제로 구현 -> 이제 Tesla는 완성된 클래스
        print("turning off...")


t = Tesla()
t.start_engine()
t.turn_off_engine()

## * Protocol
# * Protocol: 상속 안 해도 "이 모양(속성/메서드)만 갖고 있으면 이 타입으로 인정"해주는 타입힌트용 틀
# * ABC와 차이: ABC는 진짜로 상속해야 하지만, Protocol은 상속 없이 그냥 생긴 모양만 같으면 통과됨

from typing import Protocol


class Item(
    Protocol
):  # * "quantity와 price라는 속성을 가진 것"이라는 모양만 정의 (실제 동작 없음)
    quantity: float
    price: float


class Product:  # ! Item을 상속받지 않았지만 quantity, price를 둘 다 가지고 있음 -> Item 모양과 일치
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


class Stock:  # ! 이것도 Item을 상속 안 했지만 마찬가지로 quantity, price를 가짐 -> Item 모양과 일치
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


def calculate_total(items: list[Item]) -> float:
    # * items: list[Item] -> "quantity, price를 가진 것들의 리스트"라는 뜻 (Product인지 Stock인지는 안 따짐)
    return sum([item.quantity * item.price for item in items])


total = calculate_total([Product("A", 10, 150), Stock("B", 5, 250)])

print(total)

# * 덕 타이핑(duck typing): "오리처럼 걷고 오리처럼 운다면 그건 오리다" -> 상속 관계와 상관없이
# * 필요한 속성/메서드만 가지고 있으면 그 타입으로 취급하는 파이썬의 방식 (Protocol이 이걸 타입힌트로 표현한 것)
