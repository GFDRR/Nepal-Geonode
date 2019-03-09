FROM python:2.7.14
MAINTAINER GeoNode development team

RUN mkdir -p /usr/src/{app,geonode}

WORKDIR /usr/src/app

# This section is borrowed from the official Django image but adds GDAL and others
RUN apt-get update 
RUN apt-get install -y \
		gcc \
		gettext \
		postgresql-client libpq-dev \
		sqlite3 \
                python-gdal python-psycopg2 \
                python-imaging python-lxml \
                python-dev libgdal-dev \
                python-ldap \
                libmemcached-dev libsasl2-dev zlib1g-dev \
                python-pylibmc \
                osmosis \
                gdal-bin \
                cron \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*


COPY ./compose/production/django/wait-for-databases.sh /usr/bin/wait-for-databases
RUN chmod +x /usr/bin/wait-for-databases

COPY ./compose/production/django/crontab /etc/cron.d/geonode-task
RUN chmod 0644 /etc/cron.d/geonode-task
RUN service cron start



# Upgrade pip
RUN pip install --upgrade pip

# To understand the next section (the need for requirements.txt and setup.py)
# Please read: https://packaging.python.org/requirements/

# python-gdal does not seem to work, let's install manually the version that is
# compatible with the provided libgdal-dev
RUN pip install GDAL==1.10 --global-option=build_ext --global-option="-I/usr/include/gdal"

# install shallow clone of geonode master branch
# RUN git clone --depth=1 git://github.com/GeoNode/geonode.git --branch master /usr/src/geonode
# RUN cd /usr/src/geonode/; pip install --upgrade --no-cache-dir -r requirements.txt; pip install --upgrade -e .


COPY ./compose/production/django/tasks.py /usr/src/app/
COPY ./compose/production/django/entrypoint.sh /usr/src/app/

RUN chmod +x /usr/src/app/tasks.py \
    && chmod +x /usr/src/app/entrypoint.sh


COPY ./requirements.txt /usr/src/app/
RUN pip install celery
RUN cd /usr/src/app/; pip install --upgrade --no-cache-dir -r requirements.txt
COPY . /usr/src/app
RUN cd /usr/src/app/; pip install --upgrade -e .
RUN pip install --upgrade --no-cache-dir -r requirements.txt
RUN pip install -e /usr/src/app --upgrade

RUN python manage.py makemigrations --settings=geonode.settings
RUN python manage.py migrate --settings=geonode.settings

RUN pip install -r requirements1.txt

RUN chmod +x /usr/src/app/tasks.py \
    && chmod +x /usr/src/app/entrypoint.sh

RUN sed -i 's/"srid": resource.srid/"srid": resource.projection,/g' /usr/local/lib/python2.7/site-packages/geonode/geoserver/helpers.py

COPY ./compose/production/django/helpers.py /usr/local/lib/python2.7/site-packages/geonode/geoserver/helpers.py

COPY ./compose/production/django/helpers.py /usr/local/lib/python2.7/site-packages/geonode/layers/views.py

EXPOSE 8000

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["uwsgi", "--ini", "/usr/src/app/uwsgi.ini"]
