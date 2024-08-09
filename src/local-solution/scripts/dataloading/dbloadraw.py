from sqlalchemy import create_engine
import pandas as pd
import os

def main():
    username = "admin"
    password = "thepasswordispassword"
    ipaddress = "localhost"
    port = "5432"
    dbname = "auctiondb"

    postgres_str = f'postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
    connection = create_engine(postgres_str)

    for filename in os.listdir('../raw'):
        normalFilename = os.path.splitext(filename)[0]
        df = pd.read_parquet(f'../raw/{filename}')
        df.to_sql(con=connection, schema='raw', name=normalFilename, if_exists='replace')

if __name__ == "__main__":
    main()
