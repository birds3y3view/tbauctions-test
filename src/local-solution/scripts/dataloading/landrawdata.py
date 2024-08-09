import pandas as pd
import os

for filename in os.listdir('../../data'):
    normalFilename = os.path.splitext(filename)[0]
    df = pd.read_csv(f'../../data/{filename}')
    df.to_parquet(f'../../raw/{normalFilename}.parquet')
