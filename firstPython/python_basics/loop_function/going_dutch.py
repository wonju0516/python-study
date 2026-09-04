# going_dutch
num_of_people = 3
food_prices = [10, 20, 15, 17, 50]


def going_dutch(food_prices: list, num_of_people: int):
    total = 0
    for food_price in food_prices:
        total += food_price
    print(f"Your total is {total}")
    return total / num_of_people


bill = going_dutch(food_prices, num_of_people)
print(bill)
