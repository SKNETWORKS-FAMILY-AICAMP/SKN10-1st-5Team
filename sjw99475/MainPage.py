import streamlit as st
import pandas as pd
import base64

st.set_page_config(layout="wide")

st.title("전국 자동차 등록 현황")

if st.button("연도별 자동차 등록 대수 조회"):
    st.switch_page("pages/연도별 자동차 등록 대수.py")
if st.button("기업별 FAQ 조회"):
    st.switch_page("pages/기업별 FAQ 조회.py")



def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

image_path = "./메인 배경화면.png"  # 이미지 파일 경로
image_base64 = load_image(image_path)

# HTML로 배경 이미지 설정
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{image_base64}');
            background-size: conta;
            background-position: center;
            background-repeat: no-repeat;
        }}
    </style>
    """, unsafe_allow_html=True
)