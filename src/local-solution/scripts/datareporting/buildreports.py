from sqlalchemy import create_engine
import pandas as pd
import os
import matplotlib.pyplot as plt

def main():
    username = "admin"
    password = "thepasswordispassword"
    ipaddress = "localhost"
    port = "5432"
    dbname = "auctiondb"

    postgres_str = f'postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
    connection = create_engine(postgres_str)

    # for sql in os.listdir('reports'):
    #     table_name = os.path.splitext(sql)[0]

    #     with open(f'reports/{sql}') as query:
    #         df = pd.read_sql_query(f"""{query.read()}""", connection)
    #         plt.figure()
    #         df['count'].value_counts().plot(kind='hist')
    #         plt.savefig('out1.pdf')

    with open(f'reports/r_auction_type_bids_dist.sql') as query:
        df = pd.read_sql_query(f"""{query.read()}""", connection)
        plt.figure()
        graphic = df.hist('count', by='auction_type', bins=15)
        for ax in graphic.flatten():
            ax.set_xlabel("Bids")
            ax.set_ylabel("Frequency")
        plt.savefig('../reporting/r_auction_type_bids_dist.pdf')

    with open(f'reports/r_item_bids_dist.sql') as query:
        df = pd.read_sql_query(f"""{query.read()}""", connection)
        plt.figure()
        graphic = df.hist('count', by='item', bins=15)
        for ax in graphic.flatten():
            ax.set_xlabel("Bids")
            ax.set_ylabel("Frequency")
        plt.savefig('../reporting/r_item_bids_dist.pdf')

if __name__ == "__main__":
    main()
