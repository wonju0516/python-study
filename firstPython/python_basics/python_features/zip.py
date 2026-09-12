from pathlib import Path

BASE_DIR = Path(__file__).parent

# * "w+": 쓰기+읽기 겸용 모드 -> "w"처럼 없으면 새로 만들고 있으면 덮어쓰되, 같은 파일 객체로 읽기도 가능
f = open(BASE_DIR / "readme1.txt", "w+")
f.write("Helllllllllllo")
f.close()

f = open(BASE_DIR / "readme2.txt", "w+")
f.write("World")
f.close()

# * zip/unzip

import zipfile

# * ZipFile(경로, "w"): "comp.zip"이라는 이름의 빈 압축 상자를 새로 만듦 (open()이 파일 객체 주는 것과 같은 개념)
comp_file = zipfile.ZipFile(BASE_DIR / "comp.zip", "w")
# * write(파일, compress_type): comp.zip 상자 안에 파일 하나를 압축해서 담음
# * compress_type: 압축 방식 지정 -> ZIP_DEFLATED(용량 실제로 줄이는 진짜 압축) vs 기본값 ZIP_STORED(압축 아니고 그냥 담기만 함, 용량 그대로)
# ! arcname을 안 주면 zip 안에 전체 경로가 그대로 폴더 구조로 저장됨 (arcname="readme1.txt"처럼 지정하면 이름만 깔끔하게 저장)
comp_file.write(
    BASE_DIR / "readme1.txt", arcname="readme1.txt", compress_type=zipfile.ZIP_DEFLATED
)
comp_file.write(
    BASE_DIR / "readme2.txt", arcname="readme2.txt", compress_type=zipfile.ZIP_DEFLATED
)
comp_file.close()

zip_obj = zipfile.ZipFile(BASE_DIR / "comp.zip", "r")

# * extractall(폴더): 상자 안에 있던 파일들(readme1.txt, readme2.txt) 전부 압축 해제해서 그 폴더에 풀어놓음
zip_obj.extractall(BASE_DIR / "extracted")

# * shutil("shell utilities"): zip 말고도 파일 복사/이동/삭제 등 파일 시스템 작업을 폭넓게 다루는 표준 라이브러리
# * zip/unzip using shutil
import shutil

dir_to_zip = BASE_DIR / "zipme"
output = BASE_DIR / "folder_zip"

# * make_archive(결과이름, 만들형식, 압축할폴더): "zip" = 결과물을 zip 형식으로 만들어라 (출력 형식 지정)
shutil.make_archive(output, "zip", dir_to_zip)
# * unpack_archive(압축파일, 풀위치, 읽을형식): "zip" = 지금 주는 이 파일이 zip 형식이니 그렇게 읽어라 (입력 형식 지정) -> 풀린 결과는 항상 폴더/파일
shutil.unpack_archive(f"{output}.zip", BASE_DIR / "extracted2", "zip")
