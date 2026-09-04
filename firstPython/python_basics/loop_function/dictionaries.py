# dictionary
# * key value
dic = {"country": "south korea", "city": "seoul", "gender": "male", "age": 25}

print(dic["country"])

# * .items() -> key, value 쌍을 동시에 꺼낼 때 씀 (enumerate는 인덱스+값이라 딕셔너리엔 안 맞음)
for key, value in dic.items():
    print(f"{key}: {value}")

# * for key in dic: -> 딕셔너리를 그냥 순회하면 key만 나옴, value는 dic[key]로 따로 꺼내야 함
for key in dic:
    print(f"{key}: {dic[key]}")

print(dic.keys())
print(
    list(dic.values())
)  # * dict_values 와 같은 타입을 안보이게 하기 위해서는 list로 감싸기

# * in -> 딕셔너리에선 기본적으로 key만 검사함 (value는 검사 안 함) -> "name"이 key로 있는지 확인
print("name" in dic)

dic1 = {  # * 딕셔너리라고 꼭 String만 들어가는건 아니다
    1: 1,
    2: 2,
}

print(dic1[1])
