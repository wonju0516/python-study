# * pprint
# * 중첩 딕셔너리/리스트를 보기 좋게 출력

cars = {
    "tesla": {"models": "sedan", "model3": "sedan", "modelx": "suv", "modely": "suv"}
}

from pprint import pprint

pprint(cars)  # * 줄바꿈/들여쓰기 적용
print(cars)


# * Walrus Operator(왈러스 연산자, :=): 변수 대입 + 그 값 사용을 한 줄에서 동시에 처리

num = [1, 2, 3, 4, 5]
description = {
    "length": (num_length := len(num)),
    "sum": (num_sum := sum(num)),
    "mean": num_sum / num_length,  # * 위에서 왈러스로 만든 변수 재사용
}

print(description)

# * ljust/rjust/center: 지정 길이로 맞추고 남는 공간을 공백으로 채움

print("|" + "hello world".ljust(30) + "|")  # * ljust: 글자를 왼쪽에, 공백은 오른쪽에
print("|" + "hello world".rjust(30) + "|")  # * rjust: 글자를 오른쪽에, 공백은 왼쪽에
print("|" + "hello world".center(30) + "|")  # * center: 글자를 가운데에, 공백은 양쪽에

# * pickle: 파이썬 객체를 파일로 저장/복원 (json과 달리 파이썬 전용, 사람은 못 읽음)
