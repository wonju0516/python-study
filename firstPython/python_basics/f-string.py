# f-string

# * Old age -> 옛날 방식 (% 포맷팅), .format()
name = "Joon"
age = 30
print("Hello, %s." % name)


# * print("Hello, {}. I am {}.".format(name, age))
# * print("Hello, {1}. I am {0}.".format(age, name))

# * 딕셔너리 사용 -> .format()은 {} 안에 변수 이름 대신 "키 이름"을 적고, .format(키=값)으로 채워 넣는 방식
person = {"name": "Joon", "age": 17}
# ? name=person["name"], age=person["age"] -> 딕셔너리에서 값을 하나씩 꺼내서 각 키에 직접 대입해줌
print("Hello, {name}. I am {age}.".format(name=person["name"], age=person["age"]))

# ! **person -> 딕셔너리를 "키=값" 쌍으로 통째로 풀어서(unpacking) 넘겨주는 문법
# ! 즉 **person은 name=person["name"], age=person["age"]를 일일이 적은 것과 동일한 결과
# ? 딕셔너리의 키 이름이 문자열 안 {키} 이름이랑 똑같아야 자동으로 매칭됨
print("Hello, {name}. I am {age}.".format(**person))

# * f-string
print(f"Hello, {name}. I am {age}.")
print(f"Hello, {name}. I am {age}.")
print(f"{name.lower()} is cool.")
