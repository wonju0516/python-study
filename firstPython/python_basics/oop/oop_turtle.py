# oop
import time

# * from 모듈 import 이름 -> 모듈 전체가 아니라 그 안의 특정 이름만 콕 집어 가져옴 (접두어 없이 바로 사용 가능) -> 이름은 클래스일수도 함수일수도 그냥 변수일수도 있음
# * 지금처럼 그 이름이 클래스(Turtle)면, 그 클래스 안에 있는 메소드들도 전부 같이 딸려옴 (메소드는 모듈이 아니라 클래스에 속한 것이기 때문)
# * import time처럼 모듈 전체를 가져오면 time.sleep()처럼 접두어를 붙여야 함
from turtle import Turtle

# * 클래스(class) = 객체를 찍어내는 설계도. Turtle이 클래스
john = Turtle()  # * 객체/인스턴스 = 클래스로 실제로 찍어낸 것. john이 Turtle의 인스턴스
print(john)
john.shape(
    "turtle"
)  # * 메소드 = 클래스 안에 정의된, 그 객체에 소속된 함수 -> 거북이 모양 아이콘으로 변경
john.color("red", "green")  # * 메소드: 펜 색/채우기 색 지정
while True:
    john.forward(5)  # * 메소드: 앞으로 5만큼 이동
    john.left(5)  # * 메소드: 왼쪽으로 5도 회전
    # ! time.sleep()은 메소드처럼 보이지만 함수임 -> time은 객체가 아니라 모듈, sleep은 그 안의 독립 함수
    time.sleep(1)  # * 1초간 멈춤
