# * nesting(중첩) -> 리스트/딕셔너리 안에 또 다른 리스트/딕셔너리가 요소로 들어있는 것
usa = {"name": "USA", "contient": "North America"}

south_korea = {"name": "South Korea", "continent": "East Asia"}

countries = [usa, south_korea]  # * 1단계 중첩 -> 리스트 안에 딕셔너리 2개


for country in countries:
    print(country)
    print(country["name"])

california = ["los angeles", "san francisco"]
us_state = [california, "washington", "oregon"]  # * 2단계 중첩 -> 리스트(california) 안에 또 리스트

# ! 오버라이트(overwrite) -> countries에 이미 값이 있었는데, 새 값을 다시 대입해서 이전 값을 덮어씀
# ? 파이썬은 타입 체크 없이 그냥 받아들여서, 완전히 다른 구조(3단계 중첩)로도 덮어쓸 수 있음
countries = [us_state, south_korea]  # * 3단계 중첩 -> 그 리스트를 또 리스트에 담음

print(countries)
