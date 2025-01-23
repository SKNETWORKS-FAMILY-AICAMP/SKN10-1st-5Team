import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from query2db import sql_execute

# 지역 데이터들
regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '충북', '충남', 
           '전북', '전남', '경북', '경남', '제주', '강원']

# 자동차 카테고리 데이터들
car_category = ['승용','승합','특수','화물']

# Streamlit UI
st.title('전국 자동차의 Line Graph')

# 연도 범위 선택
year_range = st.slider(
    '연도 범위를 선택하세요:',
    min_value=2018,
    max_value=2024,
    value=(2018, 2024),  # 기본 범위
    step=1
)

# 지역 선택
selected_regions = st.multiselect(
    '지역을 선택하세요:',
    regions,
)

# 자동차 카테고리 선택
selected_category = st.multiselect(
    '차량 종류를 선택하세요:',
    car_category,
)

# sql문의 where 문을 작성함.
sql_where_region = " or ".join([f"city = '{region}'" for region in selected_regions])
sql_where_category = " or ".join([f"type = '{category}'" for category in selected_category])
sql_where_statement = f"where\n({sql_where_region})\nand ({sql_where_category})\nand (year >= {year_range[0]} and year <= {year_range[1]})" if sql_where_region and sql_where_category else "where 1=0"

# 사용자의 선택지대로 sql문 작성
sql = f'''
select
    year, 
    city,
    sum(value) as value
from car_detail
{sql_where_statement}
group by year, city
;
'''

# 서버로부터 결과값을 DataFrame형태로 받음
df = sql_execute(db="car", sql=sql)

# 검색된 결과가 있다면 시각화
if len(df) > 0:
    df["value"] = df["value"].astype(int)
    st.subheader(', '.join([region for region in selected_regions]) + " 지역의")
    st.text(', '.join([category for category in selected_category]) + " 차량 검색 결과입니다.")
    st.line_chart(df, x="year", y="value", color="city", height=500)