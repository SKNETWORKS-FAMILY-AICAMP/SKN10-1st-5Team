from query_kia_faq import sql_execute

sql = '''
select
    *
from kia_faq
;
'''

df = sql_execute(sql)
print(df)

# streamlit에서는 이런 식으로 DataFrame 시각화 가능
# st.dataframe(df)