GeoNode for Nepal
=================

Setup instructions:
-----------------------------------

 1. Install external dependencies as follows:
	```
	# Install Ubuntu dependencies
	sudo apt update
	sudo apt install python-virtualenv python-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev libjpeg-dev libpq-dev libgdal-dev git default-jdk
    
	# Install Java 8 (needed by latest GeoServer 2.9)
	sudo apt install oracle-java8-installer 
	```
 2. Create a new virtualenv with python 2.x
 3. Clone this repo
 4. Install project dependencies using 
	`pip install -r requirements.txt`

 5. Install gdal-bin and pygdal
	```
	sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update
	sudo apt-get install gdal-bin
	# Check GDAL version
	gdalinfo --version
		
	# install the correct PyGDAL version (>1.10.1)
	pip install pygdal==`gdal-config --version`
	
	# if you cannot find exactly the same version, be sure to install at least the closer major one e.g. 2.1.2 -> 2.1.2.3
	```

 6. Setup postgres databases as follows:
	```
	$ su postgres
	$ createdb nepal_geonode
	$ createdb nepal_geonode_data
	$ psql
		postgres=#
		postgres=# \password postgres
		postgres=# CREATE USER nepal_geonode WITH PASSWORD '$PASSWORD_HERE';
		postgres=# GRANT ALL PRIVILEGES ON DATABASE "nepal_geonode" to nepal_geonode;
		postgres=# GRANT ALL PRIVILEGES ON DATABASE "nepal_geonode_data" to nepal_geonode;
		postgres=# \q

	$ psql -d nepal_geonode_data -c 'CREATE EXTENSION postgis;'
	$ psql -d nepal_geonode_data -c 'GRANT ALL ON geometry_columns TO PUBLIC;'
	$ psql -d nepal_geonode_data -c 'GRANT ALL ON spatial_ref_sys TO PUBLIC;'
	$ exit
	```
 7.  paver setup
 8.  paver sync

Instruction to run project:
-----------------------------------
 - **Run geoserver using**
 
	`paver start_geoserver`

 - **Run django server using**
 
	`python manage.py runserver`

