# * __name__: 모든 모듈(.py 파일)이 자동으로 갖는 내장 변수
# * 이 파일을 직접 실행하면 __name__ == "__main__", 다른 파일에서 import되면 __name__ == 파일명("__name__1")


def my_func1():
    print("myfunc")


# * 직접 실행일 때만 아래 블록이 돔 -> import돼서 쓰일 때는 테스트/예제 코드가 같이 실행되는 걸 막아줌
if __name__ == "__main__":
    print("__name__1.py has run directly")
else:
    print("__name__1.py has imported")
