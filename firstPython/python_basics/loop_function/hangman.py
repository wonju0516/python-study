# hangman
# * here is the word [_,_,_,_,_,_]
# ? guess the char? -> 그냥 단어 맞추기 게임이라고 생각하면 됨 한글자씩 한글자씩

answer = list("batman")
lst = []
for i in range(len(answer)):
    lst.append("_")
print("Here is the word")
print(lst)
num_of_try = 10
while True:
    char = input("Guess the char?")
    for i, elem in enumerate(answer):
        if elem == char:
            lst[i] = char
    print(lst)

    if "_" not in lst:
        print("You won")
        print("".join(lst))
        break
    if num_of_try < 1:
        print("You lost")
        break
    num_of_try -= 1
