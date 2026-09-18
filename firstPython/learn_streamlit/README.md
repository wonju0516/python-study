# learn_streamlit

streamlit 공부 기록입니다. (작성 중)

## 가상환경 설정

### Mac / Linux

```bash
python3 -m venv .venv          # * .venv 폴더 생성 (파이썬 내장 기능, 별도 설치 필요 없음)
source .venv/bin/activate       # * 가상환경 활성화 -> 터미널 앞에 (.venv) 표시됨
pip install -r requirements.txt  # * requirements.txt에 적힌 패키지 전부 설치
```

### Windows

```powershell
python -m venv .venv            # * mac과 동일 (python3 대신 python 사용)
.venv\Scripts\Activate.ps1      # * 활성화 명령어만 다름 (source .venv/bin/activate 아님)
pip install -r requirements.txt
```

- 폴더 이름은 관례상 점(`.`)이 붙은 `.venv`로 통일함 (레포 `.gitignore`에 `.venv/`가 등록돼 있어서, 이 이름이어야 깃에 안 올라감). 점을 빼먹고 `venv\Scripts\...`로 치면 "모듈을 로드할 수 없습니다" 오류가 남
- Windows에서 `.venv\Scripts\Activate.ps1` 실행 시 "이 시스템에서 스크립트 실행이 금지되어 있습니다" 같은 오류가 나면, PowerShell을 관리자 권한으로 열어서 `Set-ExecutionPolicy RemoteSigned` 한 번 실행해줘야 함
- 가상환경 끌 때는 Mac/Windows 공통으로 `deactivate`

## requirements.txt

```
streamlit
pandas
numpy
requests
```

## 지금까지 한 것

- `python3 -m venv venv`로 가상환경 생성 (pyenv 전역 버전인 3.14.7 기준으로 생성됨)
- `source venv/bin/activate`로 활성화
- `requirements.txt` 작성 후 `pip install -r requirements.txt`로 `streamlit`/`pandas`/`numpy`/`requests` 설치
- `streamlit hello` 명령어로 설치 확인 — 실행하면 이메일 입력 질문이 뜨는데, 빈칸으로 두고 Enter만 누르면 됨 (온보딩 메일 수신 여부를 묻는 선택 사항). 그 다음 데모 앱이 브라우저에서 자동으로 열림
