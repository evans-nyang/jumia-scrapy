#!/bin/bash

# Create an admin user in your metadata database (use `admin` as username to be able to load the examples)
export FLASK_APP=superset
superset fab create-admin \
--username ${SUPERSET_USER} \
--firstname ${FIRST_NAME} \
--lastname ${LAST_NAME} \
--email ${EMAIL} \
--password ${SUPERSET_PASSWORD} 

# Load some data to play with
# superset load_examples

superset db upgrade

# Create default roles and permissions
superset init

# Build javascript assets
# cd superset-frontend
# npm ci
# npm run build


# To start a development web server on port 8088, use -p to bind to another port
# superset run -p 8088 --with-threads --reload --debugger
