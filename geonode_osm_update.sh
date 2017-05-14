#!/bin/bash

#### Script to update OSM layers in Nepal-Geonode ####
# NOTE: Make sure that the user running this script has a proper access level
# for handling database

USER_HOME=/home/geosolutions

# URL to use to download the pbf data
URL=http://download.geofabrik.de/asia/nepal-latest.osm.pbf

OSM_EXTRACT_CODE_PATH="${USER_HOME}/osm-extract/"
GEONODE_CODE_PATH="${USER_HOME}/nepal_geonode/"
GEONODE_VENV_PATH="${USER_HOME}/venvs/nepal_geonode/bin/activate"

# Open the directory containing the OSM extract code
cd $OSM_EXTRACT_CODE_PATH

# Execute code to fetch and update OSM data in postgis database
make all URL=$URL NAME=nepal

# Update published date in Nepal-Geonode database
psql -d nepal_geonode -c "update base_resourcebase set date = current_date where id in (select resourcebase_ptr_id from layers_layer where store = 'nepal_osm');"

# Change directory to Nepal-Geonode
cd $GEONODE_CODE_PATH

# Activate virtual environment
source $GEONODE_VENV_PATH

# Update layers in geonode nepal
python manage.py updatelayers
