# input

# * input()은 두 가지 일을 함: 1) 괄호 안 문자열을 화면에 프롬프트로 출력  2) 사용자가 입력한 값을 문자열로 반환(return)
# ! input()만 쓰면 프롬프트만 뜨고, 사용자가 입력한 값(예: 25)은 반환만 될 뿐 화면에 안 찍히고 사라짐
# ? 그래서 입력받은 값을 눈으로 보려면 print()로 감싸서 반환값을 넘겨받아 출력해야 함
print(input("What is your age?"))

print("My name is " + input("How Are you? what is your name?"))

print(len(input("what is your name?")))

# ! 보통은 변수에 저장해서 나중에 계산이나 조건문 등에 재사용함

age = input("What is your age?")  # * 입력값을 변수에 저장 (아직 화면에 안 뜸)
print(age)  # * 필요할 때 출력
print("나이는 " + age + "살입니다")  # * 다른 연산에도 재사용 가능

# ! 요즘은 f-string을 많이 씀
# ! +는 문자열끼리만 가능해서 숫자면 str로 변환해야함 -> f-string은 타입 상관없이 {} 안에 넣으면 됨
print(f"나이는 {age}살입니다.")
