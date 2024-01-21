import pandas as pd
import sqlalchemy as sa

engine = sa.create_engine('mysql+pymysql://root:12345@localhost:3306/college_management_system')
df = pd.read_sql_table('department', engine)
df = pd.read_sql_table('department', engine, columns=['department_name'])
print(df)