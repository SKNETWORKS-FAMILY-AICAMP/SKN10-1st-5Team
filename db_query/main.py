from query2db import sql_execute

sql = '''
select
    *
from car_detail
;
'''

df = sql_execute(db="car", sql=sql)
print(df)

# streamlit에서는 이런 식으로 DataFrame 시각화 가능
# st.dataframe(df)