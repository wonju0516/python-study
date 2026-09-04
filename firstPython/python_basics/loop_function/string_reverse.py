# reverse string

value = "Hello World"

# * 1. reverse
## ? reverse 함수는 문자열을 리스트로 바꾸어서 reverse 메서드를 사용한 뒤에 ""join으로 다시 문자열을 복구하는 방법
value_list = list(value)
value_list.reverse()
print("".join(value_list))


# * 2. reversed
# ! 이터레이터: 값을 미리 다 안 만들고, next() 호출마다 하나씩 계산해 내놓는 객체
# ? reversed()도 이터레이터 반환 -> print()로 찍으면 <reversed object ...>만 나옴, join()으로 꺼내야 진짜 값 나옴
print("".join(list(reversed(value))))
print("".join(reversed(value)))

# * 3. forloop
# ! range(len(value)-1, -1, -1)의 -1(stop)은 value[-1] 같은 음수 인덱싱이 아니라 그냥 숫자 -1, "0까지 포함하고 멈춰라"는 경계선
# ? i는 4,3,2,1,0 순으로 나오다가 다음 값(-1)은 stop이라 못 주므로 그 시점에 자동 종료
temp_list = []
for i in range(len(value) - 1, -1, -1):
    temp_list.append(value[i])

print("".join(temp_list))

# * 4.  while
value_list = list(value)
temp_list = []
while len(value_list) > 0:
    temp_list.append(value_list.pop())  # ! pop은 맨 뒤 원소부터 꺼내서 반환함

print("".join(temp_list))
