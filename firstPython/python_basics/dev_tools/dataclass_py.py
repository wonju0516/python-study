import inspect
from dataclasses import asdict, astuple, dataclass, replace
from pprint import pprint


# * frozen -> 한번 만들면 값 못 바꾸게 고정 (불변)
# * order -> 비교 연산자(<, >) 사용 가능하게 함
@dataclass(frozen=True, order=True)
# @dataclass
class Car:
    id: int
    color: str = ""
    brand: str = ""


# * 클래스 안에 있는 함수 목록 출력
pprint(inspect.getmembers(Car, inspect.isfunction))

car1 = Car(1, "White", "TESLA")
print(car1)

# ! 불변 객체라 값 수정 불가 (바꾸려 하면 에러남)

car2 = Car(2, "White", "TESLA")
print(f"comparing two objects: {car1 < car2}")  # * order=True라 비교 가능

# * 튜플로 변환
print(astuple(car1))

# * 딕셔너리로 변환
print(asdict(car1))

# * 원본은 그대로 두고, 일부 필드만 바뀐 새 복사본 생성
print(replace(car1, id=3))


# * dataclass 필드에 다른 dataclass 객체들도 담을 수 있음 (중첩 구조)
@dataclass
class Inventory:
    cars: list[Car]  # * Car 객체 여러 개를 담는 리스트 필드


inventory = Inventory([car1, car2])
print(inventory)


# * 상속 -> 부모 클래스 필드를 그대로 물려받고, 필드 추가 가능


@dataclass(frozen=True)  # ! 부모가 frozen이라 자식도 frozen이어야 함
class Taxi(Car):
    owner_company: str = ""


taxi1 = Taxi(1, "Yellow", "HYUNDAY", "xyz")
print(taxi1)
