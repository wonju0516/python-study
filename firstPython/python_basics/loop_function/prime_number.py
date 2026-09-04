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


def is_prime_number2(num: int):
    if num > 1:
        is_divisible = False
        for n in range(2, num):
            if num % n == 0:
                print(f"{num} can be cleanly divided by {n}.")
                is_divisible = True
                break
        if is_divisible:
            print("Snap! it is not the prime number")
        else:
            print(f"Congrat! {num} is a prime number")
    else:
        print(f"{num} is not the prime number")


is_prime_number2(6)
