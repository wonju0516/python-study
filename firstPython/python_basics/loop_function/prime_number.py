# prime number -> 소수 (자기 자신과 1로 제외하고 나누어지는게 없는 수)


def is_prime_number(num: int):
    count = 0
    if num > 1:
        for n in range(2, num):
            if num % n == 0:
                count += 1
        if count > 0:
            return print("not prime number")
        else:
            return print("prime number")
    else:
        return print("1이하여서 안됨")


is_prime_number(5)
