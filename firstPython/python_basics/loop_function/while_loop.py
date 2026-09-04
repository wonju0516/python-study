# while loop

# * for
## ? for action in list_of_actions:
## ?    do action

# * while
## ? while condition is True:
## ?    do action

value = 5
while value > 0:
    print(value)
    value -= 1

# ! while True는 보통 인피니트 루프로 많이 사용함

# * while True -> C언어의 while(1)처럼 무한 반복 (조건 없이 항상 참)
# ! break로 직접 빠져나오지 않으면 영원히 반복됨
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:  # * 조건 만족하면 반복문 강제 종료
        break
