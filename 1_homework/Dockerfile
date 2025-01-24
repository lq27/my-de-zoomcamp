# dockerfile for the python ingestion script, ingest_data_hw.py

FROM python:3.9 

RUN apt-get install wget
RUN pip install pandas sqlalchemy argparse psycopg2

# sets working directory in the container environment for the command after it
WORKDIR /appdata 

COPY ingest_data_hw.py .

ENTRYPOINT [ "python", "ingest_data_hw.py" ]