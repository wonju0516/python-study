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

    # ! sorted(s1) == sorted(s2) 자체가 이미 True/False 값을 만들어냄
    # ! 그래서 그걸 다시 if로 감싸서 True면 True 반환, False면 False 반환 굳이 할 필요 없음
    # ! 조건식이 곧 반환하고 싶은 값 그 자체라서, if/else 없이 조건식을 바로 return 하면 결과가 동일함

    # * return sorted(s1) == sorted(s2)


s1 = "Emperor Octavian"
s2 = "Captain over Rome"
print(is_anagram(s1, s2))

# * 팰린드롬 (Palindrome)
# ? 앞에서 읽으나 거꾸로 읽으나 똑같은 단어
# ? 판단 방법 1. 문자열을 복사해 순서를 뒤집은 다음 원래 문자열과 비교하는 것
print("blackswan"[::-1])
# ! 문자열[start:stop:step]
# ! start 어디서부터 시작? (생략하면 처음부터)
# ! stop 어디까지? (생략하면 끝까지 (처음 인덱스는 포함안됨))
# ! step 몇 칸씩 건너뛸지 (생략하면 기본값 1)


# ? 이제 문자열이 팰린드롬인지 체크하는 코드
def is_palindrome(s1):
    if (
        s1.lower() == s1[::-1].lower()
    ):  # * lower()로 소문자로 변경, 슬라이스 문법으로 뒤집어 원래 문자열과 비교
        return True
    return False


# * 마지막 숫자 (리스트 축약 문법)
# ! new_list = [expression(i) for i in iterable if filter(i)]
# ? expression(i) - i를 가지고 계산해서 새 리스트에 넣을 값
# ? iterable - 새로운 리스트를 만들기 위한 재료
# ? filter(i) - 기존 이터러블 리스트의 일부를 수정할 때 사용

print([c for c in "selftaught"])

print([c for c in "selftaught" if ord(c) > 102])
# * ord -> 문자의 ASCII 코드를 반환함

# ? 이를 이용해 문자열에서 숫자만 뽑아내기도 가능함
s = "Buy 1 get 2 free"
nl = [c for c in s if c.isdigit()]
print(nl)

# ? 그럼 새로운 리스트에 마지막 숫자를 찾는 가장 간단한 방법?
nl = [c for c in s if c.isdigit()][-1]
print(nl)

# * 시저의 암호 (Cipher)
# ? 하나의 숫자를 선택하고 메시지의 모든 문자를 그 숫자만큼 이동시켜 새로운 메시지를 만드는 것

import string


def cipher(a_string, key):
    uppercase = string.ascii_uppercase  # ? "ABC...Z"
    lowercase = string.ascii_lowercase  # ? "abc...z"
    encrypt = ""  # ? 나중에 암호화될 문자열을 담을 변수
    for c in a_string:
        if c in uppercase:  # ! 문자가 대문자면 이쪽에서
            new = (
                (uppercase.index(c) + key) % 26
            )  # * 원래 위치 + key만큼 이동, 26 넘으면 다시 처음부터 (알파벳 갯수가 26)
            encrypt += uppercase[new]  # * 문자열 자체도 인덱싱은 가능함
        elif c in lowercase:  # ! 문자가 소문자면 이쪽에서
            new = (lowercase.index[c] + key) % 26
            encrypt += lowercase[new]
        else:  # ! 특수문자인 경우이므로 바꾸지 않고 저장
            encrypt += c

    return encrypt


# ? 파이썬의 리스트 축약 문법을 사용해 다음의 리스트에서 다섯 글자 이상인 단어만 반환해보기
a_list = [
    "selftaught",
    "code",
    "sit",
    "eat",
    "programming",
    "dinner",
    "one",
    "two",
    "coding",
    "a",
    "tech",
]
nl = [c for c in a_list if len(c) >= 5]
print(nl)
