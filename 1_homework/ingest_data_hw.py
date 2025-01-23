import pandas as pd
from sqlalchemy import create_engine
import os

taxi_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz"
zones_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"
taxi_gz_fpath = os.path.join(os.getcwd(), "green_taxi.csv.gz")
taxi_csv_fpath = os.path.join(os.getcwd(), "green_taxi.csv")
zones_csv = os.path.join(os.getcwd(), "zones.csv")

# download the data to local machine 
os.system(f"wget -O {taxi_gz_fpath} {taxi_url}")
os.system(f"gunzip {taxi_gz_fpath}")
os.system(f"wget -O {zones_csv} {zones_url}")


# create an engine to connect to postgres 
engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")
engine.connect()

# ingest data 
print("importing zone data")
output = zones_df.to_sql(name="zone_data", con=engine, if_exists='replace')
print(f"{output}(ish) rows from zone data imported")

print(pd.io.sql.get_schema(frame=zones_df, name="ny_taxi", con=engine))
print(pd.io.sql.get_schema(frame=taxi_df, name="ny_taxi", con=engine))

# split data into chunks of 100,000 and create an iterator 
taxi_iter = pd.read_csv(taxi_csv_fpath, iterator=True, chunksize=100000)

# iterate over data chunks and upload each to the postgres database via engine
for i, df_chunk in enumerate(taxi_iter):
    print(f"Importing chunk {i} in green taxi data...")
    df_chunk["lpep_pickup_datetime"] = pd.to_datetime(df_chunk.lpep_pickup_datetime)
    df_chunk["lpep_dropoff_datetime"] = pd.to_datetime(df_chunk.lpep_dropoff_datetime)
    output = df_chunk.to_sql(name='green_taxi_data', con=engine, if_exists='append')
    print(f"...{output}(ish) rows from taxi data imported")  # output from df.to_sql is not guaranteed to be actual # rows written


print("done ingesting...yum")



