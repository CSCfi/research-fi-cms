#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE djangocms;
    CREATE USER cmsuser WITH ENCRYPTED PASSWORD 'mysecretpasswd';
    ALTER ROLE cmsuser SET client_encoding TO 'utf8';
    ALTER ROLE cmsuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE cmsuser SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE djangocms TO cmsuser;
    ALTER USER cmsuser WITH superuser;
EOSQL