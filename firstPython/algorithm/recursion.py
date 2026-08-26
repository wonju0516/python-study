# recursion.py
# * 팩토리얼을 계산하는 반복 알고리즘
def factorial(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n = n - 1
    return the_product


# * 같은 알고리즘을 재귀 알고리즘으로 변경
def factorial_2(n):
    if n == 0:
        return 1
    return n * factorial_2(n - 1)


# ! def - 함수를 만들다는 키워드
# ! factorial - 이 함수의 이름
# ! (n) - 이 함수가 받을 매개변수


# todo : 1부터 10까지의 숫자를 재귀로 출력해보시오.
def factorial_3(n):
    if n == 0:
        return 1
    return n * factorial_3(n - 1)


print(factorial_3(10))

# ! if문 안에 return이 있어서 조건이 참이면 함수가 그 즉시 끝나버린다.
# ! 그래서 아래에 있는 return n * factorial_2(n - 1)은
# ! "n == 0이 아닐 때만" 실행되는 코드가 된다 (else와 같은 효과).
# ! 이런 식으로 return으로 미리 끝내버리는 걸 early return이라고 부른다.
