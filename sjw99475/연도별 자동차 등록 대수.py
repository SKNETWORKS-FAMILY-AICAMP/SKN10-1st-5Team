import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 샘플 데이터 생성 (실제 데이터에 맞게 수정 가능)
years = np.arange(2000, 2021)
regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '충북', '충남', 
           '전북', '전남', '경북', '경남', '제주', '강원']

# 승용차와 승합차의 데이터 생성 (임의 데이터, 실제 데이터에 맞게 수정 필요)
data = {}
for region in regions:
    data[region] = {
        '승용차': np.random.randint(1000, 10000, size=21),
        '승합차': np.random.randint(500, 5000, size=21)
    }

df = pd.DataFrame(data, index=years)

# Streamlit UI
st.title('승용차와 승합차 Line Graph')

# 승용차/승합차 토글 버튼
show_sedan = st.checkbox('승용차 Line Graph', value=True)
show_van = st.checkbox('승합차 Line Graph', value=True)

# 지역 선택 (여러 지역을 동시에 선택할 수 있도록)
selected_regions = st.multiselect(
    '지역을 선택하세요:',
    regions,
    default=regions  # 기본으로 모든 지역 선택
)

# 승용차 그래프 출력
if show_sedan:
    st.subheader('승용차 Line Graph')
    fig, ax = plt.subplots(figsize=(10, 6))

    # 선택된 지역에 대해 각기 다른 라인 그래프 추가
    for region in selected_regions:
        ax.plot(df.index, df[region]['승용차'], label=f'{region} 승용차', linestyle='-', marker='o')

    ax.set_title('선택된 지역의 승용차 추이')
    ax.set_xlabel('년도')
    ax.set_ylabel('차량 수')
    ax.legend()

    st.pyplot(fig)

# 승합차 그래프 출력
if show_van:
    st.subheader('승합차 Line Graph')
    fig, ax = plt.subplots(figsize=(10, 6))

    # 선택된 지역에 대해 각기 다른 라인 그래프 추가
    for region in selected_regions:
        ax.plot(df.index, df[region]['승합차'], label=f'{region} 승합차', linestyle='--', marker='x')

    ax.set_title('선택된 지역의 승합차 추이')
    ax.set_xlabel('년도')
    ax.set_ylabel('차량 수')
    ax.legend()

    st.pyplot(fig)
else:
    st.write("승용차 또는 승합차 Line Graph를 표시하려면 해당 옵션을 선택하세요.")


