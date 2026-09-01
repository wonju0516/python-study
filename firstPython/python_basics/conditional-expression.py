# condition
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
