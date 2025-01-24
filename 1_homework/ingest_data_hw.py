import pandas as pd
from sqlalchemy import create_engine
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data_url", type=str, required=True)
parser.add_argument("--engine", type=str, required=True)
parser.add_argument("--tablename", type=str, required=True)

args = parser.parse_args() 
data_url = args.data_url
engine_addr = args.engine
table_name = args.tablename

# figure out destination filepaths for the data download
is_data_gz = False
wget_data_filename = "data.csv"
if data_url.endswith(".gz"):
    is_data_gz = True
    wget_data_filename = "data.csv.gz"
    
wget_url_fpath = os.path.join(os.getcwd(), wget_data_filename)  # destination filepath after calling wget on url
csv_fpath = os.path.join(os.getcwd(), "data.csv")  # filepath for final csv (same as wget_url_fpath if not a zipped file)

# download the data to local machine 
os.system(f"wget -O {wget_url_fpath} {data_url}")
if is_data_gz:
    os.system(f"gunzip {wget_url_fpath}")

# create an engine to connect to postgres 
engine = create_engine(engine_addr)
engine.connect()

# ingest data - split data into chunks of 100,000 and create an iterator 
data_iter = pd.read_csv(csv_fpath, iterator=True, chunksize=100000)  # if <100k rows, will just get 1 chunk 

# iterate over data chunks and upload each to the database via engine
for i, df_chunk in enumerate(data_iter):
    print(f"Importing chunk {i} of data...")
    # df_chunk["lpep_pickup_datetime"] = pd.to_datetime(df_chunk.lpep_pickup_datetime)
    # df_chunk["lpep_dropoff_datetime"] = pd.to_datetime(df_chunk.lpep_dropoff_datetime)
    output = df_chunk.to_sql(name=table_name, con=engine, if_exists='append')
    print(f"...{output}(ish) rows from data imported")  # output from df.to_sql is not guaranteed to be actual # rows written

# remove gz/csv files created 
os.remove(wget_url_fpath)
if is_data_gz:
    os.remove(csv_fpath)

print("done ingesting...yum")



