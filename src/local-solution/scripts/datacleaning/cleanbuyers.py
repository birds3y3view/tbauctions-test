import pandas as pd

def main():
    df = pd.read_parquet('../../raw/buyers.parquet')

    # Standardize column names
    df.rename(columns={
        "AUCTIONID": "auction_id",
        "id": "id",
        "name": "name",
        "email": "email",
        "username": "username"
    }, inplace=True)

    # Remove rows with NA in them -- currently not required
    df.dropna(inplace = True)

    # Drop duplicates
    df.drop_duplicates(inplace = True)

    df.to_parquet('../../clean/buyers.parquet')

if __name__ == "__main__":
    main()

