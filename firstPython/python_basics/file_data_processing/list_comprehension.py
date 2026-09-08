# list comprehension: [표현식 for 변수 in 반복가능한것] 형태로 반복문+리스트 생성을 한 줄로 줄이는 문법
# * 표현식 = 결과 리스트에 실제로 넣고 싶은 값(계산식)

country_list = ["USA", "South Korea", "Japan"]

# * 일반 for문 방식
lower_case_list = []
for country in country_list:
    lower_case_list.append(country.lower())

print(lower_case_list)

# ! 위 for문을 list comprehension으로 변환한 것 (같은 결과, 한 줄로 압축)
new_lower_case_list = [country.lower() for country in country_list]

print(new_lower_case_list)

# * 문자열도 반복 가능한 것(iterable)이라 한 글자씩 순회하며 리스트로 만들 수 있음
sample = "silicon valley"
print([ch for ch in sample])

# * 조건이 붙은 list comprehension: [표현식 for 변수 in 반복가능한것 if 조건]
# * sample > 1(조건)을 만족하는 값만 골라서, 그 값을 sample * 2(내가 넣고 싶은 값=표현식)로 바꿔서 넣음
sampling = [2, 3, 1, 1, 2, 3, 4]
filtered_sampling = [sample * 2 for sample in sampling if sample > 1]

print(filtered_sampling)
