# API (Application Programming Interface)
# * 서로 다른 두 프로그램이 대화할 수 있게 해주는 "중간 다리" 역할을 하는 소프트웨어
# * 앱 쓰기, 메시지 보내기, 날씨 확인 등 대부분의 활동 뒤에서 API 요청/응답이 일어나고 있음

# * example: http://open-notify.org/Open-Notify-API/ISS-Location-Now/

import requests

# * requests.get(url): 그 url로 요청을 보내고, 서버의 응답을 response 객체로 받음
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
# * <Response [200]> 처럼 상태코드가 찍힘 (내용 전체가 아니라 응답 객체 자체)

# * status_code: 요청이 성공/실패했는지 알려주는 숫자. 200이면 정상 응답
# * 200이 아니면 뭔가 잘못됐다는 뜻이라 직접 에러를 발생시켜서 멈춤
if response.status_code != 200:
    raise Exception("Error from server")

# * raise_for_status(): status_code가 에러 범위(400/500번대)면 자동으로 에러를 발생시켜줌
response.raise_for_status()

# * response.json(): 응답으로 온 JSON 텍스트를 파싱해서 파이썬 딕셔너리로 변환 (json.loads()와 같은 역할)
payload = response.json()

print(payload)

print(payload["iss_position"]["longitude"])
