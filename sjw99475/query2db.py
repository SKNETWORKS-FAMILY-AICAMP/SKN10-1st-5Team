import pymysql
import pandas as pd

# 문자열 sql문을 받아서 DataFrame으로 반환하는 함수수
def sql_execute(db:str, sql:str) -> pd.DataFrame:
    # 이런거 .env에 넣어야 할 것 같긴함.
    connection = pymysql.connect(
        host="localhost",
        port=3306,  # MySQL 서버 만들 때 3307 포트로 했음.
        user="car",
        password="c1234",
        database=db
    )

    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute(sql)

    result = pd.DataFrame(cursor.fetchall())
    return result