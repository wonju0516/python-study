free_book = False
# * customers는 "복수" -> 문자열 여러 개를 담은 리스트
customers = ["Lexi", "Britney", "Danny", "Bobbi", "Chris"]

# * for문이 한 바퀴 돌 때마다 customers 리스트에서 원소를 하나씩 꺼내
# * customer(단수) 변수에 그대로 담아준다. 즉 customer는 리스트가 아니라
# * "Lexi", "Britney" 같은 문자열 하나다.

for customer in customers:
    # ! customer는 문자열이고, 문자열도 리스트처럼 인덱싱이 가능하다.
    # ! 따라서 customer[0]은 customers 리스트의 인덱스가 아니라
    # ! customer 문자열의 "첫 번째 글자"를 뜻한다. (customer="Bobbi"면 customer[0]은 "B")
    # ? 즉 이 줄은 "이름의 첫 글자가 B인가?"를 묻는 조건문이다.
    # ? [0]을 빼고 customer == "B"라고 하면 이름 전체가 "B" 한 글자인지 비교하게 되어
    # ? 항상 False가 나온다.
    if customer[0] == "B":
        print(customer)

# ! range(시작, 끝) 끝 숫자는 포함안함  그 전까지만!!
