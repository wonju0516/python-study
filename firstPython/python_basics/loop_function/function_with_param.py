# function with param
def travel_to_country(country: str):
    print("Hello there!")
    print(f"You are going to travel to {country}")
    print("Are you excited?")


travel_to_country("USA")

## * keyword argument
travel_to_country(country="USA")


def travel_to_country_name(
    country: str, name: str
):  # * :str -> 타입힌트 => 넣으면 더 좋긴함
    print(f"Hello {name}")
    print(f"You are going to trabel to {country}")
    print("Are you excited?")


travel_to_country_name("USA", "Joon")

## * keyword argument -> 보통 이리 많이씀
travel_to_country_name(name="mok", country="KOREA")

# * function return
## ? 함수는 항상 한가지 value를 리턴할 필욘 없다!! -> 함수가 블랙박스라고 생각하면 됨 -> input값이  어떤식을오 들어오냐에 따라서 그 결과 값이 달라질 수 있음


def get_name(first_name, last_name):
    if first_name == "":
        return "Your first name is missing.."
    if last_name == "":
        return "Your last name is missing.."
    return f"{first_name}, {last_name}"


value = get_name(
    first_name=input("Your first name?"), last_name=input("your last_name?")
)

print(value)
