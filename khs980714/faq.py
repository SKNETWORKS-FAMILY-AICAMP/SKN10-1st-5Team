import streamlit as st

st.title("기업 FAQ")
with st.container():
  search_input = st.text_input('검색할 내용을 입력해주세요.')

  company_layer, categorie = st.columns(2)
  with company_layer:
    choice_company = st.selectbox('기업을 선택해주세요.', ('현대', '기아'))
  
  with categorie:
    search = st.selectbox('카테고리를 선택해주세요.', ('모든 카테고리', '대충 카테고리1'))

  search_icon = st.button("검색", type = 'primary')

with st.container(border = True):
  if (search_input is not '') and search_icon:
    st.write(f'{search_input}에 대한 내용~~~')
  else:
    st.write('모두 검색되는중')