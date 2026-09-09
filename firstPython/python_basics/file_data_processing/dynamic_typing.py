# dynamic typing: 파이썬이 타입을 다루는 방식에 대한 개념 정리
# * dynamic typing vs static typing vs strong typing - 서로 다른 축이라 헷갈리기 쉬움

# * Dynamic typing (동적 타이핑): 타입이 변수가 아니라 "값(객체)"에 붙어있음
x = 5
print(type(x))  # ! <class 'int'>
x = "hello"
print(type(x))  # ! <class 'str'> -> 같은 변수 x인데 타입이 바뀜, 에러 안 남

# * Static typing (정적 타이핑): 파이썬은 이 방식이 아님. 참고로 Java/C는 아래처럼 동작함(파이썬 코드 아님)
## * int x = 5;
## * x = "hello";  // 컴파일 에러! x는 처음부터 int 타입으로 고정됨

# * Strong typing (강한 타이핑): 연산할 때 타입이 안 맞으면 자동으로 안 섞이고 에러남
try:
    print("5" + 5)
except TypeError as e:
    print(f"에러 발생: {e}")  # ! 문자열 + 숫자를 암묵적으로 안 바꿔줌

print(str(5) + "5")  # ! "55" - 직접 변환해야만 합쳐짐 (str(5)로 숫자를 문자열로 바꿈)

# * 정리: 파이썬 = 동적 타이핑(변수 타입 고정 안 됨) + 강한 타이핑(타입 안 맞으면 에러)
# * 참고로 JS는 약한 타이핑이라 "5" + 5를 하면 에러 없이 "55"로 자동 변환됨 (파이썬과 다른 점)
