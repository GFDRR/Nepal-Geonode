#!/bin/bash
cd /usr/src/backups/db
psql -v ON_ERROR_STOP=1 -h db --username "postgres" <<-EOSQL
		drop database npl_geo;
		drop database npl_geo_data;
	    CREATE DATABASE npl_geo;
	    CREATE DATABASE npl_geo_data;
EOSQL
psql -U npl_geo_user -h db npl_geo<npl_geo.sql
psql -U npl_geo_user -h db npl_geo_data<npl_geo_data.sql

### To dump database
# pg_dump npl_geo>npl_geo.sql
# pg_dump npl_geo_data>npl_geo_data.sql
