import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data

st.title("연도별 자동차 등록대수")

st.page_link("MainPage.py", label="메인 페이지로 이동")

source = data.barley()

toggle1 = st.toggle("승용차")
if toggle1:
    st.bar_chart(source, x="year", y="yield", color="site", stack=False)

toggle2 = st.toggle("승합차")
if toggle2:
    st.bar_chart(source, x="year", y="yield", color="site", stack=False)



