# 동전 앞뒤 맞추기
import random

random_value = random.randint(0, 10)
if random_value % 2 == 0:
    print("you get head")
else:
    print("you get tail")
