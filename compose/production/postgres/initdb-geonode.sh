#!/bin/bash
set -e

function create_geonode_user_and_database() {
	local db=$1
	echo "  Creating user and database '$db'"
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	    CREATE USER $db;
		ALTER USER $db with encrypted password '$GEONODE_DATABASE_PASSWORD';
	    CREATE DATABASE $db;
	    GRANT ALL PRIVILEGES ON DATABASE $db TO $db;
EOSQL
}

function create_geonode_user_and_geodatabase() {
	local geodb=$1
	echo "  Creating user and database '$geodb'"
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	    CREATE USER $geodb;
		ALTER USER $geodb with encrypted password '$GEONODE_GEODATABASE_PASSWORD';
	    CREATE DATABASE $geodb;
	    GRANT ALL PRIVILEGES ON DATABASE $geodb TO $geodb;
EOSQL
}

function update_geodatabase_with_postgis() {
	local geonode_data=$1
	echo "  Updating geodatabase '$geonode_data' with extension"
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$geonode_data" <<-EOSQL
		CREATE EXTENSION postgis;
EOSQL
}


function create_user() {
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
		CREATE USER $GEONODE_USER;
		ALTER USER $GEONODE_USER with encrypted password '$GEONODE_USER_PASSWORD';
		ALTER USER $GEONODE_USER WITH SUPERUSER;
EOSQL
}

create_user

if [ -n "$GEONODE_DATABASE" ]; then
	echo "Geonode database creation requested: $GEONODE_DATABASE"
	create_geonode_user_and_database $GEONODE_DATABASE
	echo "Geonode database created"
fi

if [ -n "$GEONODE_GEODATABASE" ]; then
	echo "Geonode geodatabase creation requested: $GEONODE_GEODATABASE"
	create_geonode_user_and_geodatabase $GEONODE_GEODATABASE
	update_geodatabase_with_postgis $GEONODE_GEODATABASE
	echo "Geonode geodatabase created"
fi

if [ -n "$POSTGRES_MULTIPLE_DATABASES" ]; then
	echo "Multiple database creation requested: $POSTGRES_MULTIPLE_DATABASES"
	for db in $(echo $POSTGRES_MULTIPLE_DATABASES | tr ',' ' '); do
		create_geonode_user_and_geodatabase $db
		update_geodatabase_with_postgis $db
	done
	echo "Multiple databases created"
fi

