# list (리스트)
# ? 여러 값을 순서대로 묶어 둘 때 사용

countries = ["South Korea", "USA", "Japan", "China"]
print(countries)

countries[2] = "Vietnam"  # * 인덱스로 값 바꾸기 (Japan -> Vietnam)
print(countries)

element = "c"
alphabets = ["b", element, "d"]
print(alphabets)

alphabets.append("e")  # * 맨 뒤에 추가
print(alphabets)

alphabets += ["f", "g"]  # * 리스트끼리 이어붙이기
print(alphabets)

alphabets.insert(0, "a")  # * 원하는 인덱스에 끼워넣기
print(alphabets)

print(countries[0])  # * 첫 번째
print(countries[-1])  # * 마지막 (-1은 뒤에서 첫 번째)

print(countries.pop())  # * 마지막 삭제 + 그 값을 돌려줌
print(countries)

print(countries.pop(0))  # * 인덱스를 넣으면 그 자리 삭제
print(countries)


# --- 코테에서 append / insert / pop 다음으로 자주 쓰는 것들 ---

nums = [3, 1, 4, 1, 5, 9, 2]

# * len(리스트) -> 길이 (거의 모든 문제에 나옴)
print(len(nums))

# * in -> 값이 있는지 확인 (if x in 리스트)
print(1 in nums)  # True
print(7 in nums)  # False

# * 슬라이싱 [시작:끝] -> 끝 인덱스는 포함 안 됨
print(nums[1:4])  # [1, 4, 1]
print(nums[:3])  # 앞에서 3개
print(nums[-2:])  # 뒤에서 2개
print(nums[::-1])  # * 뒤집기 (코테에서 매우 자주 씀)

# * count(값) -> 그 값이 몇 개인지
print(nums.count(1))  # 2

# * index(값) -> 그 값이 처음 나오는 위치
print(nums.index(4))  # 2

# * remove(값) -> 그 값 "첫 번째"만 삭제 (인덱스가 아니라 값으로 지움)
nums.remove(1)
print(nums)  # [3, 4, 1, 5, 9, 2]  <- 앞의 1만 지워짐

# * extend(리스트) -> 다른 리스트를 뒤에 통째로 붙임 (+= 와 같음)
nums.extend([6, 7])
print(nums)

# * sort() -> 원본을 오름차순으로 정렬 (반환값 없음)
nums.sort()
print(nums)

nums.sort(reverse=True)  # * 내림차순
print(nums)

# * sorted(리스트) -> 원본은 그대로 두고, 정렬된 새 리스트를 줌
original = [3, 1, 2]
print(sorted(original))  # [1, 2, 3]
print(original)  # [3, 1, 2]  <- 원본 안 바뀜

# * reverse() -> 원본을 뒤집음 (반환값 없음)
original.reverse()
print(original)  # [2, 1, 3]

# * min / max / sum -> 최솟값, 최댓값, 합 (숫자 리스트에서 거의 매번 씀)
scores = [10, 40, 20, 30]
print(min(scores), max(scores), sum(scores))

# * enumerate -> (인덱스, 값)을 같이 꺼낼 때
for i, n in enumerate(scores):
    print(i, n)

# * join -> 문자열 리스트를 하나로 합침 (문자열 문제에 자주 나옴)
words = ["a", "b", "c"]
print("".join(words))  # abc
print("-".join(words))  # a-b-c
