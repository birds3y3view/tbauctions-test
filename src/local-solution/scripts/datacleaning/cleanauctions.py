import pandas as pd

def main():
    df = pd.read_parquet('../../raw/auctions.parquet')

    # Standardize column names
    df.rename(columns={
        "auctionid": "auction_id", 
        "auction_type": "auction_type", 
        "seller_id": "seller_id", 
        "name": "name", 
        "email": "email", 
        "username": "username"
    }, inplace=True)

    # Remove rows with NA in them -- currently not required
    df.dropna(inplace = True)

    # Drop duplicates
    df.drop_duplicates(inplace = True)

    df.to_parquet('../../clean/auctions.parquet')

if __name__ == "__main__":
    main()

