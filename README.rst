==================
 GeoNode for Nepal
==================

Setup instructions (need refining):
===================================

1. Create a new virtualenv with python2
2. Clone this repo
3. Set environment variables in the postactivate script::

    cd $VIRTUAL_ENV/bin/
    vim postactivate
    export DJANGO_SETTINGS_MODULE='config.settings.local'

    vim postdeactivate
    unset DJANGO_SETTINGS_MODULE
4. pip install -r requirements/local.txt::

       $ su postgres
       $ createdb nepalnode
       $ createdb nepalnode-imports
       $ psql
         postgres=#
         postgres=# \password postgres
         postgres=# CREATE USER nepalnode WITH PASSWORD 'nepalnode';
         postgres=# GRANT ALL PRIVILEGES ON DATABASE "nepalnode" to nepalnode;
         postgres=# GRANT ALL PRIVILEGES ON DATABASE "nepalnode-imports" to nepalnode;
         postgres=# \q

       $ psql -d nepalnode-imports -c 'CREATE EXTENSION postgis;'
       $ psql -d nepalnode-imports -c 'GRANT ALL ON geometry_columns TO PUBLIC;'
       $ psql -d nepalnode-imports -c 'GRANT ALL ON spatial_ref_sys TO PUBLIC;'

       $ exit
5. paver setup
6. paver sync
7. Follow: http://docs.geonode.org/en/master/tutorials/devel/devel_env/index.html



