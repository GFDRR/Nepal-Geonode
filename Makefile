loaddata:
	# Load fixture data
	python manage.py loaddata fixture/initial_data.json
	python manage.py loaddata fixture/default_oauth_apps.json
	python manage.py loaddata fixture/sample_admin.json

restart:
	sudo service uwsgi-emperor restart
	sudo service nginx restart

pull:
	git reset --hard HEAD
	git pull

deploy: pull restart
