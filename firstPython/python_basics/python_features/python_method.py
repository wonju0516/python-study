# class method


class Car:
    def __init__(self, body_type):
        self.body_type = body_type

    # * __repr__: 이 객체를 print()할 때 어떤 문자열로 보여줄지 정하는 매직 메소드
    # * 없으면 <__main__.Car object at 0x...> 같은 기본값이 찍힘
    def __repr__(self) -> str:
        return f"Car({self.body_type} body Type)"

    def set_body_type(self, body_type):
        self.body_type = body_type

    # * @classmethod: 첫 파라미터가 self(객체)가 아니라 cls(클래스 자신)가 됨
    # * cls("sedan")은 Car("sedan")과 같은 뜻 -> 새 객체를 만들어서 반환하는 "팩토리 메소드" 패턴

    @classmethod
    def hyundai(cls):
        return cls("sedan")

    @classmethod
    def ferrari(cls):
        return cls("convertible")


c = Car(body_type="sport")
c.set_body_type("sedan")
print(c.body_type)

# * cls는 항상 "그 클래스 자체"를 가리켜서, 인스턴스(c)로 불러도 결과는 똑같이 새 Car를 만듦
print(Car.hyundai())  # * __repr__ 덕분에 "Car(sedan body Type)"처럼 보기 좋게 출력됨
print(c.ferrari())
# * c가 갖고 있던 값(sedan)과 무관하게 새 Car("convertible")가 만들어짐


# * static method: self/cls를 아예 안 받음 -> 객체 없이 클래스명으로 바로 호출 가능
# * self가 없어서 객체 상태도 못 바꿈. "클래스랑 관련은 있지만 객체 값은 안 건드리는 계산"에 씀


# * 방법 1: 함수 다 만들고 나서 나중에 staticmethod()로 감싸기
class Calc:
    def add(x: int, y: int) -> int:
        return x + y


Calc.add = staticmethod(Calc.add)  # * 여기서 진짜로 static method로 확정시킴

print("Product", Calc.add(15, 110))


# * 방법 2: @staticmethod 데코레이터로 처음부터 명시
class Calc2:
    @staticmethod
    def add(x: int, y: int) -> int:
        return x + y


print("Product:", Calc2.add(15, 100))
