# * SMTP(Simple Mail Transfer Protocol): 이메일을 "보낼 때" 쓰는 표준 프로토콜
# * smtplib: 파이썬에서 이 프로토콜로 이메일을 코드로 직접 보낼 수 있게 해주는 표준 라이브러리
import smtplib

# ! 이건 예시 코드라 실제로 실행하면 인증 실패함 (진짜 계정/비밀번호 아님)
# ! 실제로 실습하려면 아래 내용을 바꿔야 함:
# !   1. my_email/password를 본인 계정으로 교체
# !   2. password는 로그인 비밀번호가 아니라 "앱 비밀번호"(App Password)를 따로 발급받아서 써야 함
# !   3. 서버 주소도 이메일 서비스에 맞게 교체 (Gmail: smtp.gmail.com, Yahoo: smtp.mail.yahoo.com, Naver: smtp.naver.com)
my_email = "altoformula@yahoo.com"  # * 보내는 사람 이메일 주소 (문자열)
password = "zxcvqwer!@#$"  # * 그 계정의 앱 비밀번호 (문자열)

# * smtplib.SMTP(서버주소, 포트): 이메일 서버에 연결. 포트 587은 STARTTLS 방식 표준 포트
# ! 지금 코드는 포트를 안 적어서 기본 포트(25, 요즘은 대부분 막혀있음)로 시도함 -> 587을 명시하는 게 안전함
connection = smtplib.SMTP("smtp.mail.yahoo.com")

# * starttls(): 이후 통신을 암호화(TLS)로 전환. 이걸 안 하면 비밀번호/내용이 암호화 안 된 채로 오갈 수 있음
connection.starttls()

# * login(계정, 비밀번호): 그 이메일 서버에 로그인
connection.login(user=my_email, password=password)

# * sendmail(보내는사람, 받는사람, 내용): 실제로 메일을 발송
# * from_addr: 보내는 사람 주소 (문자열)
# * to_addrs: 받는 사람 주소 (문자열 하나, 또는 여러 명이면 문자열 리스트)
# * msg: 보낼 내용 (문자열)
connection.sendmail(from_addr=my_email, to_addrs="altoformula@yahoo.com", msg="Hello")
