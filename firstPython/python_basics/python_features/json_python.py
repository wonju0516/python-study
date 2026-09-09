# json python: JSON 형식 텍스트 <-> 파이썬 객체(dict/list) 서로 변환하기
# * 파이썬 입장에서 JSON은 "특별한 타입"이 아니라 그냥 문자열(str)임
# * 문자열 상태로는 data["key"]처럼 딕셔너리로 못 다룸 -> loads()로 dict 변환해야 실제 데이터 조작 가능
# * 반대로 dict를 다시 파일에 저장하려면(write는 문자열만 받음) -> dumps()로 다시 문자열 변환해야 함

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "sample.json", mode="r") as f:
    # * f.read()만 하면 그냥 문자열(str)임 -> data["type"]처럼 딕셔너리로 못 씀
    # * json.loads(문자열): JSON 형식 문자열을 파이썬 dict/list로 변환 (loads = load string)
    data = json.loads(f.read())
    data["type"] = "drink"  # * 이제 진짜 dict라서 key로 값 수정 가능
    with open(BASE_DIR / "sample.json", mode="w") as w:
        # * json.dumps(객체): 파이썬 dict/list를 JSON 형식 문자열로 변환 (dumps = dump string)
        # ! write()는 문자열만 받을 수 있어서, dict를 그대로 못 넘기고 dumps로 문자열로 바꿔야 함
        w.write(json.dumps(data))
