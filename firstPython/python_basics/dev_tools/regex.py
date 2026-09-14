"""regex.py"""
# * regex = regular expression(정규표현식)의 줄임말
## * 문자열 안에서 특정 패턴(규칙)을 가진 부분을 찾거나, 맞는지 검사하거나, 치환할 때 쓰는 문법
## * 대소문자까지 정확히 일치하는 값을 알아야 함
### ! 정규표현식은 기본적으로 대소문자를 구분함 -> "abc" 패턴은 "ABC"와 매칭 안 됨
### ! 대소문자 구분 없이 찾고 싶으면 re.IGNORECASE 플래그를 따로 줘야 함

import re

txt = "My phone number is 123-1234-1234. Please call me to this phone number"

# * 저 텍스트에서 "number"라는 글자 그대로를 찾기
pattern = "number"
matched = re.search(pattern, txt)
# * txt 전체에서 pattern과 처음 매칭되는 부분을 찾음 (없으면 None)
print(matched)  # * 찾으면 Match 객체(위치+매칭 문자열 담김), 못 찾으면 None 출력

# * (시작, 끝) 인덱스 / 시작 인덱스만 / 끝 인덱스만
print(matched.span())
print(matched.start())
print(matched.end())

# * pattern에 있는거 다 찾아오기 -> 매칭되는 걸 전부 "문자열 리스트"로 반환
matched = re.findall(pattern, txt)
print(matched)
print(len(matched))

# * 매칭되는 걸 전부 "Match 객체"로 하나씩 순회 (위치 정보까지 필요할 때)
for m in re.finditer(pattern, txt):
    print(m.span())

phone = re.search(r"\d\d\d-\d\d\d\d-\d\d\d\d", txt)
# * phone = re.search(r"\d{3}-\d{4}-\d{4}", txt)
print(phone)
print(phone.group())  # * 매칭된 문자열 전체 -> 괄호 없이 쓰면 .group(0)과 동일

# ? detail with group
# * 패턴을 미리 컴파일해두고 재사용 (그냥 문자열로 넘겨도 되지만, 반복 사용 시 유용)
pattern = re.compile(r"(\d{3})-(\d{4})-(\d{4})")
output = re.search(pattern, txt)
## * index starts from 1
print(output.group(1))
# * 첫 번째 괄호(그룹)에 매칭된 부분만 추출 -> group(0)은 전체 매칭

r = re.search(r"cat|dog", "cats and dogs")
print(r)

r = re.findall(r".at", "The person wearing the the hat sat in the shade")
print(r)

r = re.findall(r"^\d", "1 person wearing the hat sat in the shade2")
print(r)

r = re.findall(r"[^!.?]+", "Jesus! Hello World. Typical?")
print(r)

r = re.findall(r"[\w]+-[\w]+", "Here is hypen-string")
print(r)

r = re.findall(r" (cat|sat|hat)", "person holding a cat sat wearing at hat")
print(r)
