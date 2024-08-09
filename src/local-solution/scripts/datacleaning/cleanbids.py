import pandas as pd

def main():
    df = pd.read_parquet('../../raw/bids.parquet')

    # Standardize column names
    df.rename(columns={
        "AUCTIONID": "auction_id",
        "bid": "bid",
        "bidder": "bidder",
        "OpenBid": "open_bid",
        "price": "price",
        "item": "item",
        "auction_type": "auction_type",
        "datetime": "datetime",
        "ITEMID": "item_id",
        "item_description": "item_description"
    }, inplace=True)

    # Remove rows with NA in them -- currently not required
    df.dropna(inplace = True)

    # Drop duplicates
    df.drop_duplicates(inplace = True)

    # Normalize Dates
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Normalize Doubles
    for col in ['bid', 'open_bid', 'price']:
        df[col] = df[col].astype(float)

    df.to_parquet('../../clean/bids.parquet')

if __name__ == "__main__":
    main()

