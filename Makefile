.PHONY: migrate
migrate:
	python manage.py makemigrations
	python manage.py migrate

.PHONY: run
run:
	python manage.py runserver