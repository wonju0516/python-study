# * file management (파일 관리)

# ! 이 파일은 항상 "터미널이 file_data_processing 폴더에 있는 상태"에서 실행해야 함
# ! (터미널에서 cd로 이 폴더까지 이동한 다음 실행)\

# TODO: 실무 정석은 아래처럼 pathlib으로 경로를 고정하는 것 (나중에 배우면 이 방식으로 바꿔야 함)

from pathlib import Path

BASE_DIR = Path(__file__).parent  # 이 파일이 있는 폴더 경로
# readme_path = BASE_DIR / "README.txt"      # 폴더 + 파일명을 합침
# writeme_path = BASE_DIR / "WRITEME.txt"    # 파일마다 이런 식으로 하나씩 만들어두면 됨
# open(readme_path, "r")                     # 실행 위치 상관없이 항상 이 경로로 찾음

# * open(파일명, 모드): 파일을 열어서 파일 객체를 반환. "r" = read(읽기 전용) 모드
# TODO: 여기도 "README.txt" 대신 readme_path로 바꿔야 함
file = open(BASE_DIR / "README.txt", "r")
print(file.read())  # * .read(): 파일 내용 전체를 문자열로 읽어옴
# ! close()를 꼭 해줘야 함: 안 하면 파일이 계속 "열린 상태"로 남아서 메모리/자원을 낭비함
file.close()

# * memory management: 옛날 언어는 메모리를 직접 해제해야 했음
## * 안 비우면 누수(leak), 너무 일찍 비우면 에러

# * 요즘 언어는 GC(Garbage Collector)가 알아서 정리해줌

# * with문을 쓰면 이제 close()를 직접 안 불러도 됨 (No close any more)
# * with open(...) as 변수: 이 블록이 끝나면(에러가 나도!) 파이썬이 자동으로 file.close()를 실행해줌
# TODO: 여기도 위와 동일하게 "README.txt" 대신 readme_path로 바꿔야 함
with open(BASE_DIR / "README.txt", "r") as file:
    print(file.read())

# * "a" = append(추가) 모드: 파일 끝에 내용을 덧붙임. 기존 내용은 안 지워짐
# * "r"(읽기 전용)로 열면 write()는 에러남 -> 쓰려면 "w"(덮어쓰기) 또는 "a"(추가) 모드로 열어야 함
# TODO: 여기도 "WRITEME.txt" 대신 writeme_path로 바꿔야 함
with open(BASE_DIR / "WRITEME.txt", "a") as file:
    # * .write(문자열): 파일에 문자열을 쓰고, 쓴 글자 수(int)를 반환함 -> 그래서 print(...)에 숫자가 찍힘
    print(file.write("Thanks"))

# * csv 파일 다루는 방법
# * 1 using file
# file = open("sample.csv", "r")
# print(file.read())
# file.close()

# * using csv package
import csv

with open(BASE_DIR / "sample.csv", "r") as data_file:
    sample_data = csv.reader(data_file)
    for row in sample_data:
        if row[0] != "country":
            print(row[0])

import pandas as pd

data = pd.read_csv(BASE_DIR / "sample.csv")
print(data)

print(data["country"])
