---------------------------------
MODULE 2 HW
---------------------------------

1. 128.3 MB

For this task, I disabled the final purge task so that the csv is not deleted at the end of the flow. 
Then, I checked the Outputs tab for the kestra execution. Alternatively, you can check the GCP bucket 
if you are doing this in the cloud, to see the csv file saved there. 

2. "green_tripdata_2020-04.csv"

This is the definition of the file variable
file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"

So, once it's rendered, the stuff in {{brackets}} will be replaced by those variables, which are inputs. 
"green_tripdata_2020-04.csv"

3. 24,648,499

I ran the GCP scheduled ingestion workflow with backfill from Jan 1 2020 - Dec 31 2020. Then I opened the 
yellow_tripdata db in GCP BQ, and queried it. Here is the query: 

SELECT count(*) FROM `kestra-sandbox-449722.zoomcamp.yellow_tripdata`

4. 1,734,051

I ran the GCP scheduled ingestion workflow with backfill from Jan 1 2020 - Dec 31 2020. Then I opened the 
green_tripdata db in GCP BQ, and queried it. Here is the query: 

SELECT COUNT(*) FROM `kestra-sandbox-449722.zoomcamp.green_tripdata`

5. 1,925,152

First I made sure to delete all of the existing yellow_tripdata_* tables in GCP earlier questions (to help automate this, i made a kestra
flow with scheduling so i could backfill all of the monthly csv's that need deleting - this flow is called "gcp_bq_delete_table", 
which is a template flow i adapted from https://kestra.io/plugins/plugin-gcp/tasks/bigquery/io.kestra.plugin.gcp.bigquery.deletetable)

Then I ran the "gcp_taxi_ingest" flow for just march 2023 yellow taxis. 

Then i performed a SQL query in BigQuery to find the number of rows: 
SELECT COUNT(*) FROM `kestra-sandbox-449722.zoomcamp.yellow_tripdata_2021_03` 

6. Set timezone property to America/New_York

Source traceback (in reverse order, i.e. in the order that i searched them):
https://kestra.io/docs/workflow-components/triggers
https://kestra.io/docs/workflow-components/triggers/schedule-trigger
https://kestra.io/plugins/core/triggers/io.kestra.plugin.core.trigger.schedule
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones