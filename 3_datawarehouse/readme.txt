-------------------
Module 3 Homework 
-------------------

1. 20,332,093

See Q1_SQL 

2. 0 MB for the External Table and 155.12 MB for the Materialized Table

> for materialized table:
This query will process 155.12 MB when run. 

> for external table:
This query will process 0 B when run. 

See Q2_SQL 

3. Answer:
"BigQuery is a columnar database, and it only scans the specific 
columns requested in the query. Querying two columns (PULocationID, DOLocationID) 
requires reading more data than querying one column (PULocationID), leading to a higher 
estimated number of bytes processed."

> for only PULocationID: 
This query will process 155.12 MB when run. 

> for PULocationID and DOLocationID : 
This query will process 310.24 MB when run. 

See Q3_SQL

4. 8,333

See Q4_SQL

5. Partition by tpep_dropoff_datetime and Cluster on VendorID

- Because you will filter on dropoff, so you'll only need to access some partitions. 
- And then your data will already be clustered by vendor ID within the partitions you 
need to access
-You don't want to partition on VendorID because you'll need all of them so you'd have
to access every partition which defeats the purpose 
-You could cluster the dropoff datetime, but it may be better to just partition it since
it should be well under 4000 partitions and you'll be filtering on it. 

See Q5_SQL 

6. 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

> Partitioned and clustered data: 
This query will process 26.84 MB when run.

> Non partitioned data: 
This query will process 310.24 MB when run.

See Q6_SQL 

7. GCP Bucket

8. False 

Clustering is only helpful for large data sets, otherwise the overhead actually slows things down. 

9. 0B of data

The number of records (essentially what count(*) does) is in the metadata for the table, so you don't actually have to process anything. 