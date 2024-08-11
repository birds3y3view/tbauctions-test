# This subfolder contains the local version of the solution

## Pre-requisites:

The localized docker postgresql must be running for this pipeline to function correctly.
To do so run the following commands in the localdb directory:
```
docker build -t auctiondb .

docker run --name auctiondb -p 5432:5432 -e POSTGRES_PASSWORD=thepasswordispassword -d auctiondb
```

To remove the database when done run the following commands:
```
docker kill auctiondb

docker remove auctiondb
```

## Pipeline steps

Navigate to the scripts directory and run the following commands:
```
pip install -r requirements.txt

python execute-pipeline.py
```