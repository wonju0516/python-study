# condition
# * single

if 10 > 20:  # * 조건에 맞으면 True가 나옴
    print(True)
elif 10 > 11:  # * 이 조건에 맞으면 Hello 출력
    print("Hello")
else:  # * 저 조건 이외에 다른 것들은 False가 나옴
    print(False)

if int(input("How tall are you in cm?")) > 180:
    print("You are over 180")
else:
    print("you are less than 180")

# * multiple
my_money = 100
if my_money > 0:
    print(f"My money, {my_money} is also greater that 0")

    if my_money > 10:
        print(f"My money, {my_money} is also greater than 10")

    if my_money > 20:
        print(f"My money, {my_money} is also greater than 20")

    else:
        print(f"My money, {my_money} is less than equal to 20")

# * elif -> 조건들이 서로 배타적이라 하나만 참이면 나머지는 검사 안 하고, 딱 하나만 실행됨
# ! my_money = 100이면 "20 초과"만 출력되고 끝 -> 10 초과인지 0 초과인지는 아예 확인도 안 함
if my_money > 20:
    print(f"My money, {my_money} is greater than 20")
elif my_money > 10:
    print(f"My money, {my_money} is greater than 10")
elif my_money > 0:
    print(f"My money, {my_money} is greater than 0")
else:
    print(f"My money, {my_money} is less than equal to 0")
