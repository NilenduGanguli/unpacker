#!/bin/bash
set -e

# Check if the table exists and create if not
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER myappuser WITH PASSWORD 'apppassword';
    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO myappuser;

    \connect $POSTGRES_DB;

    \i /docker-entrypoint-initdb.d/init.sql;

EOSQL
