import logging

# * root logger -> logging.debug()처럼 모듈 이름으로 바로 호출하면 자동으로 쓰이는 "기본 로거"
## ! 지금은 로거를 따로 안 만들고 이 root logger를 그대로 쓰는 방식
# * basicConfig -> 로깅 전체의 기본 설정을 한 번 지정 (보통 파일 맨 위에서 딱 한 번만 호출)
# logging.basicConfig(
#     level=logging.DEBUG,  # * DEBUG 이상(DEBUG/INFO/WARNING/ERROR/CRITICAL 전부)만 출력 -> "필터 기준선"
#     # * format -> 로그 한 줄이 어떤 형식으로 찍힐지 지정하는 문자열
#     ## * %(asctime)s  -> 로그가 찍힌 시각 (연-월-일 시:분:초,밀리초)
#     ## * %(levelname)s -> 심각도 레벨 이름 (DEBUG/INFO/WARNING/ERROR/CRITICAL)
#     ## * %(message)s  -> 실제로 logging.debug("...")에 넣은 메시지 내용
#     ## ! %(이름)s 는 옛날 방식의 파이썬 문자열 포맷팅(% 포맷팅) 문법 -> f-string 나오기 전부터 쓰이던 방식, logging 모듈은 지금도 이 문법을 씀
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )

# # * Now, you can log messages at different severity levels
# logging.debug("This is a debug message")  # * DEBUG 레벨
# logging.info("This is an info message")  # * INFO 레벨
# logging.warning("This is a warning message")  # * WARNING 레벨
# logging.error("This is an error message")  # * ERROR 레벨
# logging.critical("This is an critical message")  # * CRITICAL 레벨


# * write the log to the file
# logging.basicConfig(
#     filename="example.log",
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )


# # ! 직접 로거를 만들어서 쓰는 방식 (root logger 경고가 사라지는 방식) -> 참고용, 아래는 실행 안 됨
# logger = logging.getLogger(
#     __name__
# )  # __name__ = 이 파일의 모듈 이름을 로거 이름으로 사용
# logger.debug(
#     "This is a debug message"
# )  # logging.debug(...) 대신 logger.debug(...)로 호출
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("this is an error message")
# logger.critical("This is a critical message")


# * custom logger를 "제대로" 만드는 예제 -> getLogger + setLevel + Formatter + Handler + addHandler
## ! 위 logger는 basicConfig 설정을 그대로 물려받아서 씀 -> 여기서는 handler를 직접 붙여서 더 세밀하게 제어해봄

my_logger = logging.getLogger(
    "my_custom_logger"
)  # * 이름을 직접 지정 -> 다른 로거(root, __name__ 로거 등)와 구분됨
my_logger.setLevel(
    logging.DEBUG
)  # * 이 로거 자체가 "몇 레벨부터 처리할지" -> DEBUG 이상 다 처리하겠다는 뜻
my_logger.propagate = False  # ! True(기본값)면 이 로거의 로그가 root logger한테도 전달돼서 중복 출력됨 -> 그래서 꺼둠

# * Formatter -> 로그 한 줄의 출력 형식을 정의 (basicConfig의 format=이랑 같은 역할, handler에 직접 붙이는 방식)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# * %(name)s -> 로거 이름 (여기선 "my_custom_logger") 도 같이 출력됨

# * FileHandler -> 로그를 "파일에" 기록하는 담당자
file_handler = logging.FileHandler("custom.log")
file_handler.setLevel(logging.DEBUG)  # * 파일에는 DEBUG 이상 전부 기록
file_handler.setFormatter(formatter)  # * 이 handler가 쓸 형식 지정

# * StreamHandler -> 로그를 "콘솔(화면)에" 출력하는 담당자
console_handler = logging.StreamHandler()
console_handler.setLevel(
    logging.WARNING
)  # * 콘솔에는 WARNING 이상만 출력 (덜 시끄럽게)
console_handler.setFormatter(formatter)

# * addHandler -> 로거에 "이 담당자들 써라"라고 등록 (여러 개 등록 가능 -> 파일 + 콘솔 동시에)
my_logger.addHandler(file_handler)
my_logger.addHandler(console_handler)

my_logger.debug("디버그 메시지 -> 파일에만 기록됨 (콘솔 레벨보다 낮아서 화면엔 안 뜸)")
my_logger.info("정보 메시지 -> 파일에만 기록됨")
my_logger.warning("경고 메시지 -> 파일 + 콘솔 둘 다 출력됨")
my_logger.error("에러 메시지 -> 파일 + 콘솔 둘 다 출력됨")
my_logger.critical("치명적 메시지 -> 파일 + 콘솔 둘 다 출력됨")
