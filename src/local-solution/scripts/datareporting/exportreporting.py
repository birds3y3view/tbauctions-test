from sqlalchemy import create_engine
import pandas as pd
import os

username = "admin"
password = "thepasswordispassword"
ipaddress = "localhost"
port = "5432"
dbname = "auctiondb"

postgres_str = f'postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
connection = create_engine(postgres_str)

for sql in os.listdir('queries'):
    table_name = os.path.splitext(sql)[0]

    df = pd.read_sql_table(table_name, connection, schema="reporting")
    df.to_parquet(f'../../reporting/{table_name}.parquet')

