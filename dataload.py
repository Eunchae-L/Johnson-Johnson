from sqlalchemy import create_engine, text, Table, MetaData
import pandas as pd

#데이터 로드
connection_string = "mysql+mysqlconnector://admin:Password12!#@database-1.cks69yhf0bnc.ap-northeast-2.rds.amazonaws.com:3306/SSC"
engine = create_engine(connection_string, echo=True)

# 연결 테스트
connection = engine.connect()
result = connection.execute(text("SELECT 1"))
print(result.scalar())  # 1

# 메타데이터 생성
metadata = MetaData()

# 테이블 정의
SALES = Table('SALES_FORECASTING_DATA_SALES', metadata, autoload_with=engine)
STORES = Table('SALES_FORECASTING_DATA_STORES', metadata, autoload_with=engine)
TRANS = Table('SALES_FORECASTING_DATA_TRANSACTIONS', metadata, autoload_with=engine)
holiday = Table('holidays_events', metadata, autoload_with=engine)
oil = Table('oil', metadata, autoload_with=engine)

# 테이블 조회
select_query_sales = SALES.select()
select_query_stores = STORES.select()
select_query_trans = TRANS.select()
select_query_holiday = holiday.select()
select_query_oil = oil.select()

# 결과를 DataFrame으로 변환
df_sales = pd.read_sql(select_query_sales, connection)
df_stores = pd.read_sql(select_query_stores, connection)
df_trans = pd.read_sql(select_query_trans, connection)
df_holiday_sql = pd.read_sql(select_query_holiday, connection)
df_oil = pd.read_sql(select_query_oil, connection)

#SALES_FORECASTING_DATA_SALES
print(df_sales.head())

print(sum(df_sales.isTrain == 'Y'))
print(sum(df_sales.isTrain == 'N'))

print(sales_train = df_sales.loc[df_sales.isTrain == 'Y'])