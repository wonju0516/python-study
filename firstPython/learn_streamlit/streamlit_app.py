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


# * effortless caching: @st.cache_data
# * 문제: 위의 "다시 실행" 때문에 슬라이더를 움직일 때마다 CSV를 인터넷에서 또 받아오게 됨 (느림)
# * 해결: 함수 위에 @st.cache_data만 붙이면, 같은 인자로 다시 부를 때 함수를 실행하지 않고 저장해둔 결과를 바로 돌려줌
# * load_data(10000) 처음 호출 -> 진짜 실행 / 다시 호출 -> 캐시에서 즉시 반환 / load_data(5000)처럼 인자가 바뀌면 새로 실행
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(
        DATA_URL, nrows=nrows
    )  # * 위에서부터 nrows개 행만 읽음 (전체는 너무 큼)
    lowercase = lambda x: str(x).lower()
    # * rename(함수, axis="columns"): 모든 컬럼 이름에 함수를 적용 (행 이름이 아니라 컬럼 이름)
    # * inplace=True: 새 표를 만들지 않고 data 자체를 바꿈
    data.rename(lowercase, axis="columns", inplace=True)
    # * 문자열로 된 날짜를 진짜 날짜/시간 타입으로 변환 (그래야 아래에서 .dt.hour를 쓸 수 있음)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# * st.text(): 화면에 글자 한 줄을 그리고, 그 자리를 가리키는 객체를 돌려줌 -> 나중에 그 자리의 글자를 갈아끼울 수 있음
data_load_state = st.text("Loading data...")
# * 10,000행 로드 (캐시 덕분에 두 번째 실행부터는 거의 즉시 끝남)
data = load_data(10000)
# * 위에서 만든 그 자리의 글자를 "Done!"으로 교체
data_load_state.text("Done! (using st.cache_data)")

# * st.checkbox(): 체크하면 True를 돌려줌 -> 체크했을 때만 아래 블록이 실행됨
if st.checkbox("Show raw data"):
    st.subheader("Raw data")  # * 소제목
    st.write(data)  # * 값을 화면에 알맞은 모양으로 그려줌 (DataFrame이면 표로)

st.subheader("Number of pickups by hour")
# * np.histogram(값들, bins=24, range=(0, 24)): 0~24시를 24칸으로 나눠서 각 시간대에 몇 건이 속하는지 셈
# * 결과는 (개수 배열, 경계값 배열) 튜플이라 [0]으로 개수 배열만 꺼냄
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)  # * 막대 그래프

hour_to_filter = st.slider("hour", 0, 23, 17)  # min: 0h, max: 23h, default: 17hs
# * data[조건]: 조건이 True인 행만 남김 (여기선 승차 시각의 '시'가 슬라이더 값과 같은 행만)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f"Map of all pickups at {hour_to_filter}:00")
st.map(filtered_data)  # * lat/lon 컬럼을 찾아서 지도 위에 점으로 찍어줌
