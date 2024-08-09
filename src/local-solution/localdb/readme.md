# Local Docker Postgres Database in a box!

## Setup instructions

This container contains a skeleton to also set up schemas and users upon init.

The following code can be executed in the /src/db directory to spin up a fresh dockerized postgresql db:

```
docker build -t xdb .

docker run --name xdb -p 5432:5432 -e POSTGRES_PASSWORD=thepasswordispassword -d xdb
```

## Next Steps for improvement
* Define more specific roles with minimal access requirements for:
    * loader = Loading process, write on curated schema
    * analyst = Read only on relevant db tables
    * developer = Limited write access
    * etc...
* Parameterise further
* Integrate with a secrets manager