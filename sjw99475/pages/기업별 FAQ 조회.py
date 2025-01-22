import streamlit as st

st.title("기업 FAQ")

st.page_link("MainPage.py", label="메인 페이지로 이동")


with st.container():
  search_input = st.text_input('검색할 내용을 입력해주세요.')

  company_layer, categorie = st.columns(2)
  with st.container():
    with company_layer:
      choice_company = st.selectbox('기업을 선택해주세요.', ('현대', '기아'))
    
    if choice_company == "현대":
      with categorie:
        search = st.selectbox('카테고리를 선택해주세요.', ('모든 카테고리', '차량구매','차량정비','홈페이지','블루멤버스','모젠서비스','블루링크','현대 디지털 키','빌트인캠','기타'))
        if search == "모든 카테고리":
            sql = """
                select * from hyundai_faq;
            """
        else:
            sql = f"""
                select * from hyundai_faq where Category = {search};
            """
    elif choice_company == "기아":
      with categorie:
        search = st.selectbox('카테고리를 선택해주세요.', ('모든 카테고리', '차량구매','차량정비','기아멤버스','홈페이지','PBV','기타'))
        if search == "모든 카테고리":
            sql = """
                select * from kia_faq;
            """
        else:
            sql = f"""
                select * from kia_faq where Category = {search};
            """
  search_icon = st.button("검색", type = 'primary')

# 쿼리문 작성할 곳
with st.container(border = True):
  if (search_input is not '') and search_icon:
    st.write(f'{search_input}에 대한 내용')
  else:
    st.write('모두 검색되는중')