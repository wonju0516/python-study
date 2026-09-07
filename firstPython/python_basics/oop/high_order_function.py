# high order function
# * 함수가 "일급 객체(first-class citizen)"라서 고차함수가 가능함 -> 그 근거가 되는 5가지 특징
# * 1. 함수는 Object(객체) 타입의 인스턴스다
# * 2. 함수를 변수에 저장할 수 있다
# * 3. 함수를 다른 함수의 파라미터로 넘길 수 있다
# * 4. 함수 안에서 함수를 반환할 수 있다
# * 5. 함수를 해시 테이블(딕셔너리) 같은 자료구조에 저장할 수 있다


def add(num1, num2):
    return num1 + num2


# add2 = add  # * () 없음 = 함수 자체를 add2에 저장 -> 위 2번 특징의 예시


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2, is_floor=True):
    if is_floor:
        return num1 // num2
    else:
        return num1 / num2


def calc(num1, num2, func):
    return func(num1, num2)


print(calc(10, 5, add))  # * () 없음 = 함수 자체 전달 -> calc 안에서 func(num1, num2)로 호출됨

# * 데코레이터(Decorator)
# * 원본 코드를 바꾸지 않고, 다른 함수를 감싸서 기능을 확장하는 것


def higher_order_example(func):

    def inside():
        print("start ...")
        func()
        print("end ...")

    return inside  # * () 없음 = 함수 자체 반환, () 있음 = 실행 결과 반환


@higher_order_example
# * @데코레이터이름 -> 바로 아래 함수(sample_example)를 자동으로 그 함수의 인자로 넘겨서 실행
# * sample_example = higher_order_example(sample_example)와 같은 뜻 (파라미터 이름이 꼭 func일 필요는 없음, 그냥 첫 자리에 들어가는 것)
def sample_example():
    print("I am inside")


sample_example()  # ! 데코레이터 적용 후 sample_example은 사실 inside 함수로 교체된 상태 -> 진짜로 "실행"시키는 거라 ()가 필요함
