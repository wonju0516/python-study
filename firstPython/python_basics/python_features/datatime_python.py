import datetime

# * datetime.now(): 현재 시각을 datetime 객체로 반환
current = datetime.datetime.now()
print(current)

# ? UTC로 통일하고 싶으면 tz=datetime.timezone.utc를 넘기면 됨
# current = datetime.datetime.now(tz=datetime.timezone.utc)

# * 연/월/일은 속성(property)이라 괄호 없이 접근
print(current.year)
print(current.month)
print(current.day)

# * weekday() - 월요일=0 ~ 일요일=6으로 요일을 숫자로 반환
day_of_week = current.weekday()
print(day_of_week)

# * custom date: 연/월/일을 직접 지정해서 datetime 객체 생성
custom_date = datetime.datetime(year=2022, month=1, day=1)
print(custom_date)

# * string to datetime object: strptime(문자열, 포맷) - 문자열을 datetime 객체로 변환("parse time")
# * %Y=4자리 연도, %m=월, %d=일, %H=시(24시간), %M=분, %S=초
datetime_object = datetime.datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")

print(type(datetime_object))

# * Datetime object to string: strftime(포맷) - datetime 객체를 원하는 형식의 문자열로 변환("format time")
datetime_str = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
print(type(datetime_str))
print(datetime_str)

# * timedelta: 날짜/시간 간의 "차이"를 나타내는 객체. datetime + timedelta로 날짜 계산 가능
from datetime import timedelta

print(datetime_object + timedelta(days=1))  # * 하루 뒤 날짜 계산
