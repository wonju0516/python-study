# loop

alphabets = [
    "a",
    "b",
    "c",
    "d",
]  # * 리스트에 있는 모든 요소를 하나씩 꺼내와서 반복문 작성


# * for 값 in 리스트/문자열 -> 값 자체를 쓸 때 (인덱스 필요없음)
for alphabet in alphabets:
    print(alphabet)
    print(f"{alphabet} is char")

for char in "South Korea":  # * 문자열은 글자하나씩 들어감
    print(char, end=" /")

print()

# * average value
numbers = [1, 2, 3, 4]
sum = 0
for number in numbers:
    sum += number
print(sum / len(numbers))


# * max value
numbers = [1, 2, 3, 4]
max_num = 0
for number in numbers:
    # if number > max_num:
    #     max_num = number
    max_num = max(max_num, number)
print(max_num)

## ! 최대값을 구하려면 라이브러리 함수로도 구할 수 잇음 max()로
print(max(numbers))
print(max(1, 5))  # * 저 안에 들어있는 것중에 큰값을 뽑기도 가능함


# * for i in range(N) -> 인덱스 번호가 필요하거나, 값 상관없이 정해진 횟수만큼 반복할 때
for j in range(1, 11):  # * 1에서부터 10까지 (11-1)
    sum += j

print(sum)


# * odd number ? -> 홀수만 따로 저장하기?

for i in range(1, 11, 2):  # * range(시작, 끝, step(얼마나 건너 뛸지))
    print(i)

# * enumerate(리스트) -> 인덱스와 값이 "둘 다" 필요할 때 range(len(...))보다 깔끔한 방법
for i, alphabet in enumerate(alphabets):
    print(i, alphabet)  # 0 a / 1 b / 2 c / 3 d
