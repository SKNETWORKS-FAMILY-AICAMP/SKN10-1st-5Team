import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from query2db import sql_execute
import plotly.express as px

st.set_page_config(layout="wide")

# 그래프 종류들
graphs = ['선 그래프', '지도', '도넛 차트', '기타']

# 지역 데이터들
regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '충북', '충남', 
           '전북', '전남', '경북', '경남', '제주', '강원']

# 자동차 카테고리 데이터들
car_category = ['승용','승합','특수','화물']

# Streamlit UI
st.title('전국 자동차의 Line Graph')

# 그래프 선택
selected_graph = st.selectbox(
    '그래프를 선택하세요:',
    graphs,
    index=None
)

if selected_graph == '선 그래프':
    # 검색된 결과가 있다면 시각화
    # 연도 범위 선택
    selected_year = st.slider(
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
    sql_where_statement = f"where 1=1\nand({sql_where_region})\nand ({sql_where_category})\nand (year >= {selected_year[0]} and year <= {selected_year[1]})" if sql_where_region and sql_where_category else "where 1=0"

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

    if len(df) > 0:
        df["value"] = df["value"].astype(int)
        st.subheader(', '.join([region for region in selected_regions]) + " 지역의")
        st.text(', '.join([category for category in selected_category]) + " 차량 검색 결과입니다.")
        st.line_chart(df, x="year", y="value", color="city", height=500)

elif selected_graph == '지도':
    # 연도도 선택
    selected_year = st.slider(
        '연도를 선택하세요:',
        2018, 2024)

    # 자동차 카테고리 선택
    selected_category = st.selectbox(
        '차량 종류를 선택하세요:',
        car_category,
        index=None
    )

    sql_where_year = f"year = '{selected_year}'"
    sql_where_category = f"type = '{selected_category}'"
    sql_where_statement = f"where 1=1\nand ({sql_where_category})\nand ({sql_where_year})" if sql_where_category else "where 1=0"

    # 사용자의 선택지대로 sql문 작성
    sql = f'''
select
    year, 
    city,
    sum(value) as value
from car_detail
{sql_where_statement}
group by year, city
order by city
    ;
    '''
    # 서버로부터 결과값을 DataFrame형태로 받음
    df = sql_execute(db="car", sql=sql)

    if len(df) > 0:
        df['lon'] = [128.138917, 127.459536, 128.191177, 128.883623, 126.936935, 128.654985, 127.392024, 129.053469, 127.001016, 127.250496, 129.255976, 126.701765, 126.968492, 127.142001, 126.529157, 126.787509, 127.695370]
        df['lat'] = [37.813732, 37.436038, 35.455151, 36.291491, 35.135247, 35.816177, 36.340544, 35.161954, 37.549449, 36.564806, 35.550875, 37.456783, 34.860440, 35.714971, 33.502377, 36.715894, 36.996171]
        df['lon'] = df['lon'].astype(float)
        df['lat'] = df['lat'].astype(float)
        df["value"] = (df["value"].astype(float)) / 1000
        st.map(df, latitude="lat", longitude="lon", size="value")

elif selected_graph == '도넛 차트':
    choice_standard, selected_view, choice_view = False, False, False
    col_list = [['지역별', '연도별', '월별', '차종별', '용도별'], ['city', 'year', 'month', 'type', 'purpose']]
    selected_standard = st.selectbox("기준을 골라주세요.", col_list[0], index = None)
    if selected_standard:
        standard_idx = col_list[0].index(selected_standard)
        mapping_standard = col_list[1][standard_idx]
        sql = f'''
            select distinct {mapping_standard} from car_detail;
            '''
        standard = sql_execute(db="car", sql=sql)
        choice_standard = st.selectbox('항목을 선택해주세요.', standard, index = None)

    if choice_standard:
        _, _ = col_list[0].remove(selected_standard), col_list[1].remove(mapping_standard)
        selected_view = st.selectbox("볼 데이터를 골라주세요.", col_list[0], index = None)
        if selected_view:
            view_idx = col_list[0].index(selected_view)
            mapping_view = col_list[1][view_idx]

    if selected_view:
        sql = f'''
            select distinct {mapping_view} from car_detail;
            '''
        view = sql_execute(db="car", sql=sql)
        choice_view = st.multiselect('항목을 선택해주세요.', view)
    
    if choice_view:
        txt = f"and {mapping_view} = '{choice_view[0]}' "
        for i in choice_view[1:]:
            txt += f"or {mapping_view} = '{i}' "
        sql = f'''
            select {mapping_view}, sum(value) as sum_value from car_detail
            where 1 = 1
            {txt}
            group by {mapping_view}
            order by sum_value desc;
            '''
        df = sql_execute(db="car", sql=sql)
        fig = px.pie(
            df,
            values = "sum_value",
            title = f"{selected_standard}[{choice_standard}] / {selected_view} 도넛 차트",
            names = mapping_view,
            height = 800,
            hole = 0.3)
        fig.update_traces(textfont = dict(size=25), textinfo = 'percent+label')
        fig.update_layout(
            title = dict(font = dict(size = 30)), showlegend = True, legend = dict(font = dict(size = 25)))
        st.plotly_chart(fig)
elif selected_graph == '기타':
    # 랜덤 데이터를 생성
    np.random.seed(42)  # 랜덤 시드를 고정하여 결과를 재현 가능하게 만듦
    months = np.random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], size=100)
    values = np.random.randint(100, 1000, size=100)  # 100에서 1000 사이의 랜덤 값

    # 데이터프레임 생성
    df = pd.DataFrame({
        'month': months,
        'value': values
    })

    # Stripplot 그리기
    plt.figure(figsize=(10, 6))
    sns.stripplot(data=df, x='month', y='value', jitter=True, color='blue')
    plt.title('Stripplot graph')
    st.pyplot(plt)

    # 랜덤 데이터를 생성
    np.random.seed(42)  # 랜덤 시드를 고정하여 결과를 재현 가능하게 만듦
    months = np.random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], size=200)
    values = np.random.normal(loc=500, scale=150, size=200)  # 평균 500, 표준편차 150인 정규분포를 따르는 랜덤 값

    # 데이터프레임 생성
    df = pd.DataFrame({
        'month': months,
        'value': values
    })

    # Violinplot 그리기
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x='month', y='value', color='yellow', inner="stick")
    plt.title(' Violinplot graph')
    st.pyplot(plt)

    # 랜덤 데이터를 생성
    np.random.seed(42)  # 랜덤 시드를 고정하여 결과를 재현 가능하게 만듦
    # 5개의 랜덤 변수 생성 (예: 'A', 'B', 'C', 'D', 'E' 컬럼)
    data = np.random.rand(100, 5)  # 100개의 샘플, 5개의 변수

    # 데이터프레임 생성
    insurance_df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

    # 상관계수 계산
    corr_matrix = insurance_df.corr()

    # Heatmap 그리기
    sns.set_theme(rc={'figure.figsize': (8, 6)}, style='white')
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True, square=True)
    plt.title('heatmap graph')
    st.pyplot(plt)

    # 랜덤 데이터를 생성
    np.random.seed(42)  # 랜덤 시드를 고정하여 결과를 재현 가능하게 만듦
    categories = ['A', 'B', 'C', 'D', 'E']  # 5개의 카테고리
    values = np.random.randint(100, 1000, size=5)  # 100에서 1000 사이의 랜덤 값 생성

    # 도넛 차트 그리기
    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        values, 
        labels=categories, 
        autopct='%1.1f%%', 
        startangle=90, 
        wedgeprops=dict(width=0.4)
    )

    ax.set_title('랜덤 데이터로 그린 도넛 차트')
    
    # Streamlit에서 그래프 표시
    st.pyplot(fig)
