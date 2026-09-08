# dictionary comprehension: {key표현식: value표현식 for (key, value) in 딕셔너리.items() if 조건}
# * list comprehension이랑 원리는 같음, 대괄호[] 대신 중괄호{}에 "key: value" 쌍을 넣는 것만 다름

incorrect_score_dict = {"Tom": 80, "Lisa": 75, "Sarah": 90}

# * .items(): 딕셔너리를 (key, value) 쌍으로 순회하게 해주는 메소드
# * 조건(score < 80)은 원본 score 값으로 먼저 판단함 -> 통과한 것만 score + 5가 적용됨 (+5 한 뒤에 비교하는 게 아님)
correct_score_dict = {
    name: score + 5 for (name, score) in incorrect_score_dict.items() if score < 80
}

print(correct_score_dict)
