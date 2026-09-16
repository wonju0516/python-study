a = 10
b = 20

# * = -> "변수명=값" 형태로 자동으로 찍어주는 디버깅용 트릭 (a=10, b=20)
print(f"{a=}, {b=}")

num = 100

# * decimal places -> .2 = 소수점 2자리까지, f(fixed-point) = "소수점 고정 표기로 보여줘라"를 정하는 타입 지정자
print(f"num: {num:.2f}")  # * num: 100.00

# * hex -> x = 16진수로 변환하는 타입 지정자
## ! 0x -> "이 숫자는 16진수다"라고 사람이 알아보게 붙이는 범용 접두어 관례 (0b=2진수, 0o=8진수도 동일한 방식)
## * # -> 그 0x 접두어를 자동으로 붙여주는 플래그
print(f"hex: {num:#0x}")  # * hex: 0x64

# * binary -> b = 2진수로 변환하는 타입 지정자
print(f"binary: {num:b}")  # * binary: 1100100

# * octal -> o = 8진수로 변환하는 타입 지정자
print(f"octal: {num:o}")  # * octal: 144

# * scientific -> e = 과학적 표기법(지수 표기), 기본 소수점 6자리까지 표시
print(f"scientific: {num:e}")  # * scientific: 1.000000e+02

# * add padding -> 0 = 빈 자리를 0으로 채우는 플래그, 9 = 전체 자릿수(폭)를 9자리로 맞춤
print(f"Number:{num:09}")  # * Number:000000100

import datetime

# * tz 인자에 UTC를 명시적으로 지정
today = datetime.datetime.now(tz=datetime.timezone.utc)

print(f"current : {today}")  # * current : 2026-09-16 10:53:28.067434+00:00 (기본 형식 그대로 출력)
# * datetime 객체도 f-string의 : 뒤에 형식 지정자를 쓸 수 있음 (%m %d %Y %H %M %S -> 각각 월/일/년/시/분/초)
print(f"current : {today:%m/%d/%Y %H:%M:%S}")  # * current : 09/16/2026 10:53:28

from dataclasses import dataclass


# * @dataclass -> __init__, __repr__ 등을 자동으로 만들어주는 데코레이터
## ! 원래는 __init__(self, brand, model): self.brand = brand; self.model = model 을 직접 써야 하는데, 그걸 생략 가능하게 해줌
@dataclass
class Car:
    brand: str  # * 타입 힌트가 곧 필드 선언 -> 이 두 줄만으로 생성자 인자가 됨
    model: str

    def __str__(self) -> str:  # * print()나 f-string에 들어갈 때 보여줄 형태를 직접 커스터마이징
        return f"{self.brand} has {self.model}"


model3 = Car("Tesla", "Model 3")  # * @dataclass 덕분에 직접 만든 __init__ 없이도 이렇게 생성 가능
print(f"{model3}")  # * Tesla has Model 3 -> __str__에서 정의한 형태로 출력됨
