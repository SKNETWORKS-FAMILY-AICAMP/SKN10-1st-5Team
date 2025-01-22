import streamlit as st
import pandas as pd


st.title("전국 자동차 등록 현황")

layer_1, layer_2 = st.columns(2)

with layer_1:
    st.page_link("pages/연도별 자동차 등록 대수.py", label="연도별 자동차 등록 대수 조회")

with layer_2:
    st.page_link("pages/기업별 FAQ 조회.py", label="기업별 FAQ 조회")






