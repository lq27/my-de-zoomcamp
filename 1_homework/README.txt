HW Answers 
------------------
All of my work was done on a GCP VM using linux shell running on ubuntu. 

1. 24.3.1 

Bash command used plus output:

$ docker run -it --entrypoint "/bin/bash" python:3.12.8
root@b93ca6521d5d:/# pip --version
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)

2.

Hostname: "postgres" since that is the container name. If there were no container_name specified, then it would be "db," the service name. 
Port: 5432. The port mapping is <localhost port>:<container port> . Pgadmin will want to access postgres's container port, since 
postgres and pgadmin are both containers, seeing each other within the docker network. 

~~ PREPARE POSTGRES ~~

My approach: 
(a) Set up localhost volume/folder to map to docker data
(b) Set up pgadmin and set up postgres (use a docker-compose file to keep them in the same network)
(c) Postgres ingestion of Green taxi trips from Sept 2019 via python script 
    > Tested out in notebook for ease of exploration
    > Converted nb to python script: $jupyter nbconvert --to=script ingest_data_hw.ipynb
(d) Build a docker image forpython script & run ingestion script container in the same network as pgadmin/postgres to ingest

Local volume: /my-de-zoomcamp/1_homework/green_taxi_data
Docker-compose file: /my-de-zoomcamp/1_homework/docker-compose.yaml
Python script: /my-de-zoomcamp/1_homework/ingest_data.ipynb
Dockerfile (for python script custom image, part D): /my-de-zoomcamp/1_homework/Dockerfile

Bash commands in order: 

$ cd my-de-zoomcamp/1_homework/
$ docker build -t ingest_data:v0 .
$ docker-compose -p pgd up
$ docker run \
    --network pgd_default ingest_data:v0 \
    --data_url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz" \
    --engine="postgresql://root:root@pgdatabase:5432/ny_taxi" \
    --tablename="green_taxi"
$ docker run \
    --network pgd_default ingest_data:v0 \
    --data_url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"
    --engine="postgresql://root:root@pgdatabase:5432/ny_taxi"
    --tablename="zones"

Note: I used localhost:5433 mapped to docker port 5432 because my local postgres generally has already taken up my 
localhost:5432, and I find it annoying to stop the postgres process each time I restart my VM. I also forwarded 
my remote(VM) localhost:5433 to my laptop's localhost:5433. 

Improvements I would make for a real project:
1. Ingesting one data file per python script is not ideal. Instead, I would make it so that I could pass multiple 
  data sources to the python file and have it ingest each. 
2.  Define arguments for different parts of the database engine URL
3.  Currently, I am building a docker image for the python environment and manually running it for each data table. 
  Instead, along with (1), I would include this python container as a service in the docker-compose file with pgadmin
  and postgres (so that they are in the same network), include all of the data source urls in an environment variable, 
  and pass this arg "array" to the python script to ingest all of the data tables in one run. 
  
  Or, have an input document (potentially csv) which specified  "desired_table_name, data_source url", 
  with one row for each data source. Then have the python script accept that input file and loop over to ingest each 
  data source. This is more scalable. 
-------------------------

3. See "sql_3" file for SQL queries used. 
Answer: # 2 : 104,802; 198,924; 109,603; 27,678; 35,189

Note: I needed to ensure that the dropoff time was in the October 2019 time window, not just pickup time. 
Since some trips started on Oct 31 but finished on Nov 1 (these would not be included). 

4. See "sql_4" file. 
Answer: 2019-10-31 with 515.89 mile trip distance. 

5. See "sql_5" file. 
Answer: East Harlem North, East Harlem South, Morningside Heights

6. See "sql_6" file. 
Answer: JFK Airport

7. 
Terraform init downloads the provider and sets up backend. 
Terraform apply -auto-approve would actualize the changes proposed in a tf plan, and autoapprove would bypass the need to 
    confirm the changes. 
Terraform destroy removes tf-managed resources. 

The steps in this question skip over terraform plan, which would be between init and apply, wher you create a plan of 
actions that you want to take, before actually applying them. It is not necessary, but probably a good idea. 

----------------------------------------------------------------------------------------------------------------------------
OOPS! wrong hw qs from last year: 

1. 
--rm: docker run --help                              
    Automatically remove the container and its associated anonymous volumes when it exits

2. 
Command used, along with output: 

$ docker run -it --entrypoint "/bin/bash" python:3.9
root@2742bf341812:/# pip list
Package    Version
---------- -------
pip        23.0.1
setuptools 58.1.0
wheel      0.45.1
