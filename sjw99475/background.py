import streamlit as st
import base64

def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

image_path = "최종 로컬 이미지 파일 경로"  # 이미지 파일 경로
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