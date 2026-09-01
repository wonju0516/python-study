# primitive_data_type
# * Integers
profile_number = 2030
print(profile_number)

# * Floats(Decimal Point)
score = float(59)
print(score)

# * Boolean (True or False)
is_correct = True

# * String(str) -> 문자열, 즉 텍스트(글자) 데이터 타입. 따옴표로 감싼 값은 다 문자열
teacher_name = "Cisca"  # ? "..." 한 쌍 -> 한 줄짜리 일반 문자열
course_name = "CSC"

# ! """ (큰따옴표 3개) -> 여러 줄 문자열(multi-line string), 줄바꿈을 그대로 포함해서 저장 가능
# ! 일반 "..."는 안에서 줄바꿈하면 문법 에러가 나서, 여러 줄 텍스트를 담고 싶을 때 """를 씀 (\n 해서 해도 됨)
# ? lecture_name의 실제 값 -> "\nCisca\nOladipo\n" (맨 앞뒤 줄바꿈 포함, 두 줄이 줄바꿈으로 이어진 하나의 문자열)
lecture_name = """
Cisca
Oladipo
"""
print(lecture_name)


# * String subscript
print(teacher_name[1])  # ? 문자열에서는 인덱스를 주면 문자열에서 글자 위치로 보면 됨

# * check object type
print(type(profile_number))
