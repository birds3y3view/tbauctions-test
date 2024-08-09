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

for filename in os.listdir('../../clean'):
    normalFilename = os.path.splitext(filename)[0]
    df = pd.read_parquet(f'../../clean/{filename}')
    df.to_sql(con=connection, schema='clean', name=normalFilename, if_exists='replace')

