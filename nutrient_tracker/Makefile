dev-start:
	python manage.py runserver --settings=config.settings.dev

dev-install:
	pip install -r requirements/dev.txt

dev-showmigrations:
	python manage.py showmigrations --settings=config.settings.dev

dev-makemigrations:
	python manage.py makemigrations --settings=config.settings.dev

dev-migrate:
	python manage.py migrate  --settings=config.settings.dev

dev-superuser:
	python manage.py createsuperuser  --settings=config.settings.dev

dev-test:
	python manage.py test --verbosity=2 --settings=config.settings.dev

dev-loaddata:
	python manage.py loaddata ${filename} --settings=config.settings.dev

dev-shell:
	python manage.py shell --settings=config.settings.dev