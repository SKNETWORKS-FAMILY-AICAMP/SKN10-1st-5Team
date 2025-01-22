import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data

st.title("연도별 자동차 등록대수")

st.page_link("MainPage.py", label="메인 페이지로 이동")

source = data.barley()

toggle1 = st.toggle("승용차")
if toggle1:
    chart_data = pd.DataFrame(np.random.randn(50, 17), columns=["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "충북", "충남", "전북", "전남", "경북", "경남", "제주", "강원"])

    st.line_chart(chart_data, x_label="연도별", y_label="총 등록 차량 수")

toggle2 = st.toggle("승합차")
if toggle2:
    chart_data = pd.DataFrame(np.random.randn(50, 17), columns=["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "충북", "충남", "전북", "전남", "경북", "경남", "제주", "강원"])

    st.line_chart(chart_data, x_label="연도별", y_label="총 등록 차량 수")


