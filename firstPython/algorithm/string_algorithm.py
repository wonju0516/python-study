# string algorithm

# * 애너그램 (Anagram)
# ? 같은 글자들을 순서만 다르게 재배열한 단어 (문자의 순서와 대소에 관계없이 똑같은 문자들로 구성되면 애너그램)
# ? 문자열 s1과 s2가 애너그램인지 판단하는 알고리즘


def is_anagram(s1, s2):
    s1 = s1.replace(
        " ", ""
    ).lower()  # * replace로 띄어쓰기 공백을 지워버림 -> lower로 소문자로 통일
    s2 = s2.replace(" ", "").lower()
    if sorted(s1) == sorted(s2):  # * 알파벳 순으로 정렬해서 결과가 똑같은지 비교
        return True
    else:
        return False


s1 = "Emperor Octavian"
s2 = "Captain over Rome"
print(is_anagram(s1, s2))
