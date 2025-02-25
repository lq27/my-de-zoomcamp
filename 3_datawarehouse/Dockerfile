FROM python:alpine3.20

RUN pip install --no-cache-dir google-cloud-storage

COPY load_yellow_taxi_data.py /load_yellow_taxi_data.py
COPY gcp_key/rclone-446420-a9a8eec51226.json /gcp_key/rclone-446420-a9a8eec51226.json

CMD [ "python",  "load_yellow_taxi_data.py"]