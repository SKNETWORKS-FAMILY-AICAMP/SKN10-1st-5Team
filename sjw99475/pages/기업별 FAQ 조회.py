import streamlit as st
from query2db import sql_execute

st.set_page_config(layout="wide")

st.title("기업 FAQ")

st.page_link("MainPage.py", label="메인 페이지로 이동")

# 사용자 검색어 입력
search_input = st.text_input('검색할 내용을 입력해주세요.')

# FAQ 기업 선택
company_layer, categorie_layer = st.columns(2)
choice_company = st.selectbox('기업을 선택해주세요.', ('현대', '기아'), index=None)

# 로고 경로
hyundai = "./현대 긴 로고.png"
kia = "./기아 긴 로고.png"

# 기업에 따른 카테코리 설정
if choice_company == "현대":
  sidebar_logo = hyundai
  main_body_logo = hyundai
  st.logo(sidebar_logo, icon_image=main_body_logo)
  company = 'hyundai_faq'
  categorie = ('모든 카테고리', '차량구매', '차량정비', '홈페이지', '블루멤버스', '모젠서비스', '블루링크', '현대 디지털 키', '빌트인캠', '기타')
elif choice_company == "기아":
  sidebar_logo = kia
  main_body_logo = kia
  st.logo(sidebar_logo, icon_image=main_body_logo)
  company = 'kia_faq'
  categorie = ('모든 카테고리', '차량 구매','차량 정비','기아멤버스','홈페이지','PBV','기타')

# 아직 기업을 선택하지 않았다면 카테고리는 비어있음.
if not choice_company:
  choice_categorie = st.selectbox('카테고리를 선택해주세요.', options = [], index=None)
else:
  choice_categorie = st.selectbox('카테고리를 선택해주세요.', options = categorie, index=None)

# 선택한 기업에 따라 검색할 table이름을 설정함.
sql_from_statement = None
if choice_company == "기아":
  sql_from_statement = "kia_faq" 
elif choice_company == "현대":
  sql_from_statement = 'hyundai_faq'

# 선택한 카테코리에 따라 sql문 where절의 조건을 설정.
if choice_categorie == "모든 카테고리":
  sql_where_category = "1 = 1"
elif choice_categorie:
  sql_where_category = f"Category = '{choice_categorie}'"
else:
  sql_where_category = "1 = 0"

# 입력한 텍스트가 포함된 질문만
if search_input:
  sql_where_search = f"Question like '%{search_input}%'"
else:
  sql_where_search = "1 = 1"

sql_where_statement = f"where\n({sql_where_category})\nand {sql_where_search}" if sql_where_category else "where 1=0"

# 아직 기업, 카테고리 둘 중 하나라도 선택하지 않았다면 쿼리하지 않음.
if sql_from_statement and choice_categorie:
  # 쿼리 문
  sql = f"""
  select *
  from 
    {sql_from_statement}
  {sql_where_statement}
  """
  print(sql)

  result = sql_execute('faq', sql=sql)
  for i in range(len(result)):
    with st.expander(f"{result.iloc[i, 2]}"):
      st.write(f"{result.iloc[i, 3]}")