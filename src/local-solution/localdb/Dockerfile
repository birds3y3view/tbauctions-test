FROM postgres:14.3

ENV POSTGRES_USER="admin"
ENV POSTGRES_DB="auctiondb"

COPY /init /docker-entrypoint-initdb.d

