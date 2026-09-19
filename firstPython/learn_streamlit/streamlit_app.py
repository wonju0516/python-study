import numpy as np
import pandas as pd
import streamlit as st

st.title("Uber pickups in NYC")  # * 화면 맨 위의 큰 제목

# * 실행 방법: 터미널에서 streamlit run streamlit_app.py
# * Fetch some data
DATE_COLUMN = "date/time"
DATA_URL = (
    "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)


# * 문제: 위의 "다시 실행" 때문에 슬라이더를 움직일 때마다 CSV를 인터넷에서 또 받아오게 됨 (느림)
# * 해결: 함수 위에 @st.cache_data만 붙이면, 같은 인자로 다시 부를 때 함수를 실행하지 않고 저장해둔 결과를 바로 돌려줌
# * load_data(10000) 처음 호출 -> 진짜 실행 / 다시 호출 -> 캐시에서 즉시 반환 / load_data(5000)처럼 인자가 바뀌면 새로 실행
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(
        DATA_URL, nrows=nrows
    )  # * 위에서부터 nrows개 행만 읽음 (전체는 너무 큼)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    # * 문자열로 된 날짜를 진짜 날짜/시간 타입으로 변환 (그래야 아래에서 .dt.hour를 쓸 수 있음)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# * st.text(): 글자 한 줄 띄움 -> 변수에 담아둔 이유: 나중에 그 글자를 바꾸려고
data_load_state = st.text("Loading data...")
data = load_data(10000)
data_load_state.text(
    "Done! (using st.cache_data)"
)  # * 담아둔 그 글자가 "Done!"으로 바뀜

# * st.checkbox(): 체크하면 True를 돌려줌 -> 체크했을 때만 아래 블록이 실행됨
if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)  # * 값을 화면에 알맞은 모양으로 그려줌 (DataFrame이면 표로)

st.subheader("Number of pickups by hour")
# * np.histogram(값들, bins, range): 값들을 칸(구간)으로 나눠서 각 칸에 몇 개 들어가는지 셈
# * bins=24: 24칸으로 나눔 / range=(0, 24): 0~24시 범위 -> 한 칸이 1시간 (0~1시, 1~2시 ... 23~24시)
# * 결과는 (칸별 개수, 칸 경계값) 두 개라서 [0]으로 개수만 꺼냄 (그래프에는 개수만 필요)
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)  # * 막대 그래프

# * st.slider(이름, 최솟값, 최댓값, 처음값): 좌우로 움직이는 슬라이더를 화면에 띄우고, 지금 고른 숫자를 돌려줌
# * 여기선 "hour"라는 이름으로 0~23 사이를 고를 수 있고, 처음엔 17에 놓여 있음 (움직이면 파일이 다시 실행되고 값이 바뀜)
hour_to_filter = st.slider("hour", 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f"Map of all pickups at {hour_to_filter}:00")
st.map(filtered_data)  # * lat/lon 컬럼을 찾아서 지도 위에 점으로 찍어줌
