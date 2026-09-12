# metaclasses
# * 메타클래스(metaclass): 클래스를 만들어내는 클래스 -> "클래스의 클래스"
# * 클래스는 객체를 어떻게 찍어낼지 정하는 설계도이고, 메타클래스는 그 클래스 자체를 어떻게 찍어낼지 정하는 설계도
# * 우리는 클래스를 인스턴스화해서 각각 다른 객체를 만드는데, 클래스 자체도 사실은 메타클래스의 인스턴스임


# * object: 모든 클래스가 자동으로 상속받는 최상위 부모 -> (object) 안 써도 원래 그렇게 동작함, 여기선 명시적으로 써준 것뿐
class Car(object):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # * special method -> print(객체)할 때 보여줄 문자열을 정함
    def __repr__(self):
        return f"Brand: {self.brand}, Color: {self.color}"


myTesla = Car("Tesla", "White")  # * 이걸로 인스턴스화
print(myTesla)

# * 인스턴스뿐 아니라 클래스 Car 자체도 파이썬 안에서는 하나의 "객체"로 취급됨 (type(Car)를 찍어보면 <class 'type'>이 나옴)

# * type(이름, 부모클래스들, 속성/메서드딕셔너리): class 키워드 없이 그 자리에서 즉석으로 클래스를 만드는 방법
# * 아래 줄은 "class Car: pass"랑 완전히 똑같은 뜻 (이름="Car", 부모 없음=(), 속성/메서드 없음={})
EVCar = type("Car", (), {})
print(EVCar())  # * 만들어진 클래스를 바로 인스턴스화

# * type(name, bases, attrs) 각 인자의 뜻
# * name: 새로 만들 클래스 이름(문자열) / bases: 상속받을 부모클래스들(튜플) / attrs: 클래스 안에 넣을 속성/메서드(딕셔너리)

# * Create additional method for our new Class


def charge(self):
    return "Charging up"


# * bases=(Car,) -> Car를 상속, attrs에 batter_cap 속성과 charge 메서드를 추가 -> class EVCar(Car): 랑 같은 뜻
EVCar = type("EVCar", (Car,), {"batter_cap": "75KW", "charge": charge})
print(EVCar)

# * Create Instance of EVCar called 'lucid'
myLucid = EVCar("Lucid", "Yellow")

print(myLucid.brand)
print(myLucid.color)
print(myLucid.charge())


# * type을 상속받으면 "클래스를 만드는 클래스"인 메타클래스가 됨 (object를 상속하면 일반 클래스가 되는 것과 대응)
# * __new__: 인스턴스가 만들어지기 직전에 호출되는 메서드 -> 여기선 "새 클래스 객체"를 만들어서 반환함
class Meta(type):
    def __new__(cls, name, bases, attrs):
        return type(name, bases, attrs)


# * Meta("Car", (), {}) -> Meta.__new__가 호출되어 결국 type("Car", (), {})를 실행 -> 새 클래스 Car를 만듦
Car = Meta("Car", (), {})
print(Car)


# * Meta와 달리 bases를 인자로 안 받음 -> 대신 내부에서 항상 Car를 부모로 고정해서 만듦 (자기만의 규칙을 가진 메타클래스)
# * create our Metaclass
class Meta1(type):
    def __new__(cls, name, attrs):
        attrs["shape"] = "sendan"  # * 이 메타클래스로 만드는 모든 클래스에 자동으로 shape 속성을 추가

        # * type(name, (Car,), attrs) -> 항상 Car를 상속하는 클래스로 만들어서 반환
        return type(name, (Car,), attrs)


# * Meta1("EVCar", {}) -> Meta1.__new__(Meta1, "EVCar", {}) 호출됨 (cls=Meta1, name="EVCar", attrs={})
# * __new__ 안에서 attrs에 shape="sendan"을 자동으로 끼워넣고 Car를 상속하는 EVCar 클래스를 만들어서 반환
# * create the EVCar class
EVCar = Meta1("EVCar", {})

# * EVCar가 Car를 상속했으므로 Car의 __init__(self, brand, color)를 그대로 사용
lucid = EVCar("lucid", "Yellow")

print(lucid)  # * Car의 __repr__을 물려받아서 "Brand: lucid, Color: Yellow" 출력

# * shape는 직접 코드에 안 썼지만 Meta1.__new__가 클래스를 만들 때 자동으로 넣어준 값 -> "sendan"
print(lucid.shape)
