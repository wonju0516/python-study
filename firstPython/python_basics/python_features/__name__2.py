import __name__1

# * import하는 순간 __name__1.py 코드가 통째로 실행됨 -> 그 안의 __name__은 "__main__"이 아니라 "__name__1"이라 else 분기를 탐

# * 이 파일은 직접 실행됐으니 여기서의 __name__은 "__main__" -> if 분기를 탐
if __name__ == "__main__":
    print("__name__2.py has run directly")
else:
    print("__name__2.py has imported")
