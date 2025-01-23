import streamlit as st
from .sql_constant import INSERT_SQLs
from sqlalchemy import text


@st.cache_resource
def get_connector():
  return st.connection("mydb", type = 'sql', autocommit = True)

def insert_quary(sql_constant:INSERT_SQLs, datas:list, company_name:str) -> list:
  conn = get_connector()
  list_error = []
  for data in datas:
    try:
      insert_sql = sql_constant.value[1].format(
        faq_name = data['faq_name'], COMPANY_ID = data['COMPANY_ID'], CATEGORIE = data['CATEGORIE'], QUESTION = data['QUESTION'], ANSWER = data['ANSWER']
      )
      conn.connect().execute(text(insert_sql))
    except Exception as e:
      list_error.append(data)
  return list_error