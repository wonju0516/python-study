# * 스페셜/매직/던더 메소드: 이름이 __xxx__ 형태인 메소드. 특정 상황(print, len, == 등)에서 파이썬이 자동으로 호출해줌


class Tesla:
    def __init__(self, owner, color):
        self.owner = owner
        self.color = color

    # * __str__: print(객체) / str(객체) 할 때 보여줄 문자열을 정함 (사용자용 표현)
    def __str__(self):
        return f"This is {self.color} color {self.owner}'s car"

    # * __repr__: repr(객체) 할 때, 또는 __str__이 없을 때 print(객체)에서 쓰일 문자열 (개발자용 표현, 디버깅 목적)
    # * 보통 "이 문자열을 eval()하면 똑같은 객체가 다시 만들어진다"는 형태로 작성하는 게 관례
    def __repr__(self):
        return f"Tesla(owner={self.owner!r}, color={self.color!r})"

    # * __len__: len(객체) 했을 때 반환할 값을 정함
    def __len__(self):
        return len(self.owner)

    # * __del__: 객체가 메모리에서 삭제(소멸)될 때 자동으로 실행됨 ("destructor")
    def __del__(self):
        print("This car has been deleted")

    # * __eq__: 객체1 == 객체2 비교의 기준을 정함. 안 쓰면 기본적으로 "완전히 같은 객체(메모리 주소)"일 때만 True
    # * other: 그냥 파라미터 이름일 뿐 -> self처럼 관례일 뿐이라 다른 이름으로 바꿔도 동작은 똑같음
    def __eq__(self, other):
        return self.color == other.color


tesla = Tesla("Joon", "White")
print(tesla)  # * __str__이 있으면 print()는 __str__ 결과를 씀
print(repr(tesla))  # * repr()은 __str__이 있어도 항상 __repr__ 결과를 씀
# del tesla

tesla1 = Tesla("Aain", "White")
print(tesla == tesla1)
del tesla1  # * tesla1을 여기서 명시적으로 삭제 -> __del__ 1번째 실행

# * 스크립트가 끝나면서 남아있던 tesla도 자동으로 정리됨 -> __del__ 2번째 실행
# * 그래서 "This car has been deleted"가 총 2번 출력됨
